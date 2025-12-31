import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from catboost import CatBoostClassifier
import elements.progressbar as pb
import warnings
warnings.filterwarnings('ignore')

st.sidebar.title("Alzheimer's Disease Classification")
st.sidebar.markdown("This application classifies Alzheimer's disease stages using machine learning models.")

st.sidebar.page_link("app.py", label="Home", icon="🧠")
st.sidebar.page_link("Pages/about.py", label="About", icon="❄️")

st.write("# Alzheimer's Disease Classification Application")

try:
    # Load dataset
    df = pd.read_csv("./Database/alzheimers_disease_data (1).csv")
    df = df.drop(columns=['PatientID', 'DoctorInCharge'], errors='ignore')
    df = df.fillna(df.median(numeric_only=True))

    # Separate features and target
    X = df.drop("Diagnosis", axis=1)
    y = df["Diagnosis"]
    feature_names = X.columns.tolist()

    # Scale features and train model
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = CatBoostClassifier(iterations=100, random_state=42, verbose=0)
    model.fit(X_scaled, y)
    st.success("✅ Model trained successfully!")
except Exception as e:
    st.error(f"⚠️ Error loading or training model: {str(e)}")

# Initialize session state for keeping track of variables
if "step" not in st.session_state:
    st.session_state.step = 0
if "inputs" not in st.session_state:
    st.session_state.inputs = {}
if "show_output" not in st.session_state:
    st.session_state.show_output = False

SECTION_TITLES = ["Demographic Details","Lifestyle Factors","Medical History","Clinical Measurements","Cognitive & Functional Assessments","Symptoms"]
total_steps = len(SECTION_TITLES)

def next_step():
    if st.session_state.step < total_steps - 1:
        st.session_state.step += 1

def prev_step():
    if st.session_state.step > 0:
        st.session_state.step -= 1

def submit():
    st.session_state.show_output = True

def nav_buttons():
    """Show Back and Next/Submit buttons"""
    step = st.session_state.step
    col1, col2 = st.columns(2)

    with col1:
        st.button("⬅ Back",use_container_width=True,disabled=(step == 0),on_click=prev_step,)

    with col2:
        if step < total_steps - 1:
            st.button("Next ➜", use_container_width=True, on_click=next_step)
        else:
            st.button("Submit ✔", use_container_width=True, on_click=submit)

# Demographic Details
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
    st.session_state.inputs.update({"Age": age,"Gender": gender,"Ethnicity": ethnicity,"EducationLevel": education})
    nav_buttons()

# Lifestyle Factors
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
    
    st.session_state.inputs.update({"BMI": float(bmi), "Smoking": smoking_habit, "AlcoholConsumption": alcohol, "PhysicalActivity": physical_activity, "DietQuality": diet, "SleepQuality": sleep})
    nav_buttons()

# Medical History
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
    st.session_state.inputs.update({"FamilyHistoryAlzheimers": family_history_alzheimers, "CardiovascularDisease": cardiovascular_disease, "Diabetes": diabetes, "Depression": depression, "HeadInjury": head_injury, "Hypertension": hypertension})
    nav_buttons()

# CLINICAL MEASUREMENTS
def cm():
    st.write("### Clinical Measurements")
    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=90, max_value=180, value=120, step=1)
    diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=60, max_value=120, value=80, step=1)
    cholesterol_total = st.number_input("Total Cholesterol (mg/dL)", min_value=150, max_value=300, value=200, step=1)
    cholesterol_ldl = st.number_input("LDL Cholesterol (mg/dL)", min_value=50, max_value=200, value=100, step=1)
    cholesterol_hdl = st.number_input("HDL Cholesterol (mg/dL)", min_value=20, max_value=100, value=50, step=1)
    cholesterol_triglycerides = st.number_input("Triglycerides (mg/dL)", min_value=50, max_value=400, value=150, step=1)
    st.session_state.inputs.update({"SystolicBP": systolic_bp, "DiastolicBP": diastolic_bp, "CholesterolTotal": cholesterol_total, "CholesterolLDL": cholesterol_ldl, "CholesterolHDL": cholesterol_hdl, "CholesterolTriglycerides": cholesterol_triglycerides})
    nav_buttons()

