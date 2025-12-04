import streamlit as st
import pandas as pd
import numpy as np
import elements.progressbar as pb

st.sidebar.title("Alzheimer's Disease Classification")
st.sidebar.markdown("This application classifies Alzheimer's disease stages using machine learning models.")

# Define pages
main_page = st.Page("app.py", title="Main Page", icon="🎈")
about = st.Page("./Pages/about.py", title="About", icon="❄️")
pg = st.navigation([main_page, about])

st.write("# Alzheimer's Disease Classification Application")

# ---- State ----
if "step" not in st.session_state:
    st.session_state.step = 0  # start at first section

if "inputs" not in st.session_state:
    st.session_state.inputs = {}   # to store all features (except PI)

if "show_output" not in st.session_state:
    st.session_state.show_output = False

SECTION_TITLES = ["Patient Identification", "Demographic Details", "Lifestyle Factors", "Medical History", "Clinical Measurements", "Cognitive & Functional Assessments", "Symptoms"]

total_steps = len(SECTION_TITLES)

# dummy init; will be overwritten in output()
X = pd.DataFrame()


def next_step():
    if st.session_state.step < total_steps - 1:
        st.session_state.step += 1


def prev_step():
    if st.session_state.step > 0:
        st.session_state.step -= 1


# when user clicks Submit on last step
def submit():
    st.session_state.show_output = True


def nav_buttons():
    step = st.session_state.step
    col1, col2 = st.columns(2)

    with col1:
        st.button("⬅ Back",use_container_width=True,disabled=(step == 0),on_click=prev_step,)

    with col2:
        if step < total_steps - 1:
            st.button("Next ➜",use_container_width=True,on_click=next_step,)
        else:
            st.button("Submit ✔",use_container_width=True,on_click=submit,)


# ----------------- STEPS ----------------- #
def pi():
    st.write("### Patient Identification")
    patient_id = np.random.randint(4715, 6900)
    st.write(f"**Patient ID:** {patient_id}")
    p_name = st.text_input("Enter Patient Name")

    if p_name.strip() == "":
        st.warning("Please enter a valid patient name.")

    # We intentionally DO NOT store these into st.session_state.inputs
    # so they are excluded from X

    nav_buttons()


def dd():
    st.write("### Demographic Details")
    age = st.number_input("Enter Age", min_value=1, max_value=120)

    genders = {"Male": 0, "Female": 1}
    gl = st.selectbox("Select Gender", options=list(genders.keys()))
    gender = genders[gl]

    ethnicities = {"Caucasian": 0, "African American": 1, "Asian": 2, "Other": 3}
    el = st.selectbox("Select Ethnicity", options=list(ethnicities.keys()))
    ethnicity = ethnicities[el]

    educations = {None: 0, "High School": 1, "Bachelor's": 2, "Higher Education": 3}
    edl = st.selectbox("Select Education Level", options=list(educations.keys()))
    education = educations[edl]

    # store into feature dict
    st.session_state.inputs.update({"Age": age,"Gender": gender,"Ethnicity": ethnicity,"Education": education,})

    nav_buttons()


def lf():
    st.write("### Lifestyle Factors")

    bmi = st.number_input("Enter BMI", min_value=10.0, max_value=50.0, format="%.2f")

    yes_no = {"No": 0, "Yes": 1}
    smoking = st.selectbox("Smoking Habit", options=list(yes_no.keys()))
    smoking_habit = yes_no[smoking]

    alcohol = st.number_input("Alcohol Consumption (units per week)", min_value=0, max_value=20)

    physical_activity = st.number_input("Physical Activity (hours per week)", min_value=0, max_value=10)

    diet = st.number_input("Diet Quality Score (1-10)", min_value=1, max_value=10)

    sleep = st.number_input("Average Sleep Duration (hours)", min_value=4, max_value=10)

    st.session_state.inputs.update({"BMI": float(bmi),"SmokingHabit": smoking_habit,"AlcoholConsumption": alcohol,"PhysicalActivity": physical_activity,"DietScore": diet,"SleepDuration": sleep,})

    nav_buttons()


def mh():
    st.write("### Medical History")

    yes_no = {"No": 0, "Yes": 1}

    fh = st.selectbox("Family history of Alzheimer's", options=list(yes_no.keys()))
    family_history_alzheimers = yes_no[fh]

    cvd = st.selectbox("Cardiovascular disease", options=list(yes_no.keys()))
    cardiovascular_disease = yes_no[cvd]

    diab = st.selectbox("Diabetes", options=list(yes_no.keys()))
    diabetes = yes_no[diab]

    dep = st.selectbox("Depression", options=list(yes_no.keys()))
    depression = yes_no[dep]

    hi = st.selectbox("History of head injury", options=list(yes_no.keys()))
    head_injury = yes_no[hi]

    ht = st.selectbox("Hypertension", options=list(yes_no.keys()))
    hypertension = yes_no[ht]

    st.session_state.inputs.update({"FamilyHistoryAlzheimers": family_history_alzheimers,"CardiovascularDisease": cardiovascular_disease,"Diabetes": diabetes,"Depression": depression,"HeadInjury": head_injury,"Hypertension": hypertension,})

    nav_buttons()


