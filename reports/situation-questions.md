# Situation questions: review list

All 105 situation questions, as the app shows them. Generated on 2026-11-04 from `export/onboarding.json` (v3.1.0) with the app's own wording code (`shared/onboarding.ts`, `questionText` and `promptFor` in ppd-preference-app), so the text below is exactly what a household reads.

- **37** are in the onboarding decision tree, **31** more are onboarding follow-ups, and **37** are asked only in "Help me refine my settings".
- Every question has the options **No / Not sure / Yes**. Yes writes an allow rule and No a never rule for the situation's 28 flows (4 actions × 7 sources); Not sure keeps the preset.
- **Question** is the sentence from notebook 02's templates (`WHERE_TEXT`, `DATA_TEXT`, `PURPOSE_TEXT`) with its "(for example, …)" parts removed. **Example** is the line under it, for a household that owns none of the devices with their own example. **If they own** lists the example worded for a device they own.
- To review: tick **OK** or write what is wrong under **Notes**. Fixes to the question go in notebook 02 (`WHERE_TEXT`, `DATA_TEXT`, `PURPOSE_TEXT`, `EXAMPLE_BY_CLASS`); fixes to the example line go in the app (`ONE_EXAMPLE`, `PURPOSE_EXAMPLE`, `EXAMPLE_VERB`).

## Sent to the maker (`vendorContext`, 49 questions)

### 1. identifierData × coreFunctionality

`cell_identifierData_coreFunctionality_vendorContext` · Refine only (never asked in onboarding)

> A device sends your account details to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends your name and email address, so you can control it from your phone.*

- [ ] OK
- Notes:

### 2. identifierData × personalization

`cell_identifierData_personalization_vendorContext` · Refine only (never asked in onboarding)

> A device sends your account details to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends your name and email address, to follow your daily routine.*

- [ ] OK
- Notes:

### 3. identifierData × communicationsAndNotifications

`cell_identifierData_communicationsAndNotifications_vendorContext` · Onboarding, follow-up (6 of 57 paths)

> A device sends your account details to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends your name and email address, so it can alert you on your phone.*

- [ ] OK
- Notes:

### 4. identifierData × security

`cell_identifierData_security_vendorContext` · Onboarding, decision tree (question 3 on its path)

> A device sends your account details to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends your name and email address, to spot a break-in.*

- [ ] OK
- Notes:

### 5. identifierData × diagnosticsAndMaintenance

`cell_identifierData_diagnosticsAndMaintenance_vendorContext` · Onboarding, follow-up (6 of 57 paths)

> A device sends your account details to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends your name and email address, to send error reports.*

- [ ] OK
- Notes:

### 6. identifierData × analyticsAndImprovement

`cell_identifierData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (8 of 57 paths)

> A device sends your account details to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends your name and email address, to study how people use the device.*

- [ ] OK
- Notes:

### 7. identifierData × advertisingAndMarketing

`cell_identifierData_advertisingAndMarketing_vendorContext` · Refine only (never asked in onboarding)

> A device sends your account details to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends your name and email address, to show you ads.*

- [ ] OK
- Notes:

### 8. profileData × coreFunctionality

`cell_profileData_coreFunctionality_vendorContext` · Onboarding, decision tree (question 4 on its path)

> A device sends a profile of you to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, so you can control it from your phone.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, so you can control it from your phone.
  - TV: for example, the device sends the kinds of shows you like, so you can control it from your phone.
- [ ] OK
- Notes:

### 9. profileData × personalization

`cell_profileData_personalization_vendorContext` · Onboarding, follow-up (7 of 57 paths)

> A device sends a profile of you to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to follow your daily routine.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to follow your daily routine.
  - TV: for example, the device sends the kinds of shows you like, to follow your daily routine.
- [ ] OK
- Notes:

### 10. profileData × communicationsAndNotifications

`cell_profileData_communicationsAndNotifications_vendorContext` · Onboarding, follow-up (6 of 57 paths)

> A device sends a profile of you to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, so it can alert you on your phone.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, so it can alert you on your phone.
  - TV: for example, the device sends the kinds of shows you like, so it can alert you on your phone.
- [ ] OK
- Notes:

### 11. profileData × security

`cell_profileData_security_vendorContext` · Onboarding, decision tree (question 5 on its path)

> A device sends a profile of you to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to spot a break-in.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to spot a break-in.
  - TV: for example, the device sends the kinds of shows you like, to spot a break-in.
- [ ] OK
- Notes:

### 12. profileData × diagnosticsAndMaintenance

`cell_profileData_diagnosticsAndMaintenance_vendorContext` · Onboarding, decision tree (question 5 on its path)

> A device sends a profile of you to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to send error reports.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to send error reports.
  - TV: for example, the device sends the kinds of shows you like, to send error reports.
- [ ] OK
- Notes:

### 13. profileData × analyticsAndImprovement

`cell_profileData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (7 of 57 paths)