# COGNITIVE & FUNCTIONAL ASSESSMENTS
def cf():
    st.write("### Cognitive & Functional Assessments")
    mmse = st.number_input("MMSE (Mini-Mental State Examination) Score (0–30)", min_value=0, max_value=30, value=24, step=1)
    functional_assessment = st.number_input("Functional Ability Score (0–10)", min_value=0, max_value=10, value=7, step=1)
    yes_no = {"No": 0, "Yes": 1}
    mc = st.selectbox("Memory complaints", options=list(yes_no.keys()))
    memory_complaints = yes_no[mc]
    bp = st.selectbox("Behavioral problems", options=list(yes_no.keys()))
    behavioral_problems = yes_no[bp]
    adl = st.number_input("ADL (Activities of Daily Living) Score (0–10)", min_value=0, max_value=10, value=8, step=1)
    st.session_state.inputs.update({"MMSE": mmse, "FunctionalAssessment": functional_assessment, "MemoryComplaints": memory_complaints, "BehavioralProblems": behavioral_problems, "ADL": adl})
    nav_buttons()

# SYMPTOMS
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
    st.session_state.inputs.update({"Confusion": confusion, "Disorientation": disorientation, "PersonalityChanges": personality_changes, "DifficultyCompletingTasks": difficulty_completing_tasks, "Forgetfulness": forgetfulness})
    nav_buttons()

# PREDICTION OUTPUT
def output():
    features = st.session_state.get("inputs", {})
    if not features:
        st.warning("No input data captured yet.")
        return

    X_input = pd.DataFrame([features])
    
    st.write("---")
    st.write("## 📊 Analysis Results")
    
    with st.expander("📋 View Input Summary", expanded=False):
        st.dataframe(X_input.T, use_container_width=True)
    
    # Make prediction
    try:
        # Ensure all features are present
        for feature in feature_names:
            if feature not in X_input.columns:
                X_input[feature] = 0 
        
        X_ordered = X_input[feature_names]
        
        X_scaled = scaler.transform(X_ordered)
        
        prediction = model.predict(X_scaled)[0]
        prediction_proba = model.predict_proba(X_scaled)[0]  # [prob_no, prob_yes]
        
        st.write("### 🧠 Diagnosis Prediction")
        col1, col2 = st.columns(2)
        
        with col1:
            if prediction == 1:
                st.error("### ⚠️ Alzheimer's Disease Detected")
                st.write(f"**Confidence:** {prediction_proba[1]:.2%}")
            else:
                st.success("### ✅ No Alzheimer's Disease Detected")
                st.write(f"**Confidence:** {prediction_proba[0]:.2%}")
        
        with col2:
            st.metric(
                label="Model Used",
                value="CatBoost"
            )
        
        # Show probability breakdown
        st.write("### 📈 Prediction Probabilities")
        prob_df = pd.DataFrame({
            'Category': ['No Alzheimer\'s', 'Alzheimer\'s Disease'],
            'Probability': [f"{prediction_proba[0]:.2%}", f"{prediction_proba[1]:.2%}"]
        })
        st.dataframe(prob_df, use_container_width=True, hide_index=True)

        # Reset button to start over
        if st.button("🔄 Start New Assessment", use_container_width=True):
            st.session_state.step = 0
            st.session_state.inputs = {}
            st.session_state.show_output = False
            st.rerun()
            
    except Exception as e:
        st.error(f"⚠️ Error making prediction: {str(e)}")
        st.write("Please ensure all required fields are filled correctly.")


# List of all section functions
SECTION_FUNCS = [dd, lf, mh, cm, cf, sym]

# Show progress bar
current_step = st.session_state.step
pb.progress_bar(current_step, total_steps)

# Display current section
SECTION_FUNCS[current_step]()

# Show results if user submitted the form
if st.session_state.show_output:
    output()
