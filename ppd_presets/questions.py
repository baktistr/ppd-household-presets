"""Candidate onboarding questions and how a synthetic household answers them.

The bank extends the app's seven questions (ppd-preference-app/public/mock/questionnaire.json): the two
matrix questions are split into one question per row, and two general questions are added. A decision tree
later picks the few that best predict a household's cluster.

Answers come from the same latent traits as the decisions, plus answer noise: people do not answer exactly in
line with their preferences. ``answer_noise`` sets how much.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .taxonomy import short

THREE = ["never", "ask", "fine"]

# Rows of the app's Q2 ("Which kinds of data should stay in your home?") as their own questions.
DATA_GROUPS = {
    "content": (["ppd:contentData"], "Video, photos and sound"),
    "location": (["ppd:locationData"], "Where you are"),
    "identity": (["ppd:identifierData", "ppd:profileData"], "Who you are (accounts, names, profile)"),
    "sensor": (["ppd:sensorData"], "Sensor readings (temperature, motion, …)"),
    "usage": (["ppd:usageData"], "How you use the device"),
    "network": (["ppd:deviceAndNetworkData"], "Device and network details"),
}

# Rows of the app's Q3 ("What may companies use your data for?").
PURPOSE_GROUPS = {
    "core": (["ppd:coreFunctionality", "ppd:security"], "Making a feature work, keeping it secure"),
    "comms": (["ppd:communicationsAndNotifications"], "Sending you alerts and messages"),
    "diag": (["ppd:diagnosticsAndMaintenance", "ppd:legalCompliance"], "Fixing problems, legal duties"),
    "analytics": (["ppd:analyticsAndImprovement"], "Improving their products"),
    "personal": (["ppd:personalization"], "Personalizing what you see"),
    "ads": (["ppd:advertisingAndMarketing"], "Advertising and marketing"),
}


def question_bank() -> list[dict]:
    """id, text, options, kind (for documentation and for the tree export)."""
    qs = [
        {"id": "children", "text": "Do children live in your home, or visit often?", "options": ["yes", "no"], "kind": "context"},
        {"id": "concern", "text": "How much do you worry about what smart devices do with your data?", "options": ["1", "2", "3", "4", "5"], "kind": "general"},
        {"id": "trust_maker", "text": "How much do you trust device makers with your data?", "options": ["1", "2", "3", "4", "5"], "kind": "general"},
    ]
    for key, (_, label) in DATA_GROUPS.items():
        qs.append({"id": f"data_{key}", "text": f"{label}: may it leave your home?", "options": THREE, "kind": "data"})
    for key, (_, label) in PURPOSE_GROUPS.items():
        qs.append({"id": f"purpose_{key}", "text": f"May companies use your data for: {label.lower()}?", "options": THREE, "kind": "purpose"})
    qs += [
        {"id": "sharing", "text": "May a device's maker pass your data to other companies?", "options": ["never", "ask", "features"], "kind": "recipient"},
        {"id": "inference", "text": "May companies work out extra things about you from your data?", "options": ["never", "ask", "ok"], "kind": "action"},
        {"id": "retention", "text": "How long may companies keep your data?", "options": ["briefly", "ask", "any"], "kind": "modifier"},
    ]
    return qs


def _three(score: np.ndarray, low: float, high: float, labels: list[str]) -> np.ndarray:
    """Score in 0..1 (higher = more permissive) -> labels[0] below low, labels[2] above high."""
    return np.where(score < low, labels[0], np.where(score > high, labels[2], labels[1]))


def _likert(score: np.ndarray) -> np.ndarray:
    return np.clip(np.rint(1 + 4 * score), 1, 5).astype(int).astype(str)


def answer(households: pd.DataFrame, cfg: dict, rng: np.random.Generator) -> pd.DataFrame:
    """One row per household, one column per question."""
    noise = cfg.get("answer_noise", 0.12)
    n = len(households)
    e = lambda: rng.normal(0, noise, n)  # noqa: E731
    concern = households.concern.to_numpy()
    out = pd.DataFrame({"household_id": households.household_id})
    out["children"] = np.where(households.children, "yes", "no")
    out["concern"] = _likert(np.clip(concern + e(), 0, 1))
    out["trust_maker"] = _likert(np.clip(households.vendor_trust.to_numpy() + e(), 0, 1))

    for key, (terms, _) in DATA_GROUPS.items():
        sens = households[[f"sens_{short(t)}" for t in terms]].to_numpy().mean(axis=1)
        permissive = 1 - sens * (0.6 + concern) / 1.6 + e()
        out[f"data_{key}"] = _three(permissive, 0.35, 0.65, THREE)

    benefit = cfg["purpose_benefit"]
    orient = households.benefit_orientation.to_numpy()
    for key, (terms, _) in PURPOSE_GROUPS.items():
        b = np.mean([benefit[t] for t in terms])
        permissive = 0.5 + 0.35 * b * (0.5 + orient) - 0.4 * (concern - 0.5) + e()
        out[f"purpose_{key}"] = _three(permissive, 0.4, 0.7, THREE)

    out["sharing"] = _three(1 - households.third_party_aversion.to_numpy() + e(), 0.3, 0.6, ["never", "ask", "features"])
    out["inference"] = _three(1 - households.inference_aversion.to_numpy() + e(), 0.3, 0.6, ["never", "ask", "ok"])
    out["retention"] = _three(1 - households.retention_sensitivity.to_numpy() + e(), 0.3, 0.6, ["briefly", "ask", "any"])
    return out