> A device sends a profile of you to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to study how people use the device.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to study how people use the device.
  - TV: for example, the device sends the kinds of shows you like, to study how people use the device.
- [ ] OK
- Notes:

### 14. profileData × advertisingAndMarketing

`cell_profileData_advertisingAndMarketing_vendorContext` · Refine only (never asked in onboarding)

> A device sends a profile of you to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends the daily routine it has learned, to show you ads.*

- If they own a
  - thermostat or sensors: for example, the device sends the heating schedule your thermostat has learned, to show you ads.
  - TV: for example, the device sends the kinds of shows you like, to show you ads.
- [ ] OK
- Notes:

### 15. sensorData × coreFunctionality

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

### 16. sensorData × personalization

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

### 17. sensorData × communicationsAndNotifications

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

### 18. sensorData × security

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

### 19. sensorData × diagnosticsAndMaintenance

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

### 20. sensorData × analyticsAndImprovement

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

### 21. sensorData × advertisingAndMarketing

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

### 22. contentData × coreFunctionality

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

### 23. contentData × personalization

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

### 24. contentData × communicationsAndNotifications

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

### 25. contentData × security

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

### 26. contentData × diagnosticsAndMaintenance

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

### 27. contentData × analyticsAndImprovement

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

### 28. contentData × advertisingAndMarketing

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

### 29. locationData × coreFunctionality

`cell_locationData_coreFunctionality_vendorContext` · Refine only (never asked in onboarding)

> A device sends your location to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends your phone's location, so you can control it from your phone.*

- [ ] OK
- Notes:

### 30. locationData × personalization

`cell_locationData_personalization_vendorContext` · Onboarding, follow-up (11 of 57 paths)

> A device sends your location to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends your phone's location, to follow your daily routine.*

- [ ] OK
- Notes:

### 31. locationData × communicationsAndNotifications

`cell_locationData_communicationsAndNotifications_vendorContext` · Onboarding, decision tree (question 6 on its path)

> A device sends your location to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends your phone's location, so it can alert you on your phone.*

- [ ] OK
- Notes:

### 32. locationData × security

`cell_locationData_security_vendorContext` · Onboarding, decision tree (question 3 on its path)

> A device sends your location to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends your phone's location, to spot a break-in.*

- [ ] OK
- Notes:

### 33. locationData × diagnosticsAndMaintenance

`cell_locationData_diagnosticsAndMaintenance_vendorContext` · Onboarding, follow-up (8 of 57 paths)

> A device sends your location to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends your phone's location, to send error reports.*

- [ ] OK
- Notes:

### 34. locationData × analyticsAndImprovement

