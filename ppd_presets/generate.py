"""Synthetic households and their decisions on every core item.

Each household gets latent traits (config/generator.yaml). Its decision on an item follows from those traits:

    u = intercept + benefit_weight * benefit[purpose] * (0.5 + benefit_orientation)
        - risk_weight * sensitivity[data_type] * exposure(recipient, action) * (0.6 + concern)
        - source_term[source] + noise

    allow                if u >= 0
    allow if <limit>     else, if a modifier available for the item lifts u to >= 0 (checked in the order
                         ephemeral retention, in-home processing, on-device processing)
    deny                 otherwise

Traits are continuous (not personas), so clustering has to find structure rather than recover a planted one.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from scipy import stats

from .items import LIMIT_EPHEMERAL, LIMIT_IN_HOME, LIMIT_ON_DEVICE
from .taxonomy import ACTIONS, BOUNDARY_ACTIONS, DATA_TYPES, HANDLING_CONTEXTS, PURPOSES, SOURCES

# Decision codes stored in decisions.npy.
DENY, ALLOW, ALLOW_IF_EPHEMERAL, ALLOW_IF_IN_HOME, ALLOW_IF_ON_DEVICE = 0, 1, 2, 3, 4
DECISION_CODES = {
    DENY: "deny",
    ALLOW: "allow",
    ALLOW_IF_EPHEMERAL: f"allow_if:{LIMIT_EPHEMERAL}",
    ALLOW_IF_IN_HOME: f"allow_if:{LIMIT_IN_HOME}",
    ALLOW_IF_ON_DEVICE: f"allow_if:{LIMIT_ON_DEVICE}",
}
# Ordinal value for clustering: deny 0, any "allow if limited" 0.5, allow 1.
ORDINAL = np.array([0.0, 1.0, 0.5, 0.5, 0.5], dtype=np.float32)

TRAITS = ["concern", "vendor_trust", "third_party_aversion", "inference_aversion", "retention_sensitivity", "benefit_orientation"]


def load_config(path: str | Path) -> dict:
    return yaml.safe_load(Path(path).read_text())


@dataclass
class Synthetic:
    households: pd.DataFrame   # household_id, traits, children, sensitivity per data type
    decisions: np.ndarray      # uint8 [households x items], DECISION_CODES
    utility: np.ndarray        # float32 [households x items], the u before limits (for diagnostics)


def draw_traits(cfg: dict, rng: np.random.Generator) -> pd.DataFrame:
    """Correlated latent traits through a Gaussian copula with Beta marginals."""
    n = cfg["n_households"]
    k = len(TRAITS)
    corr = np.eye(k)
    for pair, r in (cfg.get("trait_correlation") or {}).items():
        a, b = pair.split("|")
        i, j = TRAITS.index(a), TRAITS.index(b)
        corr[i, j] = corr[j, i] = r
    z = rng.multivariate_normal(np.zeros(k), corr, size=n)
    u = stats.norm.cdf(z)
    df = pd.DataFrame({"household_id": np.arange(n)})
    for i, name in enumerate(TRAITS):
        a, b = cfg["traits"][name]["beta"]
        df[name] = stats.beta.ppf(u[:, i], a, b)
    df["children"] = rng.random(n) < cfg["household"]["children_rate"]
    return df


def data_sensitivity(cfg: dict, hh: pd.DataFrame, rng: np.random.Generator) -> np.ndarray:
    """[households x data types] sensitivity in 0..1."""
    s = cfg["data_type_sensitivity"]
    base = np.array([s["base"][d] for d in DATA_TYPES])
    shift = s["concern_shift"] * (hh.concern.to_numpy() - 0.5)
    sens = base[None, :] + shift[:, None] + rng.normal(0, s["noise_sd"], size=(len(hh), len(DATA_TYPES)))
    bonus = np.array([s.get("children_bonus", {}).get(d, 0.0) for d in DATA_TYPES])
    sens += hh.children.to_numpy()[:, None] * bonus[None, :]
    return np.clip(sens, 0.0, 1.0)


def _term(spec: dict, hh: pd.DataFrame) -> np.ndarray:
    """base + weight * trait, per household."""
    value = np.full(len(hh), float(spec.get("base", 0.0)))
    if "trait" in spec:
        value = value + float(spec["weight"]) * hh[spec["trait"]].to_numpy()
    return value


def generate(cfg: dict, items: pd.DataFrame, chunk: int = 1000) -> Synthetic:
    rng = np.random.default_rng(cfg["seed"])
    hh = draw_traits(cfg, rng)
    sens = data_sensitivity(cfg, hh, rng)
    for j, d in enumerate(DATA_TYPES):
        hh[f"sens_{d.split(':')[1]}"] = sens[:, j]

    ex, ut, lim = cfg["exposure"], cfg["utility"], cfg["limits"]
    recipient = np.stack([_term(ex["recipient"][c], hh) for c in HANDLING_CONTEXTS], axis=1)  # [h x 4]
    action = np.stack([_term(ex["action"][a], hh) for a in ACTIONS], axis=1)                   # [h x 4]
    benefit = np.array([cfg["purpose_benefit"][p] for p in PURPOSES])
    source = np.array([cfg["source_term"][s] for s in SOURCES])

    d_idx = items.data_type.map(DATA_TYPES.index).to_numpy()
    p_idx = items.purpose.map(PURPOSES.index).to_numpy()
    a_idx = items.action.map(ACTIONS.index).to_numpy()
    s_idx = items.source.map(SOURCES.index).to_numpy()
    c_idx = items.handling_context.map(HANDLING_CONTEXTS.index).to_numpy()
    home = ~items.leaves_home.to_numpy()
    boundary_ok = items.action.isin(BOUNDARY_ACTIONS).to_numpy()

    n, m = len(hh), len(items)
    decisions = np.zeros((n, m), dtype=np.uint8)
    utility = np.zeros((n, m), dtype=np.float32)
    concern = hh.concern.to_numpy()
    orient = hh.benefit_orientation.to_numpy()
    retention = hh.retention_sensitivity.to_numpy()

    for start in range(0, n, chunk):
        sl = slice(start, min(start + chunk, n))
        s_h = sens[sl][:, d_idx]                                   # sensitivity of each item's data type
        act = action[sl][:, a_idx]
        rec = recipient[sl][:, c_idx]
        exposure = np.where(home[None, :], ex["home_base"] + ex["home_action_scale"] * act, ex["away_base"] + rec + act)
        scale = ut["risk_weight"] * s_h * (0.6 + concern[sl, None])  # risk per unit of exposure
        u = (ut["intercept"]
             + ut["benefit_weight"] * benefit[p_idx][None, :] * (0.5 + orient[sl, None])
             - scale * exposure
             - source[s_idx][None, :]
             + rng.normal(0, ut["noise_sd"], size=(sl.stop - sl.start, m)))

        # What each modifier is worth for this household and item.
        gain_ephemeral = lim["ephemeral_gain"] * retention[sl, None] * s_h * np.where(home, lim["ephemeral_home_scale"], 1.0)[None, :]
        away_part = np.where(home[None, :], 0.0, rec)               # the recipient share of the exposure
        gain_in_home = np.where(boundary_ok[None, :], scale * lim["in_home_removes"] * away_part, -np.inf)
        gain_on_device = np.where(boundary_ok[None, :], scale * lim["on_device_removes"] * (away_part + np.where(home, ex["home_base"], 0.0)[None, :]), -np.inf)

        d = np.full(u.shape, DENY, dtype=np.uint8)
        d[(u + gain_on_device) >= 0] = ALLOW_IF_ON_DEVICE
        d[(u + gain_in_home) >= 0] = ALLOW_IF_IN_HOME
        d[(u + gain_ephemeral) >= 0] = ALLOW_IF_EPHEMERAL
        d[u >= 0] = ALLOW
        decisions[sl] = d
        utility[sl] = u.astype(np.float32)
    return Synthetic(households=hh, decisions=decisions, utility=utility)


def decisions_long(decisions: np.ndarray, items: pd.DataFrame, households: list[int], item_ids: list[int] | None = None) -> pd.DataFrame:
    """Readable long format for a subset of households (and of items)."""
    ids = range(decisions.shape[1]) if item_ids is None else item_ids
    rows = []
    for h in households:
        for i in ids:
            rows.append((h, i, DECISION_CODES[int(decisions[h, i])]))
    out = pd.DataFrame(rows, columns=["household_id", "item_id", "decision"])
    return out.merge(items[["item_id", "data_type", "purpose", "action", "source", "handling_context"]], on="item_id")