def cm():
    st.write("### Clinical Measurements")

    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)",min_value=90,max_value=180,value=120,step=1,)

    diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)",min_value=60,max_value=120,value=80,step=1,)

    cholesterol_total = st.number_input("Total Cholesterol (mg/dL)",min_value=150,max_value=300,value=200,step=1,)

    cholesterol_ldl = st.number_input("LDL Cholesterol (mg/dL)",min_value=50,max_value=200,value=100,step=1,)

    cholesterol_hdl = st.number_input("HDL Cholesterol (mg/dL)",min_value=20,max_value=100,value=50,step=1,)

    cholesterol_triglycerides = st.number_input("Triglycerides (mg/dL)",min_value=50,max_value=400,value=150,step=1,)

    st.session_state.inputs.update({"SystolicBP": systolic_bp,"DiastolicBP": diastolic_bp,"CholesterolTotal": cholesterol_total,"CholesterolLDL": cholesterol_ldl,"CholesterolHDL": cholesterol_hdl,"CholesterolTriglycerides": cholesterol_triglycerides,})

    nav_buttons()


def cf():
    st.write("### Cognitive & Functional Assessments")

    mmse = st.number_input("MMSE (Mini-Mental State Examination) Score (0–30)",min_value=0,max_value=30,value=24,step=1,)

    functional_assessment = st.number_input("Functional Ability Score (0–10)",min_value=0,max_value=10,value=7,step=1,)

    yes_no = {"No": 0, "Yes": 1}

    mc = st.selectbox("Memory complaints", options=list(yes_no.keys()))
    memory_complaints = yes_no[mc]

    bp = st.selectbox("Behavioral problems", options=list(yes_no.keys()))
    behavioral_problems = yes_no[bp]

    adl = st.number_input("ADL (Activities of Daily Living) Score (0–10)",min_value=0,max_value=10,value=8,step=1,)

    st.session_state.inputs.update({"MMSE": mmse,"FunctionalAssessment": functional_assessment,"MemoryComplaints": memory_complaints,"BehavioralProblems": behavioral_problems,"ADL": adl,})

    nav_buttons()


def sym():
    st.write("### Symptoms")

    yes_no = {"No": 0, "Yes": 1}

    conf = st.selectbox("Confusion", options=list(yes_no.keys()))
    confusion = yes_no[conf]

    diso = st.selectbox("Disorientation", options=list(yes_no.keys()))
    disorientation = yes_no[diso]

    pc = st.selectbox("Personality changes", options=list(yes_no.keys()))
    personality_changes = yes_no[pc]

    dct = st.selectbox("Difficulty completing daily tasks", options=list(yes_no.keys()))
    difficulty_completing_tasks = yes_no[dct]

    forg = st.selectbox("Forgetfulness", options=list(yes_no.keys()))
    forgetfulness = yes_no[forg]

    st.session_state.inputs.update({"Confusion": confusion,"Disorientation": disorientation,"PersonalityChanges": personality_changes,"DifficultyCompletingTasks": difficulty_completing_tasks,"Forgetfulness": forgetfulness,})

    nav_buttons()


def output():
    """Build X from all stored inputs (excluding pi) and show it."""
    global X
    features = st.session_state.get("inputs", {})

    if not features:
        st.warning("No input data captured yet.")
        return

    X = pd.DataFrame([features])   # 1 row, columns = feature names
    st.write("### Summary of Inputs (Model Features)")
    st.dataframe(X.T, use_container_width=True)


# ------------- Dispatcher ------------- #
SECTION_FUNCS = [
    pi,   # 0 - Patient Identification
    dd,   # 1 - Demographic Details
    lf,   # 2 - Lifestyle Factors
    mh,   # 3 - Medical History
    cm,   # 4 - Clinical Measurements
    cf,   # 5 - Cognitive & Functional Assessments
    sym,  # 6 - Symptoms
]

current_step = st.session_state.step
pb.progress_bar(current_step, total_steps)

# Render current section
SECTION_FUNCS[current_step]()

# If user clicked Submit, show X under the form
if st.session_state.show_output:
    output()
