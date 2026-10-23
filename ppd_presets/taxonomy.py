"""The PPD core taxonomy (draft-dsmullen-ppd-taxonomy-05, section 6).

Only core ``ppd:`` terms appear here. Vendor terms are reduced to these before they reach the matrix, so the
matrix never grows with vendors. tests/test_taxonomy.py checks this list against the app
(ppd-preference-app/shared/taxonomy.ts) when that repository is next to this one.
"""

# Section 6.2, Data Type (what)
DATA_TYPES = [
    "ppd:identifierData",
    "ppd:profileData",
    "ppd:sensorData",
    "ppd:contentData",
    "ppd:locationData",
    "ppd:deviceAndNetworkData",
    "ppd:usageData",
]

# Section 6.3, Purpose (why)
PURPOSES = [
    "ppd:coreFunctionality",
    "ppd:personalization",
    "ppd:communicationsAndNotifications",
    "ppd:security",
    "ppd:diagnosticsAndMaintenance",
    "ppd:analyticsAndImprovement",
    "ppd:legalCompliance",
    "ppd:advertisingAndMarketing",
]

# Section 6.4, Action (how)
ACTIONS = ["ppd:collection", "ppd:use", "ppd:transfer", "ppd:inference"]

# Section 6.5, Source (from where)
SOURCES = [
    "ppd:userProvided",
    "ppd:participantObserved",
    "ppd:participantGenerated",
    "ppd:householdProvided",
    "ppd:vendorProvided",
    "ppd:thirdPartyProvided",
    "ppd:derivedFromPriorData",
]

# Section 6.6, Handling Context
HANDLING_CONTEXTS = [
    "ppd:householdContext",
    "ppd:vendorContext",
    "ppd:thirdPartyContext",
    "ppd:publicAudience",
]

# Section 6.7, Dataflow Qualifiers. These are modifiers on an answer, not matrix columns.
RETENTION = ["ppd:ephemeral", "ppd:indefinite"]  # 6.7.1
PROCESSING_BOUNDARY = ["ppd:onDeviceOnly", "ppd:inHomeOnly", "ppd:approvedRemoteProcessing"]  # 6.7.2
# 6.7.2: processing_boundary is defined only for use and inference.
BOUNDARY_ACTIONS = {"ppd:use", "ppd:inference"}

FIELDS = ["data_type", "purpose", "action", "source", "handling_context"]
FIELD_TERMS = {
    "data_type": DATA_TYPES,
    "purpose": PURPOSES,
    "action": ACTIONS,
    "source": SOURCES,
    "handling_context": HANDLING_CONTEXTS,
}


def short(term: str) -> str:
    """``ppd:sensorData`` -> ``sensorData`` (for tables and plots)."""
    return term.split(":", 1)[1]