`cell_locationData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (10 of 57 paths)

> A device sends your location to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends your phone's location, to study how people use the device.*

- [ ] OK
- Notes:

### 35. locationData × advertisingAndMarketing

`cell_locationData_advertisingAndMarketing_vendorContext` · Refine only (never asked in onboarding)

> A device sends your location to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends your phone's location, to show you ads.*

- [ ] OK
- Notes:

### 36. deviceAndNetworkData × coreFunctionality

`cell_deviceAndNetworkData_coreFunctionality_vendorContext` · Refine only (never asked in onboarding)

> A device sends device and network details to the company that made it, so the device works. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, so you can control it from your phone.*

- [ ] OK
- Notes:

### 37. deviceAndNetworkData × personalization

`cell_deviceAndNetworkData_personalization_vendorContext` · Onboarding, follow-up (10 of 57 paths)

> A device sends device and network details to the company that made it, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to follow your daily routine.*

- [ ] OK
- Notes:

### 38. deviceAndNetworkData × communicationsAndNotifications

`cell_deviceAndNetworkData_communicationsAndNotifications_vendorContext` · Onboarding, follow-up (7 of 57 paths)

> A device sends device and network details to the company that made it, to send you alerts and messages. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, so it can alert you on your phone.*

- [ ] OK
- Notes:

### 39. deviceAndNetworkData × security

`cell_deviceAndNetworkData_security_vendorContext` · Refine only (never asked in onboarding)

> A device sends device and network details to the company that made it, to keep your home and the device secure. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to spot a break-in.*

- [ ] OK
- Notes:

### 40. deviceAndNetworkData × diagnosticsAndMaintenance

`cell_deviceAndNetworkData_diagnosticsAndMaintenance_vendorContext` · Onboarding, follow-up (6 of 57 paths)

> A device sends device and network details to the company that made it, to fix problems and update the device. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to send error reports.*

- [ ] OK
- Notes:

### 41. deviceAndNetworkData × analyticsAndImprovement

`cell_deviceAndNetworkData_analyticsAndImprovement_vendorContext` · Onboarding, follow-up (15 of 57 paths)

> A device sends device and network details to the company that made it, to improve their products. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to study how people use the device.*

- [ ] OK
- Notes:

### 42. deviceAndNetworkData × advertisingAndMarketing

`cell_deviceAndNetworkData_advertisingAndMarketing_vendorContext` · Onboarding, decision tree (question 3 on its path)

> A device sends device and network details to the company that made it, for advertising and marketing. Would you allow this?
>
> *For example, the device sends your Wi-Fi network, to show you ads.*

- [ ] OK
- Notes:

### 43. usageData × coreFunctionality

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

### 44. usageData × personalization

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

### 45. usageData × communicationsAndNotifications

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

### 46. usageData × security

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

### 47. usageData × diagnosticsAndMaintenance

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

### 48. usageData × analyticsAndImprovement

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

### 49. usageData × advertisingAndMarketing

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

## Passed on to other companies (`thirdPartyContext`, 28 questions)

### 50. identifierData × personalization

`cell_identifierData_personalization_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes your account details on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on your name and email address, to follow your daily routine.*

- [ ] OK
- Notes:

### 51. identifierData × diagnosticsAndMaintenance

`cell_identifierData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, decision tree (question 6 on its path)

> A device's maker passes your account details on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on your name and email address, to send error reports.*

- [ ] OK
- Notes:

### 52. identifierData × analyticsAndImprovement

`cell_identifierData_analyticsAndImprovement_thirdPartyContext` · Onboarding, decision tree (question 2 on its path)

> A device's maker passes your account details on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on your name and email address, to study how people use the device.*

- [ ] OK
- Notes:

### 53. identifierData × advertisingAndMarketing

`cell_identifierData_advertisingAndMarketing_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes your account details on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on your name and email address, to show you ads.*

- [ ] OK
- Notes:

### 54. profileData × personalization

`cell_profileData_personalization_thirdPartyContext` · Onboarding, decision tree (question 4 on its path)

> A device's maker passes a profile of you on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on the daily routine it has learned, to follow your daily routine.*

- If they own a
  - thermostat or sensors: for example, the maker passes on the heating schedule your thermostat has learned, to follow your daily routine.
  - TV: for example, the maker passes on the kinds of shows you like, to follow your daily routine.
- [ ] OK
- Notes:

### 55. profileData × diagnosticsAndMaintenance

`cell_profileData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, decision tree (question 4 on its path)

> A device's maker passes a profile of you on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on the daily routine it has learned, to send error reports.*

- If they own a
  - thermostat or sensors: for example, the maker passes on the heating schedule your thermostat has learned, to send error reports.
  - TV: for example, the maker passes on the kinds of shows you like, to send error reports.
- [ ] OK
- Notes:

### 56. profileData × analyticsAndImprovement

`cell_profileData_analyticsAndImprovement_thirdPartyContext` · Onboarding, decision tree (question 5 on its path)

> A device's maker passes a profile of you on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on the daily routine it has learned, to study how people use the device.*

- If they own a
  - thermostat or sensors: for example, the maker passes on the heating schedule your thermostat has learned, to study how people use the device.
  - TV: for example, the maker passes on the kinds of shows you like, to study how people use the device.
- [ ] OK
- Notes:

### 57. profileData × advertisingAndMarketing

`cell_profileData_advertisingAndMarketing_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes a profile of you on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on the daily routine it has learned, to show you ads.*

- If they own a
  - thermostat or sensors: for example, the maker passes on the heating schedule your thermostat has learned, to show you ads.
  - TV: for example, the maker passes on the kinds of shows you like, to show you ads.
- [ ] OK
- Notes:

### 58. sensorData × personalization

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

