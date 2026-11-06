# Onboarding questions: review list

The follow-up questions each onboarding path asks first, then all 105 situation questions as the app shows them. Generated on 2026-11-06 from `export/onboarding.json` (v3.1.0) with the app's own wording code (`shared/onboarding.ts`, `questionText` and `promptFor` in ppd-preference-app), so the text below is exactly what a household reads.

- Of the situation questions, **37** are in the onboarding decision tree, **31** more are onboarding follow-ups, and **37** are asked only in "Help me refine my settings".
- Every question has the options **No / Not sure / Yes**. Yes writes an allow rule and No a never rule for the situation's 28 flows (4 actions × 7 sources); Not sure keeps the preset.
- **Question** is the sentence from notebook 02's templates (`WHERE_TEXT`, `DATA_TEXT`, `PURPOSE_TEXT`) with its "(for example, …)" parts removed. **Example** is the line under it, for a household that owns none of the devices with their own example. **If they own** lists the example worded for a device they own.
- To review: tick **OK** or write what is wrong under **Notes**. Fixes to the question go in notebook 02 (`WHERE_TEXT`, `DATA_TEXT`, `PURPOSE_TEXT`, `EXAMPLE_BY_CLASS`); fixes to the example line go in the app (`ONE_EXAMPLE`, `PURPOSE_EXAMPLE`, `EXAMPLE_VERB`).

## Follow-ups per path (57 paths)

What the app asks in "The details", the second part of onboarding. The decision tree's answers lead to one of 57 paths; each path ends in a preset and then asks its own follow-ups, in this order, until the household has answered 15 questions in all. A follow-up the tree already asked is skipped. Each question links to its entry in the list of 105 below, where its full text and example are.

