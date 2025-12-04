# Alzheimer's Disease Classification

## Business Objective

The primary goal of this project is to analyze health, lifestyle, demographic, medical, and cognitive factors to understand their association with Alzheimer's Disease and to build predictive machine learning models that can identify patients at high risk.

Using the dataset of 2,149 patients (ages 60–90), the objective is to:

- Detect patterns and early indicators related to Alzheimer's onset
- Identify key risk factors contributing to disease progression
- Develop classification models to predict the diagnosis outcome
- Support clinicians and researchers in making data-driven decisions

This analysis will ultimately facilitate early detection, improve patient management strategies, and contribute to healthcare research focused on neurodegenerative diseases.

## Process

Use all the machine learning model steps and fit a suitable model.

## Dataset Variables Description

### Patient Identification

| Variable Name | Description |
|---------------|-------------|
| PatientID | Unique identifier assigned to each patient (ranging from 4751 to 6900) |

### Demographic Details

| Variable Name | Description |
|---------------|-------------|
| Age | Age of the patient (60–90 years) |
| Gender | Gender of the patient (0 = Male, 1 = Female) |
| Ethnicity | Ethnicity category: 0 = Caucasian, 1 = African American, 2 = Asian, 3 = Other |
| EducationLevel | Highest education achieved: 0 = None, 1 = High School, 2 = Bachelor's, 3 = Higher Education |

### Lifestyle Factors

| Variable Name | Description |
|---------------|-------------|
| BMI | Body Mass Index (15–40) |
| Smoking | Smoking status (0 = No, 1 = Yes) |
| AlcoholConsumption | Weekly alcohol intake in units (0–20) |
| PhysicalActivity | Weekly physical activity in hours (0–10) |
| DietQuality | Diet quality score (0–10) |
| SleepQuality | Sleep quality score (4–10) |

### Medical History

| Variable Name | Description |
|---------------|-------------|
| FamilyHistoryAlzheimers | Whether the patient has a family history of Alzheimer's (0 = No, 1 = Yes) |
| CardiovascularDisease | Presence of cardiovascular disease (0 = No, 1 = Yes) |
| Diabetes | Presence of diabetes (0 = No, 1 = Yes) |
| Depression | Presence of depression (0 = No, 1 = Yes) |
| HeadInjury | History of head injury (0 = No, 1 = Yes) |
| Hypertension | Presence of hypertension (0 = No, 1 = Yes) |

### Clinical Measurements

| Variable Name | Description |
|---------------|-------------|
| SystolicBP | Systolic blood pressure (90–180 mmHg) |
| DiastolicBP | Diastolic blood pressure (60–120 mmHg) |
| CholesterolTotal | Total cholesterol level (150–300 mg/dL) |
| CholesterolLDL | LDL cholesterol level (50–200 mg/dL) |
| CholesterolHDL | HDL cholesterol level (20–100 mg/dL) |
| CholesterolTriglycerides | Triglycerides level (50–400 mg/dL) |

### Cognitive & Functional Assessments

| Variable Name | Description |
|---------------|-------------|
| MMSE | Mini-Mental State Examination score (0–30). Lower scores indicate cognitive impairment |
| FunctionalAssessment | Functional ability score (0–10). Lower scores indicate functional decline |
| MemoryComplaints | Whether the patient reports memory issues (0 = No, 1 = Yes) |
| BehavioralProblems | Presence of behavioral issues (0 = No, 1 = Yes) |
| ADL | Activities of Daily Living score (0–10). Lower scores indicate difficulty performing daily tasks |

### Symptoms

| Variable Name | Description |
|---------------|-------------|
| Confusion | Presence of confusion (0 = No, 1 = Yes) |
| Disorientation | Presence of disorientation (0 = No, 1 = Yes) |
| PersonalityChanges | Presence of personality changes (0 = No, 1 = Yes) |
| DifficultyCompletingTasks | Difficulty in completing daily tasks (0 = No, 1 = Yes) |
| Forgetfulness | Presence of forgetfulness (0 = No, 1 = Yes) |

### Diagnosis Information

| Variable Name | Description |
|---------------|-------------|
| Diagnosis | Alzheimer's Disease diagnosis (0 = No, 1 = Yes). This is the target variable |

### Confidential Information

| Variable Name | Description |
|---------------|-------------|
| DoctorInCharge | Confidential field marked "XXXConfid" for all patients |

## Project Timeline

| Milestone | Duration | Task Start - End Date |
|-----------|----------|----------------------|
| Kick off and Business Objective discussion | 1 Day | 02-12-2025 |
| EDA | 1 Week | 09-12-2025 |
| Model Building | 1 Week | 16-12-2025 |
| Deployment | 1 Week | 23-12-2025 |
| Final presentation | 1 Week | 30-12-2025 |

## Protocols

- All participants should adhere to agreed timelines, which will not be extended
- All the documentation – Final presentation and python code to be submitted before the final presentation day
- All the participants must attend review meetings