### 59. sensorData × diagnosticsAndMaintenance

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

### 60. sensorData × analyticsAndImprovement

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

### 61. sensorData × advertisingAndMarketing

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

### 62. contentData × personalization

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

### 63. contentData × diagnosticsAndMaintenance

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

### 64. contentData × analyticsAndImprovement

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

### 65. contentData × advertisingAndMarketing

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

### 66. locationData × personalization

`cell_locationData_personalization_thirdPartyContext` · Onboarding, decision tree (question 5 on its path)

> A device's maker passes your location on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on your phone's location, to follow your daily routine.*

- [ ] OK
- Notes:

### 67. locationData × diagnosticsAndMaintenance

`cell_locationData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, decision tree (question 4 on its path)

> A device's maker passes your location on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on your phone's location, to send error reports.*

- [ ] OK
- Notes:

### 68. locationData × analyticsAndImprovement

`cell_locationData_analyticsAndImprovement_thirdPartyContext` · Onboarding, follow-up (4 of 57 paths)

> A device's maker passes your location on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on your phone's location, to study how people use the device.*

- [ ] OK
- Notes:

### 69. locationData × advertisingAndMarketing

`cell_locationData_advertisingAndMarketing_thirdPartyContext` · Refine only (never asked in onboarding)

> A device's maker passes your location on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on your phone's location, to show you ads.*

- [ ] OK
- Notes:

### 70. deviceAndNetworkData × personalization

`cell_deviceAndNetworkData_personalization_thirdPartyContext` · Onboarding, decision tree (question 5 on its path)

> A device's maker passes device and network details on to other companies, such as advertising or analytics firms, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the maker passes on your Wi-Fi network, to follow your daily routine.*

- [ ] OK
- Notes:

### 71. deviceAndNetworkData × diagnosticsAndMaintenance

`cell_deviceAndNetworkData_diagnosticsAndMaintenance_thirdPartyContext` · Onboarding, follow-up (17 of 57 paths)

> A device's maker passes device and network details on to other companies, such as advertising or analytics firms, to fix problems and update the device. Would you allow this?
>
> *For example, the maker passes on your Wi-Fi network, to send error reports.*

- [ ] OK
- Notes:

### 72. deviceAndNetworkData × analyticsAndImprovement

`cell_deviceAndNetworkData_analyticsAndImprovement_thirdPartyContext` · Onboarding, decision tree (question 4 on its path)

> A device's maker passes device and network details on to other companies, such as advertising or analytics firms, to improve their products. Would you allow this?
>
> *For example, the maker passes on your Wi-Fi network, to study how people use the device.*

- [ ] OK
- Notes:

### 73. deviceAndNetworkData × advertisingAndMarketing

`cell_deviceAndNetworkData_advertisingAndMarketing_thirdPartyContext` · Onboarding, decision tree (question 5 on its path)

> A device's maker passes device and network details on to other companies, such as advertising or analytics firms, for advertising and marketing. Would you allow this?
>
> *For example, the maker passes on your Wi-Fi network, to show you ads.*

- [ ] OK
- Notes:

### 74. usageData × personalization

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

### 75. usageData × diagnosticsAndMaintenance

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

### 76. usageData × analyticsAndImprovement

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

### 77. usageData × advertisingAndMarketing

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

## Stays in the home (`householdContext`, 28 questions)

### 78. identifierData × coreFunctionality

`cell_identifierData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses your account details only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses your name and email address, so you can control it from your phone.*

- [ ] OK
- Notes:

### 79. identifierData × personalization

`cell_identifierData_personalization_householdContext` · Onboarding, decision tree (question 4 on its path)

> A device uses your account details only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses your name and email address, to follow your daily routine.*

- [ ] OK
- Notes:

### 80. identifierData × communicationsAndNotifications

`cell_identifierData_communicationsAndNotifications_householdContext` · Onboarding, decision tree (question 5 on its path)

> A device uses your account details only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses your name and email address, so it can alert you on your phone.*

- [ ] OK
- Notes:

### 81. identifierData × security

`cell_identifierData_security_householdContext` · Refine only (never asked in onboarding)

> A device uses your account details only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses your name and email address, to spot a break-in.*

- [ ] OK
- Notes:

### 82. profileData × coreFunctionality

`cell_profileData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses a profile of you only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses the daily routine it has learned, so you can control it from your phone.*

- If they own a
  - thermostat or sensors: for example, the device uses the heating schedule your thermostat has learned, so you can control it from your phone.
  - TV: for example, the device uses the kinds of shows you like, so you can control it from your phone.
- [ ] OK
- Notes:

### 83. profileData × personalization

`cell_profileData_personalization_householdContext` · Onboarding, follow-up (8 of 57 paths)

> A device uses a profile of you only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses the daily routine it has learned, to follow your daily routine.*

- If they own a
  - thermostat or sensors: for example, the device uses the heating schedule your thermostat has learned, to follow your daily routine.
  - TV: for example, the device uses the kinds of shows you like, to follow your daily routine.
- [ ] OK
- Notes:

### 84. profileData × communicationsAndNotifications

`cell_profileData_communicationsAndNotifications_householdContext` · Onboarding, decision tree (question 6 on its path)

> A device uses a profile of you only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses the daily routine it has learned, so it can alert you on your phone.*

- If they own a
  - thermostat or sensors: for example, the device uses the heating schedule your thermostat has learned, so it can alert you on your phone.
  - TV: for example, the device uses the kinds of shows you like, so it can alert you on your phone.
- [ ] OK
- Notes:

### 85. profileData × security

`cell_profileData_security_householdContext` · Onboarding, decision tree (question 6 on its path)

> A device uses a profile of you only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses the daily routine it has learned, to spot a break-in.*

- If they own a
  - thermostat or sensors: for example, the device uses the heating schedule your thermostat has learned, to spot a break-in.
  - TV: for example, the device uses the kinds of shows you like, to spot a break-in.
- [ ] OK
- Notes:

### 86. sensorData × coreFunctionality

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

### 87. sensorData × personalization

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

### 88. sensorData × communicationsAndNotifications

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

### 89. sensorData × security

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

### 90. contentData × coreFunctionality

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

### 91. contentData × personalization

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

### 92. contentData × communicationsAndNotifications

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

### 93. contentData × security

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

### 94. locationData × coreFunctionality

`cell_locationData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses your location only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses your phone's location, so you can control it from your phone.*

- [ ] OK
- Notes:

### 95. locationData × personalization

`cell_locationData_personalization_householdContext` · Onboarding, decision tree (question 5 on its path)

> A device uses your location only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses your phone's location, to follow your daily routine.*

- [ ] OK
- Notes:

### 96. locationData × communicationsAndNotifications

`cell_locationData_communicationsAndNotifications_householdContext` · Onboarding, follow-up (13 of 57 paths)

> A device uses your location only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses your phone's location, so it can alert you on your phone.*

- [ ] OK
- Notes:

### 97. locationData × security

`cell_locationData_security_householdContext` · Refine only (never asked in onboarding)

> A device uses your location only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses your phone's location, to spot a break-in.*

- [ ] OK
- Notes:

### 98. deviceAndNetworkData × coreFunctionality

`cell_deviceAndNetworkData_coreFunctionality_householdContext` · Refine only (never asked in onboarding)

> A device uses device and network details only inside your home, without it leaving your home, so the device works. Would you allow this?
>
> *For example, the device uses your Wi-Fi network, so you can control it from your phone.*

- [ ] OK
- Notes:

### 99. deviceAndNetworkData × personalization

`cell_deviceAndNetworkData_personalization_householdContext` · Onboarding, decision tree (question 6 on its path)

> A device uses device and network details only inside your home, without it leaving your home, to personalize what the device does or shows you. Would you allow this?
>
> *For example, the device uses your Wi-Fi network, to follow your daily routine.*

- [ ] OK
- Notes:

### 100. deviceAndNetworkData × communicationsAndNotifications

`cell_deviceAndNetworkData_communicationsAndNotifications_householdContext` · Refine only (never asked in onboarding)

> A device uses device and network details only inside your home, without it leaving your home, to send you alerts and messages. Would you allow this?
>
> *For example, the device uses your Wi-Fi network, so it can alert you on your phone.*

- [ ] OK
- Notes:

### 101. deviceAndNetworkData × security

`cell_deviceAndNetworkData_security_householdContext` · Refine only (never asked in onboarding)

> A device uses device and network details only inside your home, without it leaving your home, to keep your home and the device secure. Would you allow this?
>
> *For example, the device uses your Wi-Fi network, to spot a break-in.*

- [ ] OK
- Notes:

### 102. usageData × coreFunctionality

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

### 103. usageData × personalization

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

### 104. usageData × communicationsAndNotifications

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

### 105. usageData × security

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