### Path 1: Strict · no fixing problems or legal duties

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: No or Not sure
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: No or Not sure
- [#95](#q-95) locationData × personalization in the home: No or Not sure
- [#92](#q-92) contentData × communicationsAndNotifications in the home: No or Not sure

Then 9 follow-ups:

1. [#96](#q-96) locationData × communicationsAndNotifications in the home
2. [#43](#q-43) usageData × coreFunctionality to the maker
3. [#80](#q-80) identifierData × communicationsAndNotifications in the home
4. [#38](#q-38) deviceAndNetworkData × communicationsAndNotifications to the maker
5. [#84](#q-84) profileData × communicationsAndNotifications in the home
6. [#40](#q-40) deviceAndNetworkData × diagnosticsAndMaintenance to the maker
7. [#104](#q-104) usageData × communicationsAndNotifications in the home
8. [#8](#q-8) profileData × coreFunctionality to the maker
9. [#99](#q-99) deviceAndNetworkData × personalization in the home

- [ ] OK
- Notes:

### Path 2: Strict · no fixing problems or legal duties

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: No or Not sure
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: No or Not sure
- [#95](#q-95) locationData × personalization in the home: No or Not sure
- [#92](#q-92) contentData × communicationsAndNotifications in the home: Yes

Then 9 follow-ups:

1. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
2. [#8](#q-8) profileData × coreFunctionality to the maker
3. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
4. [#96](#q-96) locationData × communicationsAndNotifications in the home
5. [#80](#q-80) identifierData × communicationsAndNotifications in the home
6. [#43](#q-43) usageData × coreFunctionality to the maker
7. [#84](#q-84) profileData × communicationsAndNotifications in the home
8. [#38](#q-38) deviceAndNetworkData × communicationsAndNotifications to the maker
9. [#40](#q-40) deviceAndNetworkData × diagnosticsAndMaintenance to the maker

- [ ] OK
- Notes:

### Path 3: Strict · no fixing problems or legal duties

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: No or Not sure
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: No or Not sure
- [#95](#q-95) locationData × personalization in the home: Yes
- [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker: No or Not sure

Then 9 follow-ups:

1. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
2. [#8](#q-8) profileData × coreFunctionality to the maker
3. [#96](#q-96) locationData × communicationsAndNotifications in the home
4. [#103](#q-103) usageData × personalization in the home
5. [#92](#q-92) contentData × communicationsAndNotifications in the home
6. [#80](#q-80) identifierData × communicationsAndNotifications in the home
7. [#43](#q-43) usageData × coreFunctionality to the maker
8. [#84](#q-84) profileData × communicationsAndNotifications in the home
9. [#38](#q-38) deviceAndNetworkData × communicationsAndNotifications to the maker

- [ ] OK
- Notes:

### Path 4: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: No or Not sure
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: No or Not sure
- [#95](#q-95) locationData × personalization in the home: Yes
- [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker: Yes

Then 9 follow-ups:

1. [#103](#q-103) usageData × personalization in the home
2. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
3. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
4. [#25](#q-25) contentData × security to the maker
5. [#16](#q-16) sensorData × personalization to the maker
6. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
7. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
8. [#46](#q-46) usageData × security to the maker
9. [#11](#q-11) profileData × security to the maker

- [ ] OK
- Notes:

### Path 5: Strict · no fixing problems or legal duties

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: No or Not sure
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: Yes
- [#95](#q-95) locationData × personalization in the home: No
- [#22](#q-22) contentData × coreFunctionality to the maker: No or Not sure

Then 9 follow-ups:

1. [#8](#q-8) profileData × coreFunctionality to the maker
2. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
3. [#96](#q-96) locationData × communicationsAndNotifications in the home
4. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
5. [#80](#q-80) identifierData × communicationsAndNotifications in the home
6. [#43](#q-43) usageData × coreFunctionality to the maker
7. [#92](#q-92) contentData × communicationsAndNotifications in the home
8. [#84](#q-84) profileData × communicationsAndNotifications in the home
9. [#38](#q-38) deviceAndNetworkData × communicationsAndNotifications to the maker

- [ ] OK
- Notes:

### Path 6: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: No or Not sure
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: Yes
- [#95](#q-95) locationData × personalization in the home: No
- [#22](#q-22) contentData × coreFunctionality to the maker: Yes

Then 9 follow-ups:

1. [#103](#q-103) usageData × personalization in the home
2. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
3. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
4. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
5. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
6. [#8](#q-8) profileData × coreFunctionality to the maker
7. [#25](#q-25) contentData × security to the maker
8. [#16](#q-16) sensorData × personalization to the maker
9. [#60](#q-60) sensorData × analyticsAndImprovement to other companies

- [ ] OK
- Notes:

### Path 7: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: No or Not sure
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: Yes
- [#95](#q-95) locationData × personalization in the home: Not sure or Yes
- [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies: No

Then 9 follow-ups:

1. [#103](#q-103) usageData × personalization in the home
2. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
3. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
4. [#25](#q-25) contentData × security to the maker
5. [#16](#q-16) sensorData × personalization to the maker
6. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
7. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
8. [#46](#q-46) usageData × security to the maker
9. [#11](#q-11) profileData × security to the maker

- [ ] OK
- Notes:

### Path 8: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: No or Not sure
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: Yes
- [#95](#q-95) locationData × personalization in the home: Not sure or Yes
- [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies: Not sure or Yes

Then 9 follow-ups:

1. [#16](#q-16) sensorData × personalization to the maker
2. [#46](#q-46) usageData × security to the maker
3. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
4. [#25](#q-25) contentData × security to the maker
5. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
6. [#11](#q-11) profileData × security to the maker
7. [#37](#q-37) deviceAndNetworkData × personalization to the maker
8. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
9. [#58](#q-58) sensorData × personalization to other companies

- [ ] OK
- Notes:

### Path 9: Strict · no fixing problems or legal duties

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: Yes
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: No
- [#11](#q-11) profileData × security to the maker: No or Not sure
- [#84](#q-84) profileData × communicationsAndNotifications in the home: No or Not sure

Then 9 follow-ups:

1. [#8](#q-8) profileData × coreFunctionality to the maker
2. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
3. [#96](#q-96) locationData × communicationsAndNotifications in the home
4. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
5. [#80](#q-80) identifierData × communicationsAndNotifications in the home
6. [#43](#q-43) usageData × coreFunctionality to the maker
7. [#92](#q-92) contentData × communicationsAndNotifications in the home
8. [#38](#q-38) deviceAndNetworkData × communicationsAndNotifications to the maker
9. [#40](#q-40) deviceAndNetworkData × diagnosticsAndMaintenance to the maker

- [ ] OK
- Notes:

### Path 10: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: Yes
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: No
- [#11](#q-11) profileData × security to the maker: No or Not sure
- [#84](#q-84) profileData × communicationsAndNotifications in the home: Yes

Then 9 follow-ups:

1. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
2. [#103](#q-103) usageData × personalization in the home
3. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
4. [#8](#q-8) profileData × coreFunctionality to the maker
5. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
6. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
7. [#96](#q-96) locationData × communicationsAndNotifications in the home
8. [#16](#q-16) sensorData × personalization to the maker
9. [#25](#q-25) contentData × security to the maker

- [ ] OK
- Notes:

### Path 11: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: Yes
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: No
- [#11](#q-11) profileData × security to the maker: Yes
- [#99](#q-99) deviceAndNetworkData × personalization in the home: No

Then 9 follow-ups:

1. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
2. [#103](#q-103) usageData × personalization in the home
3. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
4. [#8](#q-8) profileData × coreFunctionality to the maker
5. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
6. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
7. [#96](#q-96) locationData × communicationsAndNotifications in the home
8. [#16](#q-16) sensorData × personalization to the maker
9. [#92](#q-92) contentData × communicationsAndNotifications in the home

- [ ] OK
- Notes:

### Path 12: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: Yes
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: No
- [#11](#q-11) profileData × security to the maker: Yes
- [#99](#q-99) deviceAndNetworkData × personalization in the home: Not sure or Yes

Then 9 follow-ups:

1. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
2. [#25](#q-25) contentData × security to the maker
3. [#16](#q-16) sensorData × personalization to the maker
4. [#46](#q-46) usageData × security to the maker
5. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
6. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
7. [#103](#q-103) usageData × personalization in the home
8. [#95](#q-95) locationData × personalization in the home
9. [#37](#q-37) deviceAndNetworkData × personalization to the maker

- [ ] OK
- Notes:

### Path 13: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: Yes
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: Not sure or Yes
- [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies: No
- [#84](#q-84) profileData × communicationsAndNotifications in the home: No

Then 9 follow-ups:

1. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
2. [#103](#q-103) usageData × personalization in the home
3. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
4. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
5. [#8](#q-8) profileData × coreFunctionality to the maker
6. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
7. [#16](#q-16) sensorData × personalization to the maker
8. [#25](#q-25) contentData × security to the maker
9. [#96](#q-96) locationData × communicationsAndNotifications in the home

- [ ] OK
- Notes:

### Path 14: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: Yes
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: Not sure or Yes
- [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies: No
- [#84](#q-84) profileData × communicationsAndNotifications in the home: Not sure or Yes

Then 9 follow-ups:

1. [#16](#q-16) sensorData × personalization to the maker
2. [#46](#q-46) usageData × security to the maker
3. [#25](#q-25) contentData × security to the maker
4. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
5. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
6. [#11](#q-11) profileData × security to the maker
7. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
8. [#95](#q-95) locationData × personalization in the home
9. [#37](#q-37) deviceAndNetworkData × personalization to the maker

- [ ] OK
- Notes:

### Path 15: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: Yes
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: Not sure or Yes
- [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies: Not sure or Yes
- [#31](#q-31) locationData × communicationsAndNotifications to the maker: No or Not sure

Then 9 follow-ups:

1. [#37](#q-37) deviceAndNetworkData × personalization to the maker
2. [#32](#q-32) locationData × security to the maker
3. [#95](#q-95) locationData × personalization in the home
4. [#58](#q-58) sensorData × personalization to other companies
5. [#11](#q-11) profileData × security to the maker
6. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
7. [#83](#q-83) profileData × personalization in the home
8. [#16](#q-16) sensorData × personalization to the maker
9. [#46](#q-46) usageData × security to the maker

- [ ] OK
- Notes:

### Path 16: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#4](#q-4) identifierData × security to the maker: Yes
- [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies: Not sure or Yes
- [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies: Not sure or Yes
- [#31](#q-31) locationData × communicationsAndNotifications to the maker: Yes

Then 9 follow-ups:

1. [#79](#q-79) identifierData × personalization in the home
2. [#33](#q-33) locationData × diagnosticsAndMaintenance to the maker
3. [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker
4. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
5. [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker
6. [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies
7. [#24](#q-24) contentData × communicationsAndNotifications to the maker
8. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
9. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies

- [ ] OK
- Notes:

### Path 17: Strict · no fixing problems or legal duties

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: No
- [#8](#q-8) profileData × coreFunctionality to the maker: No
- [#104](#q-104) usageData × communicationsAndNotifications in the home: No or Not sure
- [#16](#q-16) sensorData × personalization to the maker: No

Then 9 follow-ups:

1. [#96](#q-96) locationData × communicationsAndNotifications in the home
2. [#43](#q-43) usageData × coreFunctionality to the maker
3. [#80](#q-80) identifierData × communicationsAndNotifications in the home
4. [#38](#q-38) deviceAndNetworkData × communicationsAndNotifications to the maker
5. [#92](#q-92) contentData × communicationsAndNotifications in the home
6. [#84](#q-84) profileData × communicationsAndNotifications in the home
7. [#40](#q-40) deviceAndNetworkData × diagnosticsAndMaintenance to the maker
8. [#99](#q-99) deviceAndNetworkData × personalization in the home
9. [#22](#q-22) contentData × coreFunctionality to the maker

- [ ] OK
- Notes:

### Path 18: Strict · no fixing problems or legal duties

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: No
- [#8](#q-8) profileData × coreFunctionality to the maker: No
- [#104](#q-104) usageData × communicationsAndNotifications in the home: No or Not sure
- [#16](#q-16) sensorData × personalization to the maker: Not sure or Yes

Then 9 follow-ups:

1. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
2. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
3. [#96](#q-96) locationData × communicationsAndNotifications in the home
4. [#80](#q-80) identifierData × communicationsAndNotifications in the home
5. [#92](#q-92) contentData × communicationsAndNotifications in the home
6. [#43](#q-43) usageData × coreFunctionality to the maker
7. [#84](#q-84) profileData × communicationsAndNotifications in the home
8. [#38](#q-38) deviceAndNetworkData × communicationsAndNotifications to the maker
9. [#40](#q-40) deviceAndNetworkData × diagnosticsAndMaintenance to the maker

- [ ] OK
- Notes:

### Path 19: Strict · no fixing problems or legal duties

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: No
- [#8](#q-8) profileData × coreFunctionality to the maker: No
- [#104](#q-104) usageData × communicationsAndNotifications in the home: Yes
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: No

Then 9 follow-ups:

1. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
2. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
3. [#96](#q-96) locationData × communicationsAndNotifications in the home
4. [#4](#q-4) identifierData × security to the maker
5. [#92](#q-92) contentData × communicationsAndNotifications in the home
6. [#80](#q-80) identifierData × communicationsAndNotifications in the home
7. [#103](#q-103) usageData × personalization in the home
8. [#43](#q-43) usageData × coreFunctionality to the maker
9. [#84](#q-84) profileData × communicationsAndNotifications in the home

- [ ] OK
- Notes:

### Path 20: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: No
- [#8](#q-8) profileData × coreFunctionality to the maker: No
- [#104](#q-104) usageData × communicationsAndNotifications in the home: Yes
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: Not sure or Yes

Then 9 follow-ups:

1. [#4](#q-4) identifierData × security to the maker
2. [#103](#q-103) usageData × personalization in the home
3. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
4. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
5. [#25](#q-25) contentData × security to the maker
6. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
7. [#16](#q-16) sensorData × personalization to the maker
8. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
9. [#46](#q-46) usageData × security to the maker

- [ ] OK
- Notes:

### Path 21: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: No
- [#8](#q-8) profileData × coreFunctionality to the maker: Not sure or Yes
- [#80](#q-80) identifierData × communicationsAndNotifications in the home: No
- [#25](#q-25) contentData × security to the maker: No or Not sure

Then 9 follow-ups:

1. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
2. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
3. [#4](#q-4) identifierData × security to the maker
4. [#96](#q-96) locationData × communicationsAndNotifications in the home
5. [#103](#q-103) usageData × personalization in the home
6. [#92](#q-92) contentData × communicationsAndNotifications in the home
7. [#43](#q-43) usageData × coreFunctionality to the maker
8. [#84](#q-84) profileData × communicationsAndNotifications in the home
9. [#40](#q-40) deviceAndNetworkData × diagnosticsAndMaintenance to the maker

- [ ] OK
- Notes:

### Path 22: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: No
- [#8](#q-8) profileData × coreFunctionality to the maker: Not sure or Yes
- [#80](#q-80) identifierData × communicationsAndNotifications in the home: No
- [#25](#q-25) contentData × security to the maker: Yes

Then 9 follow-ups:

1. [#103](#q-103) usageData × personalization in the home
2. [#4](#q-4) identifierData × security to the maker
3. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
4. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
5. [#16](#q-16) sensorData × personalization to the maker
6. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
7. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
8. [#46](#q-46) usageData × security to the maker
9. [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies

- [ ] OK
- Notes:

### Path 23: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: No
- [#8](#q-8) profileData × coreFunctionality to the maker: Not sure or Yes
- [#80](#q-80) identifierData × communicationsAndNotifications in the home: Not sure or Yes
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: No

Then 9 follow-ups:

1. [#4](#q-4) identifierData × security to the maker
2. [#103](#q-103) usageData × personalization in the home
3. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
4. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
5. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
6. [#25](#q-25) contentData × security to the maker
7. [#16](#q-16) sensorData × personalization to the maker
8. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
9. [#46](#q-46) usageData × security to the maker

- [ ] OK
- Notes:

### Path 24: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: No
- [#8](#q-8) profileData × coreFunctionality to the maker: Not sure or Yes
- [#80](#q-80) identifierData × communicationsAndNotifications in the home: Not sure or Yes
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: Not sure or Yes

Then 9 follow-ups:

1. [#11](#q-11) profileData × security to the maker
2. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
3. [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies
4. [#37](#q-37) deviceAndNetworkData × personalization to the maker
5. [#95](#q-95) locationData × personalization in the home
6. [#16](#q-16) sensorData × personalization to the maker
7. [#46](#q-46) usageData × security to the maker
8. [#58](#q-58) sensorData × personalization to other companies
9. [#25](#q-25) contentData × security to the maker

- [ ] OK
- Notes:

### Path 25: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: Not sure or Yes
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#79](#q-79) identifierData × personalization in the home: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No

Then 9 follow-ups:

1. [#25](#q-25) contentData × security to the maker
2. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
3. [#16](#q-16) sensorData × personalization to the maker
4. [#46](#q-46) usageData × security to the maker
5. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
6. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
7. [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies
8. [#11](#q-11) profileData × security to the maker
9. [#103](#q-103) usageData × personalization in the home

- [ ] OK
- Notes:

### Path 26: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: Not sure or Yes
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#79](#q-79) identifierData × personalization in the home: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Not sure or Yes

Then 9 follow-ups:

1. [#95](#q-95) locationData × personalization in the home
2. [#37](#q-37) deviceAndNetworkData × personalization to the maker
3. [#58](#q-58) sensorData × personalization to other companies
4. [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies
5. [#11](#q-11) profileData × security to the maker
6. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
7. [#83](#q-83) profileData × personalization in the home
8. [#47](#q-47) usageData × diagnosticsAndMaintenance to the maker
9. [#16](#q-16) sensorData × personalization to the maker

- [ ] OK
- Notes:

### Path 27: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: Not sure or Yes
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#79](#q-79) identifierData × personalization in the home: Yes
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: No

Then 9 follow-ups:

1. [#11](#q-11) profileData × security to the maker
2. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
3. [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies
4. [#37](#q-37) deviceAndNetworkData × personalization to the maker
5. [#95](#q-95) locationData × personalization in the home
6. [#16](#q-16) sensorData × personalization to the maker
7. [#46](#q-46) usageData × security to the maker
8. [#58](#q-58) sensorData × personalization to other companies
9. [#25](#q-25) contentData × security to the maker

- [ ] OK
- Notes:

### Path 28: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: Not sure or Yes
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: No or Not sure
- [#79](#q-79) identifierData × personalization in the home: Yes
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: Not sure or Yes

Then 9 follow-ups:

1. [#5](#q-5) identifierData × diagnosticsAndMaintenance to the maker
2. [#31](#q-31) locationData × communicationsAndNotifications to the maker
3. [#10](#q-10) profileData × communicationsAndNotifications to the maker
4. [#3](#q-3) identifierData × communicationsAndNotifications to the maker
5. [#24](#q-24) contentData × communicationsAndNotifications to the maker
6. [#83](#q-83) profileData × personalization in the home
7. [#47](#q-47) usageData × diagnosticsAndMaintenance to the maker
8. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
9. [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker

- [ ] OK
- Notes:

### Path 29: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: Not sure or Yes
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: Yes
- [#56](#q-56) profileData × analyticsAndImprovement to other companies: No or Not sure
- [#61](#q-61) sensorData × advertisingAndMarketing to other companies: No or Not sure

Then 9 follow-ups:

1. [#3](#q-3) identifierData × communicationsAndNotifications to the maker
2. [#10](#q-10) profileData × communicationsAndNotifications to the maker
3. [#70](#q-70) deviceAndNetworkData × personalization to other companies
4. [#83](#q-83) profileData × personalization in the home
5. [#47](#q-47) usageData × diagnosticsAndMaintenance to the maker
6. [#5](#q-5) identifierData × diagnosticsAndMaintenance to the maker
7. [#31](#q-31) locationData × communicationsAndNotifications to the maker
8. [#58](#q-58) sensorData × personalization to other companies
9. [#24](#q-24) contentData × communicationsAndNotifications to the maker

- [ ] OK
- Notes:

### Path 30: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: Not sure or Yes
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: Yes
- [#56](#q-56) profileData × analyticsAndImprovement to other companies: No or Not sure
- [#61](#q-61) sensorData × advertisingAndMarketing to other companies: Yes

Then 9 follow-ups:

1. [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies
2. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
3. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
4. [#79](#q-79) identifierData × personalization in the home
5. [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies
6. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
7. [#44](#q-44) usageData × personalization to the maker
8. [#33](#q-33) locationData × diagnosticsAndMaintenance to the maker
9. [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker

- [ ] OK
- Notes:

### Path 31: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: Not sure or Yes
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: Yes
- [#56](#q-56) profileData × analyticsAndImprovement to other companies: Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No or Not sure

Then 9 follow-ups:

1. [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies
2. [#79](#q-79) identifierData × personalization in the home
3. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
4. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
5. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
6. [#33](#q-33) locationData × diagnosticsAndMaintenance to the maker
7. [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker
8. [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker
9. [#44](#q-44) usageData × personalization to the maker

- [ ] OK
- Notes:

### Path 32: Relaxed · OK with legal duties and fixing problems

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: No or Not sure
- [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies: Yes
- [#32](#q-32) locationData × security to the maker: Not sure or Yes
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: Yes
- [#56](#q-56) profileData × analyticsAndImprovement to other companies: Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Yes

Then 9 follow-ups:

1. [#34](#q-34) locationData × analyticsAndImprovement to the maker
2. [#61](#q-61) sensorData × advertisingAndMarketing to other companies
3. [#91](#q-91) contentData × personalization in the home
4. [#6](#q-6) identifierData × analyticsAndImprovement to the maker
5. [#30](#q-30) locationData × personalization to the maker
6. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
7. [#52](#q-52) identifierData × analyticsAndImprovement to other companies
8. [#48](#q-48) usageData × analyticsAndImprovement to the maker
9. [#44](#q-44) usageData × personalization to the maker

- [ ] OK
- Notes:

### Path 33: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: No
- [#85](#q-85) profileData × security in the home: No or Not sure

Then 9 follow-ups:

1. [#59](#q-59) sensorData × diagnosticsAndMaintenance to other companies
2. [#4](#q-4) identifierData × security to the maker
3. [#71](#q-71) deviceAndNetworkData × diagnosticsAndMaintenance to other companies
4. [#103](#q-103) usageData × personalization in the home
5. [#19](#q-19) sensorData × diagnosticsAndMaintenance to the maker
6. [#20](#q-20) sensorData × analyticsAndImprovement to the maker
7. [#8](#q-8) profileData × coreFunctionality to the maker
8. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
9. [#96](#q-96) locationData × communicationsAndNotifications in the home

- [ ] OK
- Notes:

### Path 34: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: No
- [#85](#q-85) profileData × security in the home: Yes

Then 9 follow-ups:

1. [#16](#q-16) sensorData × personalization to the maker
2. [#46](#q-46) usageData × security to the maker
3. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
4. [#25](#q-25) contentData × security to the maker
5. [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies
6. [#11](#q-11) profileData × security to the maker
7. [#41](#q-41) deviceAndNetworkData × analyticsAndImprovement to the maker
8. [#95](#q-95) locationData × personalization in the home
9. [#37](#q-37) deviceAndNetworkData × personalization to the maker

- [ ] OK
- Notes:

### Path 35: Strict · no product improvement or personalization · OK with features

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: Not sure or Yes
- [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker: No

Then 9 follow-ups:

1. [#37](#q-37) deviceAndNetworkData × personalization to the maker
2. [#32](#q-32) locationData × security to the maker
3. [#95](#q-95) locationData × personalization in the home
4. [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies
5. [#58](#q-58) sensorData × personalization to other companies
6. [#11](#q-11) profileData × security to the maker
7. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
8. [#83](#q-83) profileData × personalization in the home
9. [#16](#q-16) sensorData × personalization to the maker

- [ ] OK
- Notes:

### Path 36: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No
- [#70](#q-70) deviceAndNetworkData × personalization to other companies: Not sure or Yes
- [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker: Not sure or Yes

Then 9 follow-ups:

1. [#31](#q-31) locationData × communicationsAndNotifications to the maker
2. [#5](#q-5) identifierData × diagnosticsAndMaintenance to the maker
3. [#10](#q-10) profileData × communicationsAndNotifications to the maker
4. [#24](#q-24) contentData × communicationsAndNotifications to the maker
5. [#3](#q-3) identifierData × communicationsAndNotifications to the maker
6. [#83](#q-83) profileData × personalization in the home
7. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
8. [#47](#q-47) usageData × diagnosticsAndMaintenance to the maker
9. [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker

- [ ] OK
- Notes:

### Path 37: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Not sure or Yes
- [#66](#q-66) locationData × personalization to other companies: No or Not sure
- [#64](#q-64) contentData × analyticsAndImprovement to other companies: No or Not sure

Then 9 follow-ups:

1. [#31](#q-31) locationData × communicationsAndNotifications to the maker
2. [#5](#q-5) identifierData × diagnosticsAndMaintenance to the maker
3. [#70](#q-70) deviceAndNetworkData × personalization to other companies
4. [#10](#q-10) profileData × communicationsAndNotifications to the maker
5. [#24](#q-24) contentData × communicationsAndNotifications to the maker
6. [#3](#q-3) identifierData × communicationsAndNotifications to the maker
7. [#83](#q-83) profileData × personalization in the home
8. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
9. [#47](#q-47) usageData × diagnosticsAndMaintenance to the maker

- [ ] OK
- Notes:

### Path 38: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Not sure or Yes
- [#66](#q-66) locationData × personalization to other companies: No or Not sure
- [#64](#q-64) contentData × analyticsAndImprovement to other companies: Yes

Then 9 follow-ups:

1. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
2. [#44](#q-44) usageData × personalization to the maker
3. [#61](#q-61) sensorData × advertisingAndMarketing to other companies
4. [#91](#q-91) contentData × personalization in the home
5. [#6](#q-6) identifierData × analyticsAndImprovement to the maker
6. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
7. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
8. [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies
9. [#34](#q-34) locationData × analyticsAndImprovement to the maker

- [ ] OK
- Notes:

### Path 39: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Not sure or Yes
- [#66](#q-66) locationData × personalization to other companies: Yes
- [#21](#q-21) sensorData × advertisingAndMarketing to the maker: No

Then 9 follow-ups:

1. [#33](#q-33) locationData × diagnosticsAndMaintenance to the maker
2. [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker
3. [#79](#q-79) identifierData × personalization in the home
4. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
5. [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker
6. [#24](#q-24) contentData × communicationsAndNotifications to the maker
7. [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies
8. [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies
9. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies

- [ ] OK
- Notes:

### Path 40: Relaxed · OK with legal duties and fixing problems

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: No or Not sure
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Not sure or Yes
- [#66](#q-66) locationData × personalization to other companies: Yes
- [#21](#q-21) sensorData × advertisingAndMarketing to the maker: Not sure or Yes

Then 9 follow-ups:

1. [#91](#q-91) contentData × personalization in the home
2. [#61](#q-61) sensorData × advertisingAndMarketing to other companies
3. [#6](#q-6) identifierData × analyticsAndImprovement to the maker
4. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
5. [#34](#q-34) locationData × analyticsAndImprovement to the maker
6. [#44](#q-44) usageData × personalization to the maker
7. [#30](#q-30) locationData × personalization to the maker
8. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
9. [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies

- [ ] OK
- Notes:

### Path 41: Careful · no ads · OK with security and device details

Reached by answering (5 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: Yes
- [#61](#q-61) sensorData × advertisingAndMarketing to other companies: No
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: No or Not sure

Then 10 follow-ups:

1. [#79](#q-79) identifierData × personalization in the home
2. [#33](#q-33) locationData × diagnosticsAndMaintenance to the maker
3. [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker
4. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
5. [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies
6. [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker
7. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
8. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
9. [#24](#q-24) contentData × communicationsAndNotifications to the maker
10. [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies

- [ ] OK
- Notes:

### Path 42: Relaxed · OK with legal duties and fixing problems

Reached by answering (5 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: Yes
- [#61](#q-61) sensorData × advertisingAndMarketing to other companies: No
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: Yes

Then 10 follow-ups:

1. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
2. [#91](#q-91) contentData × personalization in the home
3. [#6](#q-6) identifierData × analyticsAndImprovement to the maker
4. [#44](#q-44) usageData × personalization to the maker
5. [#34](#q-34) locationData × analyticsAndImprovement to the maker
6. [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies
7. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
8. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
9. [#30](#q-30) locationData × personalization to the maker
10. [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies

- [ ] OK
- Notes:

### Path 43: Relaxed · OK with legal duties and fixing problems

Reached by answering (5 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: Yes
- [#61](#q-61) sensorData × advertisingAndMarketing to other companies: Not sure or Yes
- [#48](#q-48) usageData × analyticsAndImprovement to the maker: No

Then 10 follow-ups:

1. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
2. [#91](#q-91) contentData × personalization in the home
3. [#6](#q-6) identifierData × analyticsAndImprovement to the maker
4. [#44](#q-44) usageData × personalization to the maker
5. [#34](#q-34) locationData × analyticsAndImprovement to the maker
6. [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies
7. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
8. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
9. [#30](#q-30) locationData × personalization to the maker
10. [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies

- [ ] OK
- Notes:

### Path 44: Relaxed · OK with legal duties and fixing problems

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: Yes
- [#61](#q-61) sensorData × advertisingAndMarketing to other companies: Not sure or Yes
- [#48](#q-48) usageData × analyticsAndImprovement to the maker: Not sure or Yes
- [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies: No or Not sure

Then 9 follow-ups:

1. [#30](#q-30) locationData × personalization to the maker
2. [#34](#q-34) locationData × analyticsAndImprovement to the maker
3. [#13](#q-13) profileData × analyticsAndImprovement to the maker
4. [#9](#q-9) profileData × personalization to the maker
5. [#74](#q-74) usageData × personalization to other companies
6. [#27](#q-27) contentData × analyticsAndImprovement to the maker
7. [#91](#q-91) contentData × personalization in the home
8. [#68](#q-68) locationData × analyticsAndImprovement to other companies
9. [#6](#q-6) identifierData × analyticsAndImprovement to the maker

- [ ] OK
- Notes:

### Path 45: Relaxed · OK with legal duties and fixing problems

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: No
- [#23](#q-23) contentData × personalization to the maker: Yes
- [#61](#q-61) sensorData × advertisingAndMarketing to other companies: Not sure or Yes
- [#48](#q-48) usageData × analyticsAndImprovement to the maker: Not sure or Yes
- [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies: Yes

Then 9 follow-ups:

1. [#68](#q-68) locationData × analyticsAndImprovement to other companies
2. [#74](#q-74) usageData × personalization to other companies
3. [#9](#q-9) profileData × personalization to the maker
4. [#27](#q-27) contentData × analyticsAndImprovement to the maker
5. [#13](#q-13) profileData × analyticsAndImprovement to the maker
6. [#63](#q-63) contentData × diagnosticsAndMaintenance to other companies
7. [#30](#q-30) locationData × personalization to the maker
8. [#56](#q-56) profileData × analyticsAndImprovement to other companies
9. [#66](#q-66) locationData × personalization to other companies

- [ ] OK
- Notes:

### Path 46: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: No
- [#54](#q-54) profileData × personalization to other companies: No
- [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker: No or Not sure
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: No

Then 9 follow-ups:

1. [#72](#q-72) deviceAndNetworkData × analyticsAndImprovement to other companies
2. [#11](#q-11) profileData × security to the maker
3. [#60](#q-60) sensorData × analyticsAndImprovement to other companies
4. [#37](#q-37) deviceAndNetworkData × personalization to the maker
5. [#95](#q-95) locationData × personalization in the home
6. [#32](#q-32) locationData × security to the maker
7. [#58](#q-58) sensorData × personalization to other companies
8. [#16](#q-16) sensorData × personalization to the maker
9. [#46](#q-46) usageData × security to the maker

- [ ] OK
- Notes:

### Path 47: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: No
- [#54](#q-54) profileData × personalization to other companies: No
- [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker: No or Not sure
- [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies: Not sure or Yes

Then 9 follow-ups:

1. [#24](#q-24) contentData × communicationsAndNotifications to the maker
2. [#31](#q-31) locationData × communicationsAndNotifications to the maker
3. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
4. [#5](#q-5) identifierData × diagnosticsAndMaintenance to the maker
5. [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker
6. [#70](#q-70) deviceAndNetworkData × personalization to other companies
7. [#10](#q-10) profileData × communicationsAndNotifications to the maker
8. [#3](#q-3) identifierData × communicationsAndNotifications to the maker
9. [#33](#q-33) locationData × diagnosticsAndMaintenance to the maker

- [ ] OK
- Notes:

### Path 48: Careful · no ads · OK with security and device details

Reached by answering (5 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: No
- [#54](#q-54) profileData × personalization to other companies: No
- [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker: Yes

Then 10 follow-ups:

1. [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies
2. [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies
3. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
4. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
5. [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies
6. [#79](#q-79) identifierData × personalization in the home
7. [#44](#q-44) usageData × personalization to the maker
8. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
9. [#33](#q-33) locationData × diagnosticsAndMaintenance to the maker
10. [#61](#q-61) sensorData × advertisingAndMarketing to other companies

- [ ] OK
- Notes:

### Path 49: Careful · no ads · OK with security and device details

Reached by answering (5 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: No
- [#54](#q-54) profileData × personalization to other companies: Not sure or Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No or Not sure

Then 10 follow-ups:

1. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
2. [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies
3. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
4. [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies
5. [#44](#q-44) usageData × personalization to the maker
6. [#79](#q-79) identifierData × personalization in the home
7. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
8. [#61](#q-61) sensorData × advertisingAndMarketing to other companies
9. [#91](#q-91) contentData × personalization in the home
10. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies

- [ ] OK
- Notes:

### Path 50: Relaxed · OK with legal duties and fixing problems

Reached by answering (5 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: No
- [#54](#q-54) profileData × personalization to other companies: Not sure or Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Yes

Then 10 follow-ups:

1. [#34](#q-34) locationData × analyticsAndImprovement to the maker
2. [#61](#q-61) sensorData × advertisingAndMarketing to other companies
3. [#6](#q-6) identifierData × analyticsAndImprovement to the maker
4. [#91](#q-91) contentData × personalization in the home
5. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
6. [#30](#q-30) locationData × personalization to the maker
7. [#44](#q-44) usageData × personalization to the maker
8. [#48](#q-48) usageData × analyticsAndImprovement to the maker
9. [#13](#q-13) profileData × analyticsAndImprovement to the maker
10. [#9](#q-9) profileData × personalization to the maker

- [ ] OK
- Notes:

### Path 51: Careful · no ads · OK with security and device details

Reached by answering (5 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: Not sure or Yes
- [#79](#q-79) identifierData × personalization in the home: No
- [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker: No

Then 10 follow-ups:

1. [#3](#q-3) identifierData × communicationsAndNotifications to the maker
2. [#10](#q-10) profileData × communicationsAndNotifications to the maker
3. [#70](#q-70) deviceAndNetworkData × personalization to other companies
4. [#5](#q-5) identifierData × diagnosticsAndMaintenance to the maker
5. [#83](#q-83) profileData × personalization in the home
6. [#31](#q-31) locationData × communicationsAndNotifications to the maker
7. [#47](#q-47) usageData × diagnosticsAndMaintenance to the maker
8. [#24](#q-24) contentData × communicationsAndNotifications to the maker
9. [#58](#q-58) sensorData × personalization to other companies
10. [#95](#q-95) locationData × personalization in the home

- [ ] OK
- Notes:

### Path 52: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: Not sure or Yes
- [#79](#q-79) identifierData × personalization in the home: No
- [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker: Not sure or Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No or Not sure

Then 9 follow-ups:

1. [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies
2. [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies
3. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
4. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
5. [#44](#q-44) usageData × personalization to the maker
6. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies
7. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
8. [#33](#q-33) locationData × diagnosticsAndMaintenance to the maker
9. [#61](#q-61) sensorData × advertisingAndMarketing to other companies

- [ ] OK
- Notes:

### Path 53: Relaxed · OK with legal duties and fixing problems

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: Not sure or Yes
- [#79](#q-79) identifierData × personalization in the home: No
- [#12](#q-12) profileData × diagnosticsAndMaintenance to the maker: Not sure or Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Yes

Then 9 follow-ups:

1. [#34](#q-34) locationData × analyticsAndImprovement to the maker
2. [#30](#q-30) locationData × personalization to the maker
3. [#61](#q-61) sensorData × advertisingAndMarketing to other companies
4. [#91](#q-91) contentData × personalization in the home
5. [#6](#q-6) identifierData × analyticsAndImprovement to the maker
6. [#48](#q-48) usageData × analyticsAndImprovement to the maker
7. [#13](#q-13) profileData × analyticsAndImprovement to the maker
8. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
9. [#9](#q-9) profileData × personalization to the maker

- [ ] OK
- Notes:

### Path 54: Careful · no ads · OK with security and device details

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: Not sure or Yes
- [#79](#q-79) identifierData × personalization in the home: Not sure or Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No
- [#23](#q-23) contentData × personalization to the maker: No

Then 9 follow-ups:

1. [#21](#q-21) sensorData × advertisingAndMarketing to the maker
2. [#55](#q-55) profileData × diagnosticsAndMaintenance to other companies
3. [#51](#q-51) identifierData × diagnosticsAndMaintenance to other companies
4. [#73](#q-73) deviceAndNetworkData × advertisingAndMarketing to other companies
5. [#44](#q-44) usageData × personalization to the maker
6. [#26](#q-26) contentData × diagnosticsAndMaintenance to the maker
7. [#61](#q-61) sensorData × advertisingAndMarketing to other companies
8. [#91](#q-91) contentData × personalization in the home
9. [#75](#q-75) usageData × diagnosticsAndMaintenance to other companies

- [ ] OK
- Notes:

### Path 55: Relaxed · OK with legal duties and fixing problems

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: Not sure or Yes
- [#79](#q-79) identifierData × personalization in the home: Not sure or Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: No
- [#23](#q-23) contentData × personalization to the maker: Not sure or Yes

Then 9 follow-ups:

1. [#48](#q-48) usageData × analyticsAndImprovement to the maker
2. [#13](#q-13) profileData × analyticsAndImprovement to the maker
3. [#30](#q-30) locationData × personalization to the maker
4. [#9](#q-9) profileData × personalization to the maker
5. [#27](#q-27) contentData × analyticsAndImprovement to the maker
6. [#74](#q-74) usageData × personalization to other companies
7. [#68](#q-68) locationData × analyticsAndImprovement to other companies
8. [#34](#q-34) locationData × analyticsAndImprovement to the maker
9. [#63](#q-63) contentData × diagnosticsAndMaintenance to other companies

- [ ] OK
- Notes:

### Path 56: Relaxed · OK with legal duties and fixing problems

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: Not sure or Yes
- [#79](#q-79) identifierData × personalization in the home: Not sure or Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Not sure or Yes
- [#64](#q-64) contentData × analyticsAndImprovement to other companies: No

Then 9 follow-ups:

1. [#30](#q-30) locationData × personalization to the maker
2. [#34](#q-34) locationData × analyticsAndImprovement to the maker
3. [#48](#q-48) usageData × analyticsAndImprovement to the maker
4. [#13](#q-13) profileData × analyticsAndImprovement to the maker
5. [#61](#q-61) sensorData × advertisingAndMarketing to other companies
6. [#9](#q-9) profileData × personalization to the maker
7. [#74](#q-74) usageData × personalization to other companies
8. [#27](#q-27) contentData × analyticsAndImprovement to the maker
9. [#91](#q-91) contentData × personalization in the home

- [ ] OK
- Notes:

### Path 57: Relaxed · OK with legal duties and fixing problems

Reached by answering (6 tree questions):

- [#45](#q-45) usageData × communicationsAndNotifications to the maker: Yes
- [#52](#q-52) identifierData × analyticsAndImprovement to other companies: Not sure or Yes
- [#42](#q-42) deviceAndNetworkData × advertisingAndMarketing to the maker: Not sure or Yes
- [#79](#q-79) identifierData × personalization in the home: Not sure or Yes
- [#67](#q-67) locationData × diagnosticsAndMaintenance to other companies: Not sure or Yes
- [#64](#q-64) contentData × analyticsAndImprovement to other companies: Not sure or Yes

Then 9 follow-ups:

1. [#74](#q-74) usageData × personalization to other companies
2. [#68](#q-68) locationData × analyticsAndImprovement to other companies
3. [#9](#q-9) profileData × personalization to the maker
4. [#27](#q-27) contentData × analyticsAndImprovement to the maker
5. [#48](#q-48) usageData × analyticsAndImprovement to the maker
6. [#13](#q-13) profileData × analyticsAndImprovement to the maker
7. [#63](#q-63) contentData × diagnosticsAndMaintenance to other companies
8. [#30](#q-30) locationData × personalization to the maker
9. [#56](#q-56) profileData × analyticsAndImprovement to other companies

- [ ] OK
- Notes:

## The 105 situation questions

### Sent to the maker (`vendorContext`, 49 questions)

<a id="q-1"></a>

#### 1. identifierData × coreFunctionality

`cell_identifierData_coreFunctionality_vendorContext` · Refine only (never asked in onboarding)

> A device sends your account details to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends your name and email address, so you can control it from your phone.*

- [ ] OK
- Notes:

<a id="q-2"></a>

#### 2. identifierData × personalization

`cell_identifierData_personalization_vendorContext` · Refine only (never asked in onboarding)

> A device sends your account details to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends your name and email address, to follow your daily routine.*

- [ ] OK
- Notes:

<a id="q-3"></a>

#### 3. identifierData × communicationsAndNotifications

`cell_identifierData_communicationsAndNotifications_vendorContext` · Onboarding, follow-up (6 of 57 paths)

> A device sends your account details to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends your name and email address, so it can alert you on your phone.*

- [ ] OK
- Notes:

<a id="q-4"></a>

#### 4. identifierData × security

`cell_identifierData_security_vendorContext` · Onboarding, decision tree (question 3 on its path)

> A device sends your account details to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends your name and email address, to spot a break-in.*

- [ ] OK
- Notes:

<a id="q-5"></a>

#### 5. identifierData × diagnosticsAndMaintenance

`cell_identifierData_diagnosticsAndMaintenance_vendorContext` · Onboarding, follow-up (6 of 57 paths)

> A device sends your account details to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends your name and email address, to send error reports.*

- [ ] OK
- Notes:

<a id="q-6"></a>

#### 6. identifierData × analyticsAndImprovement

`cell_identifierData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (8 of 57 paths)

> A device sends your account details to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends your name and email address, to study how people use the device.*

- [ ] OK
- Notes:

<a id="q-7"></a>

#### 7. identifierData × advertisingAndMarketing

`cell_identifierData_advertisingAndMarketing_vendorContext` · Refine only (never asked in onboarding)

> A device sends your account details to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends your name and email address, to show you ads.*

- [ ] OK
- Notes:

<a id="q-8"></a>

#### 8. profileData × coreFunctionality

`cell_profileData_coreFunctionality_vendorContext` · Onboarding, decision tree (question 4 on its path)

> A device sends a profile of you to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, so you can control it from your phone.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, so you can control it from your phone.
  - TV: for example, the device sends the kinds of shows you like, so you can control it from your phone.
- [ ] OK
- Notes:

<a id="q-9"></a>

#### 9. profileData × personalization

`cell_profileData_personalization_vendorContext` · Onboarding, follow-up (7 of 57 paths)

> A device sends a profile of you to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to follow your daily routine.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to follow your daily routine.
  - TV: for example, the device sends the kinds of shows you like, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-10"></a>

#### 10. profileData × communicationsAndNotifications

`cell_profileData_communicationsAndNotifications_vendorContext` · Onboarding, follow-up (6 of 57 paths)

> A device sends a profile of you to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, so it can alert you on your phone.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, so it can alert you on your phone.
  - TV: for example, the device sends the kinds of shows you like, so it can alert you on your phone.
- [ ] OK
- Notes:

<a id="q-11"></a>

#### 11. profileData × security

`cell_profileData_security_vendorContext` · Onboarding, decision tree (question 5 on its path)

> A device sends a profile of you to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to spot a break-in.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to spot a break-in.
  - TV: for example, the device sends the kinds of shows you like, to spot a break-in.
- [ ] OK
- Notes:

<a id="q-12"></a>

#### 12. profileData × diagnosticsAndMaintenance

`cell_profileData_diagnosticsAndMaintenance_vendorContext` · Onboarding, decision tree (question 5 on its path)

> A device sends a profile of you to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to send error reports.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to send error reports.
  - TV: for example, the device sends the kinds of shows you like, to send error reports.
- [ ] OK
- Notes:

<a id="q-13"></a>

#### 13. profileData × analyticsAndImprovement

`cell_profileData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (7 of 57 paths)

> A device sends a profile of you to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to study how people use the device.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to study how people use the device.
  - TV: for example, the device sends the kinds of shows you like, to study how people use the device.
- [ ] OK
- Notes:

<a id="q-14"></a>

#### 14. profileData × advertisingAndMarketing

`cell_profileData_advertisingAndMarketing_vendorContext` · Refine only (never asked in onboarding)

> A device sends a profile of you to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to show you ads.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to show you ads.
  - TV: for example, the device sends the kinds of shows you like, to show you ads.
- [ ] OK
- Notes:

<a id="q-15"></a>

#### 15. sensorData × coreFunctionality

`cell_sensorData_coreFunctionality_vendorContext` · Refine only (never asked in onboarding)

> A device sends sensor readings to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends whether someone is home, so you can control it from your phone.*

- If they own a
  - thermostat or sensors: for example, the device sends your home's temperature and whether someone is home, so you can control it from your phone.
  - camera: for example, the device sends motion your camera detects, so you can control it from your phone.
  - lock or doorbell: for example, the device sends the times your door is opened, so you can control it from your phone.
- [ ] OK
- Notes:

<a id="q-16"></a>

#### 16. sensorData × personalization

`cell_sensorData_personalization_vendorContext` · Onboarding, decision tree (question 6 on its path)

> A device sends sensor readings to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends whether someone is home, to follow your daily routine.*

- If they own a
  - thermostat or sensors: for example, the device sends your home's temperature and whether someone is home, to follow your daily routine.
  - camera: for example, the device sends motion your camera detects, to follow your daily routine.
  - lock or doorbell: for example, the device sends the times your door is opened, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-17"></a>

#### 17. sensorData × communicationsAndNotifications

`cell_sensorData_communicationsAndNotifications_vendorContext` · Refine only (never asked in onboarding)

> A device sends sensor readings to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends whether someone is home, so it can alert you on your phone.*

- If they own a
  - thermostat or sensors: for example, the device sends your home's temperature and whether someone is home, so it can alert you on your phone.
  - camera: for example, the device sends motion your camera detects, so it can alert you on your phone.
  - lock or doorbell: for example, the device sends the times your door is opened, so it can alert you on your phone.
- [ ] OK
- Notes:

<a id="q-18"></a>

#### 18. sensorData × security

`cell_sensorData_security_vendorContext` · Refine only (never asked in onboarding)

> A device sends sensor readings to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends whether someone is home, to spot a break-in.*

- If they own a
  - thermostat or sensors: for example, the device sends your home's temperature and whether someone is home, to spot a break-in.
  - camera: for example, the device sends motion your camera detects, to spot a break-in.
  - lock or doorbell: for example, the device sends the times your door is opened, to spot a break-in.
- [ ] OK
- Notes:

<a id="q-19"></a>

#### 19. sensorData × diagnosticsAndMaintenance

`cell_sensorData_diagnosticsAndMaintenance_vendorContext` · Onboarding, decision tree (question 6 on its path)

> A device sends sensor readings to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends whether someone is home, to send error reports.*

- If they own a
  - thermostat or sensors: for example, the device sends your home's temperature and whether someone is home, to send error reports.
  - camera: for example, the device sends motion your camera detects, to send error reports.
  - lock or doorbell: for example, the device sends the times your door is opened, to send error reports.
- [ ] OK
- Notes:

<a id="q-20"></a>

#### 20. sensorData × analyticsAndImprovement

`cell_sensorData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (14 of 57 paths)

> A device sends sensor readings to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends whether someone is home, to study how people use the device.*

- If they own a
  - thermostat or sensors: for example, the device sends your home's temperature and whether someone is home, to study how people use the device.
  - camera: for example, the device sends motion your camera detects, to study how people use the device.
  - lock or doorbell: for example, the device sends the times your door is opened, to study how people use the device.
- [ ] OK
- Notes:

<a id="q-21"></a>

#### 21. sensorData × advertisingAndMarketing

`cell_sensorData_advertisingAndMarketing_vendorContext` · Onboarding, decision tree (question 6 on its path)

> A device sends sensor readings to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends whether someone is home, to show you ads.*

- If they own a
  - thermostat or sensors: for example, the device sends your home's temperature and whether someone is home, to show you ads.
  - camera: for example, the device sends motion your camera detects, to show you ads.
  - lock or doorbell: for example, the device sends the times your door is opened, to show you ads.
- [ ] OK
- Notes:

<a id="q-22"></a>

#### 22. contentData × coreFunctionality

`cell_contentData_coreFunctionality_vendorContext` · Onboarding, decision tree (question 6 on its path)

> A device sends video or audio to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends a camera's video of your living room, so you can control it from your phone.*

- If they own a
  - camera: for example, the device sends your camera's video of your living room, so you can control it from your phone.
  - voice assistant: for example, the device sends what you say to your voice assistant, so you can control it from your phone.
  - lock or doorbell: for example, the device sends your doorbell's video of your front door, so you can control it from your phone.
- [ ] OK
- Notes:

<a id="q-23"></a>

#### 23. contentData × personalization

`cell_contentData_personalization_vendorContext` · Onboarding, decision tree (question 3 on its path)

> A device sends video or audio to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends a camera's video of your living room, to follow your daily routine.*

- If they own a
  - camera: for example, the device sends your camera's video of your living room, to follow your daily routine.
  - voice assistant: for example, the device sends what you say to your voice assistant, to follow your daily routine.
  - lock or doorbell: for example, the device sends your doorbell's video of your front door, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-24"></a>

#### 24. contentData × communicationsAndNotifications

`cell_contentData_communicationsAndNotifications_vendorContext` · Onboarding, follow-up (9 of 57 paths)

> A device sends video or audio to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends a camera's video of your living room, so it can alert you on your phone.*

- If they own a
  - camera: for example, the device sends your camera's video of your living room, so it can alert you on your phone.
  - voice assistant: for example, the device sends what you say to your voice assistant, so it can alert you on your phone.
  - lock or doorbell: for example, the device sends your doorbell's video of your front door, so it can alert you on your phone.
- [ ] OK
- Notes:

<a id="q-25"></a>

#### 25. contentData × security

`cell_contentData_security_vendorContext` · Onboarding, decision tree (question 6 on its path)

> A device sends video or audio to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends a camera's video of your living room, to spot a break-in.*

- If they own a
  - camera: for example, the device sends your camera's video of your living room, to spot a break-in.
  - voice assistant: for example, the device sends what you say to your voice assistant, to spot a break-in.
  - lock or doorbell: for example, the device sends your doorbell's video of your front door, to spot a break-in.
- [ ] OK
- Notes:

<a id="q-26"></a>

#### 26. contentData × diagnosticsAndMaintenance

`cell_contentData_diagnosticsAndMaintenance_vendorContext` · Onboarding, decision tree (question 5 on its path)

> A device sends video or audio to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends a camera's video of your living room, to send error reports.*

- If they own a
  - camera: for example, the device sends your camera's video of your living room, to send error reports.
  - voice assistant: for example, the device sends what you say to your voice assistant, to send error reports.
  - lock or doorbell: for example, the device sends your doorbell's video of your front door, to send error reports.
- [ ] OK
- Notes:

<a id="q-27"></a>

#### 27. contentData × analyticsAndImprovement

`cell_contentData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (5 of 57 paths)

> A device sends video or audio to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends a camera's video of your living room, to study how people use the device.*

- If they own a
  - camera: for example, the device sends your camera's video of your living room, to study how people use the device.
  - voice assistant: for example, the device sends what you say to your voice assistant, to study how people use the device.
  - lock or doorbell: for example, the device sends your doorbell's video of your front door, to study how people use the device.
- [ ] OK
- Notes:

<a id="q-28"></a>

#### 28. contentData × advertisingAndMarketing

`cell_contentData_advertisingAndMarketing_vendorContext` · Refine only (never asked in onboarding)

> A device sends video or audio to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends a camera's video of your living room, to show you ads.*

- If they own a
  - camera: for example, the device sends your camera's video of your living room, to show you ads.
  - voice assistant: for example, the device sends what you say to your voice assistant, to show you ads.
  - lock or doorbell: for example, the device sends your doorbell's video of your front door, to show you ads.
- [ ] OK
- Notes:

<a id="q-29"></a>

#### 29. locationData × coreFunctionality

`cell_locationData_coreFunctionality_vendorContext` · Refine only (never asked in onboarding)

> A device sends your location to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends your phone's location, so you can control it from your phone.*

- [ ] OK
- Notes:

<a id="q-30"></a>

#### 30. locationData × personalization

`cell_locationData_personalization_vendorContext` · Onboarding, follow-up (11 of 57 paths)

> A device sends your location to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends your phone's location, to follow your daily routine.*

- [ ] OK
- Notes:

<a id="q-31"></a>

#### 31. locationData × communicationsAndNotifications

`cell_locationData_communicationsAndNotifications_vendorContext` · Onboarding, decision tree (question 6 on its path)

> A device sends your location to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends your phone's location, so it can alert you on your phone.*

- [ ] OK
- Notes:

<a id="q-32"></a>

#### 32. locationData × security

`cell_locationData_security_vendorContext` · Onboarding, decision tree (question 3 on its path)

> A device sends your location to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends your phone's location, to spot a break-in.*

- [ ] OK
- Notes:

<a id="q-33"></a>

#### 33. locationData × diagnosticsAndMaintenance

`cell_locationData_diagnosticsAndMaintenance_vendorContext` · Onboarding, follow-up (8 of 57 paths)

> A device sends your location to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends your phone's location, to send error reports.*

- [ ] OK
- Notes:

<a id="q-34"></a>

#### 34. locationData × analyticsAndImprovement

`cell_locationData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (10 of 57 paths)

> A device sends your location to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends your phone's location, to study how people use the device.*

- [ ] OK
- Notes:

<a id="q-35"></a>

#### 35. locationData × advertisingAndMarketing

`cell_locationData_advertisingAndMarketing_vendorContext` · Refine only (never asked in onboarding)

> A device sends your location to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends your phone's location, to show you ads.*

- [ ] OK
- Notes:

<a id="q-36"></a>

#### 36. deviceAndNetworkData × coreFunctionality

`cell_deviceAndNetworkData_coreFunctionality_vendorContext` · Refine only (never asked in onboarding)

> A device sends device and network details to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, so you can control it from your phone.*

- [ ] OK
- Notes:

<a id="q-37"></a>

#### 37. deviceAndNetworkData × personalization

`cell_deviceAndNetworkData_personalization_vendorContext` · Onboarding, follow-up (10 of 57 paths)

> A device sends device and network details to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to follow your daily routine.*

- [ ] OK
- Notes:

<a id="q-38"></a>

#### 38. deviceAndNetworkData × communicationsAndNotifications

`cell_deviceAndNetworkData_communicationsAndNotifications_vendorContext` · Onboarding, follow-up (7 of 57 paths)

> A device sends device and network details to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, so it can alert you on your phone.*

- [ ] OK
- Notes:

<a id="q-39"></a>

#### 39. deviceAndNetworkData × security

`cell_deviceAndNetworkData_security_vendorContext` · Refine only (never asked in onboarding)

> A device sends device and network details to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to spot a break-in.*

- [ ] OK
- Notes:

<a id="q-40"></a>

#### 40. deviceAndNetworkData × diagnosticsAndMaintenance

`cell_deviceAndNetworkData_diagnosticsAndMaintenance_vendorContext` · Onboarding, follow-up (6 of 57 paths)

> A device sends device and network details to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to send error reports.*

- [ ] OK
- Notes:

<a id="q-41"></a>

#### 41. deviceAndNetworkData × analyticsAndImprovement

`cell_deviceAndNetworkData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (15 of 57 paths)

> A device sends device and network details to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to study how people use the device.*

- [ ] OK
- Notes:

<a id="q-42"></a>

#### 42. deviceAndNetworkData × advertisingAndMarketing

`cell_deviceAndNetworkData_advertisingAndMarketing_vendorContext` · Onboarding, decision tree (question 3 on its path)

> A device sends device and network details to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to show you ads.*

- [ ] OK
- Notes:

<a id="q-43"></a>

#### 43. usageData × coreFunctionality

`cell_usageData_coreFunctionality_vendorContext` · Onboarding, follow-up (9 of 57 paths)

> A device sends how you use your devices to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends the times you switch your lights on and off, so you can control it from your phone.*

- If they own a
  - TV: for example, the device sends what you watch on your TV, so you can control it from your phone.
  - thermostat or sensors: for example, the device sends the times you change the temperature, so you can control it from your phone.
  - camera: for example, the device sends the times you check your camera from your phone, so you can control it from your phone.
  - lock or doorbell: for example, the device sends the times you lock and unlock your door, so you can control it from your phone.
- [ ] OK
- Notes:

<a id="q-44"></a>

#### 44. usageData × personalization

`cell_usageData_personalization_vendorContext` · Onboarding, follow-up (12 of 57 paths)

> A device sends how you use your devices to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends the times you switch your lights on and off, to follow your daily routine.*

- If they own a
  - TV: for example, the device sends what you watch on your TV, to follow your daily routine.
  - thermostat or sensors: for example, the device sends the times you change the temperature, to follow your daily routine.
  - camera: for example, the device sends the times you check your camera from your phone, to follow your daily routine.
  - lock or doorbell: for example, the device sends the times you lock and unlock your door, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-45"></a>

#### 45. usageData × communicationsAndNotifications

`cell_usageData_communicationsAndNotifications_vendorContext` · Onboarding, decision tree (question 1 on its path)

> A device sends how you use your devices to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends the times you switch your lights on and off, so it can alert you on your phone.*

- If they own a
  - TV: for example, the device sends what you watch on your TV, so it can alert you on your phone.
  - thermostat or sensors: for example, the device sends the times you change the temperature, so it can alert you on your phone.
  - camera: for example, the device sends the times you check your camera from your phone, so it can alert you on your phone.
  - lock or doorbell: for example, the device sends the times you lock and unlock your door, so it can alert you on your phone.
- [ ] OK
- Notes:

<a id="q-46"></a>

#### 46. usageData × security

`cell_usageData_security_vendorContext` · Onboarding, follow-up (14 of 57 paths)

> A device sends how you use your devices to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends the times you switch your lights on and off, to spot a break-in.*

- If they own a
  - TV: for example, the device sends what you watch on your TV, to spot a break-in.
  - thermostat or sensors: for example, the device sends the times you change the temperature, to spot a break-in.
  - camera: for example, the device sends the times you check your camera from your phone, to spot a break-in.
  - lock or doorbell: for example, the device sends the times you lock and unlock your door, to spot a break-in.
- [ ] OK
- Notes:

<a id="q-47"></a>

#### 47. usageData × diagnosticsAndMaintenance

`cell_usageData_diagnosticsAndMaintenance_vendorContext` · Onboarding, follow-up (6 of 57 paths)

> A device sends how you use your devices to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends the times you switch your lights on and off, to send error reports.*

- If they own a
  - TV: for example, the device sends what you watch on your TV, to send error reports.
  - thermostat or sensors: for example, the device sends the times you change the temperature, to send error reports.
  - camera: for example, the device sends the times you check your camera from your phone, to send error reports.
  - lock or doorbell: for example, the device sends the times you lock and unlock your door, to send error reports.
- [ ] OK
- Notes:

<a id="q-48"></a>

#### 48. usageData × analyticsAndImprovement

`cell_usageData_analyticsAndImprovement_vendorContext` · Onboarding, decision tree (question 5 on its path)

> A device sends how you use your devices to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends the times you switch your lights on and off, to study how people use the device.*

- If they own a
  - TV: for example, the device sends what you watch on your TV, to study how people use the device.
  - thermostat or sensors: for example, the device sends the times you change the temperature, to study how people use the device.
  - camera: for example, the device sends the times you check your camera from your phone, to study how people use the device.
  - lock or doorbell: for example, the device sends the times you lock and unlock your door, to study how people use the device.
- [ ] OK
- Notes:

<a id="q-49"></a>

#### 49. usageData × advertisingAndMarketing

`cell_usageData_advertisingAndMarketing_vendorContext` · Refine only (never asked in onboarding)

> A device sends how you use your devices to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends the times you switch your lights on and off, to show you ads.*

- If they own a
  - TV: for example, the device sends what you watch on your TV, to show you ads.
  - thermostat or sensors: for example, the device sends the times you change the temperature, to show you ads.
  - camera: for example, the device sends the times you check your camera from your phone, to show you ads.
  - lock or doorbell: for example, the device sends the times you lock and unlock your door, to show you ads.
- [ ] OK
- Notes:

### Passed on to other companies (`thirdPartyContext`, 28 questions)

<a id="q-50"></a>

#### 50. identifierData × personalization

`cell_identifierData_personalization_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes your account details on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on your name and email address, to follow your daily routine.*

- [ ] OK
- Notes:

<a id="q-51"></a>

#### 51. identifierData × diagnosticsAndMaintenance

`cell_identifierData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, decision tree (question 6 on its path)

> A device's maker passes your account details on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on your name and email address, to send error reports.*

- [ ] OK
- Notes:

<a id="q-52"></a>

#### 52. identifierData × analyticsAndImprovement

`cell_identifierData_analyticsAndImprovement_thirdPartyContext` · Onboarding, decision tree (question 2 on its path)

> A device's maker passes your account details on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on your name and email address, to study how people use the device.*

- [ ] OK
- Notes:

<a id="q-53"></a>

#### 53. identifierData × advertisingAndMarketing

`cell_identifierData_advertisingAndMarketing_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes your account details on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on your name and email address, to show you ads.*

- [ ] OK
- Notes:

<a id="q-54"></a>

#### 54. profileData × personalization

`cell_profileData_personalization_thirdPartyContext` · Onboarding, decision tree (question 4 on its path)

> A device's maker passes a profile of you on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on the daily routine it has learned, to follow your daily routine.*

- If they own a
  - thermostat or sensors: for example, the maker passes on the heating schedule your thermostat has learned, to follow your daily routine.
  - TV: for example, the maker passes on the kinds of shows you like, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-55"></a>

#### 55. profileData × diagnosticsAndMaintenance

`cell_profileData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, decision tree (question 4 on its path)

> A device's maker passes a profile of you on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on the daily routine it has learned, to send error reports.*

- If they own a
  - thermostat or sensors: for example, the maker passes on the heating schedule your thermostat has learned, to send error reports.
  - TV: for example, the maker passes on the kinds of shows you like, to send error reports.
- [ ] OK
- Notes:

<a id="q-56"></a>

#### 56. profileData × analyticsAndImprovement

`cell_profileData_analyticsAndImprovement_thirdPartyContext` · Onboarding, decision tree (question 5 on its path)

> A device's maker passes a profile of you on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on the daily routine it has learned, to study how people use the device.*

- If they own a
  - thermostat or sensors: for example, the maker passes on the heating schedule your thermostat has learned, to study how people use the device.
  - TV: for example, the maker passes on the kinds of shows you like, to study how people use the device.
- [ ] OK
- Notes:

<a id="q-57"></a>

#### 57. profileData × advertisingAndMarketing

`cell_profileData_advertisingAndMarketing_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes a profile of you on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on the daily routine it has learned, to show you ads.*

- If they own a
  - thermostat or sensors: for example, the maker passes on the heating schedule your thermostat has learned, to show you ads.
  - TV: for example, the maker passes on the kinds of shows you like, to show you ads.
- [ ] OK
- Notes:

<a id="q-58"></a>

#### 58. sensorData × personalization

`cell_sensorData_personalization_thirdPartyContext` · Onboarding, follow-up (9 of 57 paths)

> A device's maker passes sensor readings on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on whether someone is home, to follow your daily routine.*

- If they own a
  - thermostat or sensors: for example, the maker passes on your home's temperature and whether someone is home, to follow your daily routine.
  - camera: for example, the maker passes on motion your camera detects, to follow your daily routine.
  - lock or doorbell: for example, the maker passes on the times your door is opened, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-59"></a>

#### 59. sensorData × diagnosticsAndMaintenance

`cell_sensorData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, decision tree (question 2 on its path)

> A device's maker passes sensor readings on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on whether someone is home, to send error reports.*

- If they own a
  - thermostat or sensors: for example, the maker passes on your home's temperature and whether someone is home, to send error reports.
  - camera: for example, the maker passes on motion your camera detects, to send error reports.
  - lock or doorbell: for example, the maker passes on the times your door is opened, to send error reports.
- [ ] OK
- Notes:

<a id="q-60"></a>

#### 60. sensorData × analyticsAndImprovement

`cell_sensorData_analyticsAndImprovement_thirdPartyContext` · Onboarding, follow-up (17 of 57 paths)

> A device's maker passes sensor readings on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on whether someone is home, to study how people use the device.*

- If they own a
  - thermostat or sensors: for example, the maker passes on your home's temperature and whether someone is home, to study how people use the device.
  - camera: for example, the maker passes on motion your camera detects, to study how people use the device.
  - lock or doorbell: for example, the maker passes on the times your door is opened, to study how people use the device.
- [ ] OK
- Notes:

<a id="q-61"></a>

#### 61. sensorData × advertisingAndMarketing

`cell_sensorData_advertisingAndMarketing_thirdPartyContext` · Onboarding, decision tree (question 4 on its path)

> A device's maker passes sensor readings on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on whether someone is home, to show you ads.*

- If they own a
  - thermostat or sensors: for example, the maker passes on your home's temperature and whether someone is home, to show you ads.
  - camera: for example, the maker passes on motion your camera detects, to show you ads.
  - lock or doorbell: for example, the maker passes on the times your door is opened, to show you ads.
- [ ] OK
- Notes:

<a id="q-62"></a>

#### 62. contentData × personalization

`cell_contentData_personalization_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes video or audio on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on a camera's video of your living room, to follow your daily routine.*

- If they own a
  - camera: for example, the maker passes on your camera's video of your living room, to follow your daily routine.
  - voice assistant: for example, the maker passes on what you say to your voice assistant, to follow your daily routine.
  - lock or doorbell: for example, the maker passes on your doorbell's video of your front door, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-63"></a>

#### 63. contentData × diagnosticsAndMaintenance

`cell_contentData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, follow-up (3 of 57 paths)

> A device's maker passes video or audio on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on a camera's video of your living room, to send error reports.*

- If they own a
  - camera: for example, the maker passes on your camera's video of your living room, to send error reports.
  - voice assistant: for example, the maker passes on what you say to your voice assistant, to send error reports.
  - lock or doorbell: for example, the maker passes on your doorbell's video of your front door, to send error reports.
- [ ] OK
- Notes:

<a id="q-64"></a>

#### 64. contentData × analyticsAndImprovement

`cell_contentData_analyticsAndImprovement_thirdPartyContext` · Onboarding, decision tree (question 6 on its path)

> A device's maker passes video or audio on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on a camera's video of your living room, to study how people use the device.*

- If they own a
  - camera: for example, the maker passes on your camera's video of your living room, to study how people use the device.
  - voice assistant: for example, the maker passes on what you say to your voice assistant, to study how people use the device.
  - lock or doorbell: for example, the maker passes on your doorbell's video of your front door, to study how people use the device.
- [ ] OK
- Notes:

<a id="q-65"></a>

#### 65. contentData × advertisingAndMarketing

`cell_contentData_advertisingAndMarketing_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes video or audio on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on a camera's video of your living room, to show you ads.*

- If they own a
  - camera: for example, the maker passes on your camera's video of your living room, to show you ads.
  - voice assistant: for example, the maker passes on what you say to your voice assistant, to show you ads.
  - lock or doorbell: for example, the maker passes on your doorbell's video of your front door, to show you ads.
- [ ] OK
- Notes:

<a id="q-66"></a>

#### 66. locationData × personalization

`cell_locationData_personalization_thirdPartyContext` · Onboarding, decision tree (question 5 on its path)

> A device's maker passes your location on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on your phone's location, to follow your daily routine.*

- [ ] OK
- Notes:

<a id="q-67"></a>

#### 67. locationData × diagnosticsAndMaintenance

`cell_locationData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, decision tree (question 4 on its path)

> A device's maker passes your location on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on your phone's location, to send error reports.*

- [ ] OK
- Notes:

<a id="q-68"></a>

#### 68. locationData × analyticsAndImprovement

`cell_locationData_analyticsAndImprovement_thirdPartyContext` · Onboarding, follow-up (4 of 57 paths)

> A device's maker passes your location on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on your phone's location, to study how people use the device.*

- [ ] OK
- Notes:

<a id="q-69"></a>

#### 69. locationData × advertisingAndMarketing

`cell_locationData_advertisingAndMarketing_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes your location on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on your phone's location, to show you ads.*

- [ ] OK
- Notes:

<a id="q-70"></a>

#### 70. deviceAndNetworkData × personalization

`cell_deviceAndNetworkData_personalization_thirdPartyContext` · Onboarding, decision tree (question 5 on its path)

> A device's maker passes device and network details on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on your Wi-Fi network, to follow your daily routine.*

- [ ] OK
- Notes:

<a id="q-71"></a>

#### 71. deviceAndNetworkData × diagnosticsAndMaintenance

`cell_deviceAndNetworkData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, follow-up (17 of 57 paths)

> A device's maker passes device and network details on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on your Wi-Fi network, to send error reports.*

- [ ] OK
- Notes:

<a id="q-72"></a>

#### 72. deviceAndNetworkData × analyticsAndImprovement

`cell_deviceAndNetworkData_analyticsAndImprovement_thirdPartyContext` · Onboarding, decision tree (question 4 on its path)

> A device's maker passes device and network details on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on your Wi-Fi network, to study how people use the device.*

- [ ] OK
- Notes:

<a id="q-73"></a>

#### 73. deviceAndNetworkData × advertisingAndMarketing

`cell_deviceAndNetworkData_advertisingAndMarketing_thirdPartyContext` · Onboarding, decision tree (question 5 on its path)

> A device's maker passes device and network details on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on your Wi-Fi network, to show you ads.*

- [ ] OK
- Notes:

<a id="q-74"></a>

#### 74. usageData × personalization

`cell_usageData_personalization_thirdPartyContext` · Onboarding, follow-up (5 of 57 paths)

> A device's maker passes how you use your devices on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on the times you switch your lights on and off, to follow your daily routine.*

- If they own a
  - TV: for example, the maker passes on what you watch on your TV, to follow your daily routine.
  - thermostat or sensors: for example, the maker passes on the times you change the temperature, to follow your daily routine.
  - camera: for example, the maker passes on the times you check your camera from your phone, to follow your daily routine.
  - lock or doorbell: for example, the maker passes on the times you lock and unlock your door, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-75"></a>

#### 75. usageData × diagnosticsAndMaintenance

`cell_usageData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, follow-up (13 of 57 paths)

> A device's maker passes how you use your devices on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on the times you switch your lights on and off, to send error reports.*

- If they own a
  - TV: for example, the maker passes on what you watch on your TV, to send error reports.
  - thermostat or sensors: for example, the maker passes on the times you change the temperature, to send error reports.
  - camera: for example, the maker passes on the times you check your camera from your phone, to send error reports.
  - lock or doorbell: for example, the maker passes on the times you lock and unlock your door, to send error reports.
- [ ] OK
- Notes:

<a id="q-76"></a>

#### 76. usageData × analyticsAndImprovement

`cell_usageData_analyticsAndImprovement_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes how you use your devices on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on the times you switch your lights on and off, to study how people use the device.*

- If they own a
  - TV: for example, the maker passes on what you watch on your TV, to study how people use the device.
  - thermostat or sensors: for example, the maker passes on the times you change the temperature, to study how people use the device.
  - camera: for example, the maker passes on the times you check your camera from your phone, to study how people use the device.
  - lock or doorbell: for example, the maker passes on the times you lock and unlock your door, to study how people use the device.
- [ ] OK
- Notes:

<a id="q-77"></a>

#### 77. usageData × advertisingAndMarketing

`cell_usageData_advertisingAndMarketing_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes how you use your devices on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on the times you switch your lights on and off, to show you ads.*

- If they own a
  - TV: for example, the maker passes on what you watch on your TV, to show you ads.
  - thermostat or sensors: for example, the maker passes on the times you change the temperature, to show you ads.
  - camera: for example, the maker passes on the times you check your camera from your phone, to show you ads.
  - lock or doorbell: for example, the maker passes on the times you lock and unlock your door, to show you ads.
- [ ] OK
- Notes:

### Stays in the home (`householdContext`, 28 questions)

<a id="q-78"></a>

#### 78. identifierData × coreFunctionality

`cell_identifierData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses your account details only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses your name and email address, so you can control it from your phone.*

- [ ] OK
- Notes:

<a id="q-79"></a>

#### 79. identifierData × personalization

`cell_identifierData_personalization_householdContext` · Onboarding, decision tree (question 4 on its path)

> A device uses your account details only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses your name and email address, to follow your daily routine.*

- [ ] OK
- Notes:

<a id="q-80"></a>

#### 80. identifierData × communicationsAndNotifications

`cell_identifierData_communicationsAndNotifications_householdContext` · Onboarding, decision tree (question 5 on its path)

> A device uses your account details only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses your name and email address, so it can alert you on your phone.*

- [ ] OK
- Notes:

<a id="q-81"></a>

#### 81. identifierData × security

`cell_identifierData_security_householdContext` · Refine only (never asked in onboarding)

> A device uses your account details only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses your name and email address, to spot a break-in.*

- [ ] OK
- Notes:

<a id="q-82"></a>

#### 82. profileData × coreFunctionality

`cell_profileData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses a profile of you only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses the daily routine it has learned, so you can control it from your phone.*

- If they own a
  - thermostat or sensors: for example, the device uses the heating schedule your thermostat has learned, so you can control it from your phone.
  - TV: for example, the device uses the kinds of shows you like, so you can control it from your phone.
- [ ] OK
- Notes:

<a id="q-83"></a>

#### 83. profileData × personalization

`cell_profileData_personalization_householdContext` · Onboarding, follow-up (8 of 57 paths)

> A device uses a profile of you only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses the daily routine it has learned, to follow your daily routine.*

- If they own a
  - thermostat or sensors: for example, the device uses the heating schedule your thermostat has learned, to follow your daily routine.
  - TV: for example, the device uses the kinds of shows you like, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-84"></a>

#### 84. profileData × communicationsAndNotifications

`cell_profileData_communicationsAndNotifications_householdContext` · Onboarding, decision tree (question 6 on its path)

> A device uses a profile of you only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses the daily routine it has learned, so it can alert you on your phone.*

- If they own a
  - thermostat or sensors: for example, the device uses the heating schedule your thermostat has learned, so it can alert you on your phone.
  - TV: for example, the device uses the kinds of shows you like, so it can alert you on your phone.
- [ ] OK
- Notes:

<a id="q-85"></a>

#### 85. profileData × security

`cell_profileData_security_householdContext` · Onboarding, decision tree (question 6 on its path)

> A device uses a profile of you only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses the daily routine it has learned, to spot a break-in.*

- If they own a
  - thermostat or sensors: for example, the device uses the heating schedule your thermostat has learned, to spot a break-in.
  - TV: for example, the device uses the kinds of shows you like, to spot a break-in.
- [ ] OK
- Notes:

<a id="q-86"></a>

#### 86. sensorData × coreFunctionality

`cell_sensorData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses sensor readings only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses whether someone is home, so you can control it from your phone.*

- If they own a
  - thermostat or sensors: for example, the device uses your home's temperature and whether someone is home, so you can control it from your phone.
  - camera: for example, the device uses motion your camera detects, so you can control it from your phone.
  - lock or doorbell: for example, the device uses the times your door is opened, so you can control it from your phone.
- [ ] OK
- Notes:

<a id="q-87"></a>

#### 87. sensorData × personalization

`cell_sensorData_personalization_householdContext` · Refine only (never asked in onboarding)

> A device uses sensor readings only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses whether someone is home, to follow your daily routine.*

- If they own a
  - thermostat or sensors: for example, the device uses your home's temperature and whether someone is home, to follow your daily routine.
  - camera: for example, the device uses motion your camera detects, to follow your daily routine.
  - lock or doorbell: for example, the device uses the times your door is opened, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-88"></a>

#### 88. sensorData × communicationsAndNotifications

`cell_sensorData_communicationsAndNotifications_householdContext` · Refine only (never asked in onboarding)

> A device uses sensor readings only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses whether someone is home, so it can alert you on your phone.*

- If they own a
  - thermostat or sensors: for example, the device uses your home's temperature and whether someone is home, so it can alert you on your phone.
  - camera: for example, the device uses motion your camera detects, so it can alert you on your phone.
  - lock or doorbell: for example, the device uses the times your door is opened, so it can alert you on your phone.
- [ ] OK
- Notes:

<a id="q-89"></a>

#### 89. sensorData × security

`cell_sensorData_security_householdContext` · Refine only (never asked in onboarding)

> A device uses sensor readings only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses whether someone is home, to spot a break-in.*

- If they own a
  - thermostat or sensors: for example, the device uses your home's temperature and whether someone is home, to spot a break-in.
  - camera: for example, the device uses motion your camera detects, to spot a break-in.
  - lock or doorbell: for example, the device uses the times your door is opened, to spot a break-in.
- [ ] OK
- Notes:

<a id="q-90"></a>

#### 90. contentData × coreFunctionality

`cell_contentData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses video or audio only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses a camera's video of your living room, so you can control it from your phone.*

- If they own a
  - camera: for example, the device uses your camera's video of your living room, so you can control it from your phone.
  - voice assistant: for example, the device uses what you say to your voice assistant, so you can control it from your phone.
  - lock or doorbell: for example, the device uses your doorbell's video of your front door, so you can control it from your phone.
- [ ] OK
- Notes:

<a id="q-91"></a>

#### 91. contentData × personalization

`cell_contentData_personalization_householdContext` · Onboarding, follow-up (11 of 57 paths)

> A device uses video or audio only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses a camera's video of your living room, to follow your daily routine.*

- If they own a
  - camera: for example, the device uses your camera's video of your living room, to follow your daily routine.
  - voice assistant: for example, the device uses what you say to your voice assistant, to follow your daily routine.
  - lock or doorbell: for example, the device uses your doorbell's video of your front door, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-92"></a>

#### 92. contentData × communicationsAndNotifications

`cell_contentData_communicationsAndNotifications_householdContext` · Onboarding, decision tree (question 6 on its path)

> A device uses video or audio only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses a camera's video of your living room, so it can alert you on your phone.*

- If they own a
  - camera: for example, the device uses your camera's video of your living room, so it can alert you on your phone.
  - voice assistant: for example, the device uses what you say to your voice assistant, so it can alert you on your phone.
  - lock or doorbell: for example, the device uses your doorbell's video of your front door, so it can alert you on your phone.
- [ ] OK
- Notes:

<a id="q-93"></a>

#### 93. contentData × security

`cell_contentData_security_householdContext` · Refine only (never asked in onboarding)

> A device uses video or audio only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses a camera's video of your living room, to spot a break-in.*

- If they own a
  - camera: for example, the device uses your camera's video of your living room, to spot a break-in.
  - voice assistant: for example, the device uses what you say to your voice assistant, to spot a break-in.
  - lock or doorbell: for example, the device uses your doorbell's video of your front door, to spot a break-in.
- [ ] OK
- Notes:

<a id="q-94"></a>

#### 94. locationData × coreFunctionality

`cell_locationData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses your location only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses your phone's location, so you can control it from your phone.*

- [ ] OK
- Notes:

<a id="q-95"></a>

#### 95. locationData × personalization

`cell_locationData_personalization_householdContext` · Onboarding, decision tree (question 5 on its path)

> A device uses your location only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses your phone's location, to follow your daily routine.*

- [ ] OK
- Notes:

<a id="q-96"></a>

#### 96. locationData × communicationsAndNotifications

`cell_locationData_communicationsAndNotifications_householdContext` · Onboarding, follow-up (13 of 57 paths)

> A device uses your location only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses your phone's location, so it can alert you on your phone.*

- [ ] OK
- Notes:

<a id="q-97"></a>

#### 97. locationData × security

`cell_locationData_security_householdContext` · Refine only (never asked in onboarding)

> A device uses your location only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses your phone's location, to spot a break-in.*

- [ ] OK
- Notes:

<a id="q-98"></a>

#### 98. deviceAndNetworkData × coreFunctionality

`cell_deviceAndNetworkData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses device and network details only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses your Wi-Fi network, so you can control it from your phone.*

- [ ] OK
- Notes:

<a id="q-99"></a>

#### 99. deviceAndNetworkData × personalization

`cell_deviceAndNetworkData_personalization_householdContext` · Onboarding, decision tree (question 6 on its path)

> A device uses device and network details only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses your Wi-Fi network, to follow your daily routine.*

- [ ] OK
- Notes:

<a id="q-100"></a>

#### 100. deviceAndNetworkData × communicationsAndNotifications

`cell_deviceAndNetworkData_communicationsAndNotifications_householdContext` · Refine only (never asked in onboarding)

> A device uses device and network details only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses your Wi-Fi network, so it can alert you on your phone.*

- [ ] OK
- Notes:

<a id="q-101"></a>

#### 101. deviceAndNetworkData × security

`cell_deviceAndNetworkData_security_householdContext` · Refine only (never asked in onboarding)

> A device uses device and network details only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses your Wi-Fi network, to spot a break-in.*

- [ ] OK
- Notes:

<a id="q-102"></a>

#### 102. usageData × coreFunctionality

`cell_usageData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses how you use your devices only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses the times you switch your lights on and off, so you can control it from your phone.*

- If they own a
  - TV: for example, the device uses what you watch on your TV, so you can control it from your phone.
  - thermostat or sensors: for example, the device uses the times you change the temperature, so you can control it from your phone.
  - camera: for example, the device uses the times you check your camera from your phone, so you can control it from your phone.
  - lock or doorbell: for example, the device uses the times you lock and unlock your door, so you can control it from your phone.
- [ ] OK
- Notes:

<a id="q-103"></a>

#### 103. usageData × personalization

`cell_usageData_personalization_householdContext` · Onboarding, follow-up (15 of 57 paths)

> A device uses how you use your devices only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses the times you switch your lights on and off, to follow your daily routine.*

- If they own a
  - TV: for example, the device uses what you watch on your TV, to follow your daily routine.
  - thermostat or sensors: for example, the device uses the times you change the temperature, to follow your daily routine.
  - camera: for example, the device uses the times you check your camera from your phone, to follow your daily routine.
  - lock or doorbell: for example, the device uses the times you lock and unlock your door, to follow your daily routine.
- [ ] OK
- Notes:

<a id="q-104"></a>

#### 104. usageData × communicationsAndNotifications

`cell_usageData_communicationsAndNotifications_householdContext` · Onboarding, decision tree (question 5 on its path)

> A device uses how you use your devices only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses the times you switch your lights on and off, so it can alert you on your phone.*

- If they own a
  - TV: for example, the device uses what you watch on your TV, so it can alert you on your phone.
  - thermostat or sensors: for example, the device uses the times you change the temperature, so it can alert you on your phone.
  - camera: for example, the device uses the times you check your camera from your phone, so it can alert you on your phone.
  - lock or doorbell: for example, the device uses the times you lock and unlock your door, so it can alert you on your phone.
- [ ] OK
- Notes:

<a id="q-105"></a>

#### 105. usageData × security

`cell_usageData_security_householdContext` · Refine only (never asked in onboarding)

> A device uses how you use your devices only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses the times you switch your lights on and off, to spot a break-in.*

- If they own a
  - TV: for example, the device uses what you watch on your TV, to spot a break-in.
  - thermostat or sensors: for example, the device uses the times you change the temperature, to spot a break-in.
  - camera: for example, the device uses the times you check your camera from your phone, to spot a break-in.
  - lock or doorbell: for example, the device uses the times you lock and unlock your door, to spot a break-in.
- [ ] OK
- Notes:

