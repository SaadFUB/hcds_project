import streamlit as st
import pandas as pd
from production.inference import REQUIRED_FEATURES
from production.inference import predict
from production.inference import load_random_row
from production.inference import explain_waterfall
from production.inference import explain_force
from production.inference import violin_with_user_value
from production.inference import pdp_with_user_value
from production.inference import explain_shap_values


st.set_page_config(page_title="Alzheimer's Risk Assessment", layout="wide")

NUM_FEATURES = [
    'Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality',
    'SystolicBP', 'DiastolicBP',
    'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides',
    'MMSE', 'FunctionalAssessment', 'ADL'
]

CAT_FEATURES = [
    'Gender', 'Ethnicity', 'EducationLevel',
    'Smoking', 'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes', 'Depression',
    'HeadInjury', 'Hypertension',
    'MemoryComplaints', 'BehavioralProblems', 'Confusion', 'Disorientation',
    'PersonalityChanges', 'DifficultyCompletingTasks', 'Forgetfulness'
]

models = ['Logistic Regression', 'Random Forest', 'Neural Network']

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Ethnicity': ['Caucasian', 'African American', 'Asian', 'Other'],
    'EducationLevel': ['None', 'High School', 'Bachelor\'s', 'Higher'],
    'Smoking': ['No', 'Yes'],
    'FamilyHistoryAlzheimers': ['No', 'Yes'],
    'CardiovascularDisease': ['No', 'Yes'],
    'Diabetes': ['No', 'Yes'],
    'Depression': ['No', 'Yes'],
    'HeadInjury': ['No', 'Yes'],
    'Hypertension': ['No', 'Yes'],
    'MemoryComplaints': ['No', 'Yes'],
    'BehavioralProblems': ['No', 'Yes'],
    'Confusion': ['No', 'Yes'],
    'Disorientation': ['No', 'Yes'],
    'PersonalityChanges': ['No', 'Yes'],
    'DifficultyCompletingTasks': ['No', 'Yes'],
    'Forgetfulness': ['No', 'Yes']
}

numerical_config = {
    'Age': {'min_value': 18, 'max_value': 120, 'value': 65, 'step': 1},
    'BMI': {'min_value': 15.0, 'max_value': 40.0, 'value': 25.0, 'step': 0.1},
    'AlcoholConsumption': {'min_value': 0, 'max_value': 20, 'value': 2, 'step': 1},
    'PhysicalActivity': {'min_value': 0, 'max_value': 10, 'value': 5, 'step': 1},
    'DietQuality': {'min_value': 0, 'max_value': 10, 'value': 6, 'step': 1},
    'SleepQuality': {'min_value': 4, 'max_value': 10, 'value': 7, 'step': 1},
    'SystolicBP': {'min_value': 90, 'max_value': 180, 'value': 120, 'step': 1},
    'DiastolicBP': {'min_value': 60, 'max_value': 120, 'value': 80, 'step': 1},
    'CholesterolTotal': {'min_value': 150, 'max_value': 300, 'value': 200, 'step': 1},
    'CholesterolLDL': {'min_value': 50, 'max_value': 200, 'value': 100, 'step': 1},
    'CholesterolHDL': {'min_value': 20, 'max_value': 100, 'value': 50, 'step': 1},
    'CholesterolTriglycerides': {'min_value': 50, 'max_value': 400, 'value': 150, 'step': 1},
    'MMSE': {'min_value': 0, 'max_value': 30, 'value': 28, 'step': 1},
    'FunctionalAssessment': {'min_value': 0, 'max_value': 10, 'value': 8, 'step': 1},
    'ADL': {'min_value': 0, 'max_value': 10, 'value': 9, 'step': 1}
}

if 'form_data' not in st.session_state:
    st.session_state.form_data = {}
    st.session_state.model = models[0]
    st.session_state.show_prediction = False
    st.session_state.update_prediction = False

st.title("🧠 Alzheimer's Disease Risk Assessment")
st.markdown("Please fill out the following information to assess your risk for Alzheimer's disease.")
st.markdown("---")

st.header("👤 Demographics & Basic Information")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (years)", **numerical_config['Age'])
    gender = st.selectbox("Gender", categorical_options['Gender'])
    ethnicity = st.selectbox("Ethnicity", categorical_options['Ethnicity'])

with col2:
    education = st.selectbox("Education Level", categorical_options['EducationLevel'])
    bmi = st.number_input("BMI (kg/m²)", **numerical_config['BMI'])

st.markdown("---")

st.header("🏃 Lifestyle Factors")
col1, col2 = st.columns(2)

with col1:
    smoking = st.selectbox("Smoking", categorical_options['Smoking'])
    alcohol = st.number_input("Alcohol Consumption (drinks/week)", **numerical_config['AlcoholConsumption'])
    physical_activity = st.slider("Physical Activity Level (0-10)", **numerical_config['PhysicalActivity'])

with col2:
    diet_quality = st.slider("Diet Quality (0-10)", **numerical_config['DietQuality'])
    sleep_quality = st.slider("Sleep Quality (4-10)", **numerical_config['SleepQuality'])

st.markdown("---")

st.header("🏥 Health History & Medical Conditions")
col1, col2 = st.columns(2)

with col1:
    family_history = st.selectbox("Family History of Alzheimer's", categorical_options['FamilyHistoryAlzheimers'])
    head_injury = st.selectbox("History of Head Injury", categorical_options['HeadInjury'])
    cardiovascular = st.selectbox("Cardiovascular Disease", categorical_options['CardiovascularDisease'])
    diabetes = st.selectbox("Diabetes", categorical_options['Diabetes'])

with col2:
    depression = st.selectbox("Depression", categorical_options['Depression'])
    hypertension = st.selectbox("Hypertension", categorical_options['Hypertension'])

st.markdown("---")

st.header("🩺 Vital Signs")
col1, col2 = st.columns(2)

with col1:
    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", **numerical_config['SystolicBP'])

with col2:
    diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", **numerical_config['DiastolicBP'])

st.markdown("---")

st.header("🧪 Laboratory Results")
st.caption("Normal ranges provided for reference")
col1, col2 = st.columns(2)

with col1:
    total_chol = st.number_input("Total Cholesterol (mg/dL)", **numerical_config['CholesterolTotal'], 
                               help="Normal: < 200 mg/dL")
    ldl_chol = st.number_input("LDL Cholesterol (mg/dL)", **numerical_config['CholesterolLDL'],
                             help="Normal: < 100 mg/dL")

with col2:
    hdl_chol = st.number_input("HDL Cholesterol (mg/dL)", **numerical_config['CholesterolHDL'],
                             help="Normal: > 40 mg/dL (men), > 50 mg/dL (women)")
    triglycerides = st.number_input("Triglycerides (mg/dL)", **numerical_config['CholesterolTriglycerides'],
                                  help="Normal: < 150 mg/dL")

st.markdown("---")

st.header("🧠 Cognitive Assessment")
col1, col2 = st.columns(2)

with col1:
    mmse = st.number_input("MMSE Score (0-30)", **numerical_config['MMSE'],
                         help="Mini-Mental State Examination. Normal: 24-30")
    functional_assessment = st.slider("Functional Assessment (0-10)", **numerical_config['FunctionalAssessment'],
                                    help="Overall functional ability")

with col2:
    adl = st.slider("Activities of Daily Living (0-10)", **numerical_config['ADL'],
                   help="Independence in daily activities")

st.markdown("---")

st.header("🧩 Symptoms & Behavioral Assessment")
col1, col2 = st.columns(2)

with col1:
    memory_complaints = st.selectbox("Memory Complaints", categorical_options['MemoryComplaints'])
    behavioral_problems = st.selectbox("Behavioral Problems", categorical_options['BehavioralProblems'])
    confusion = st.selectbox("Confusion", categorical_options['Confusion'])
    disorientation = st.selectbox("Disorientation", categorical_options['Disorientation'])

with col2:
    personality_changes = st.selectbox("Personality Changes", categorical_options['PersonalityChanges'])
    difficulty_tasks = st.selectbox("Difficulty Completing Tasks", categorical_options['DifficultyCompletingTasks'])
    forgetfulness = st.selectbox("Forgetfulness", categorical_options['Forgetfulness'])

st.session_state.model = st.selectbox("Select Model", models)

st.markdown("---")


form_data = {
    
    'Age': age, 'BMI': bmi, 'AlcoholConsumption': alcohol, 'PhysicalActivity': physical_activity,
    'DietQuality': diet_quality, 'SleepQuality': sleep_quality, 'SystolicBP': systolic_bp,
    'DiastolicBP': diastolic_bp, 'CholesterolTotal': total_chol, 'CholesterolLDL': ldl_chol,
    'CholesterolHDL': hdl_chol, 'CholesterolTriglycerides': triglycerides, 'MMSE': mmse,
    'FunctionalAssessment': functional_assessment, 'ADL': adl,
    
    
    'Gender': gender, 'Ethnicity': ethnicity, 'EducationLevel': education, 'Smoking': smoking,
    'FamilyHistoryAlzheimers': family_history, 'CardiovascularDisease': cardiovascular,
    'Diabetes': diabetes, 'Depression': depression, 'HeadInjury': head_injury,
    'Hypertension': hypertension, 'MemoryComplaints': memory_complaints,
    'BehavioralProblems': behavioral_problems, 'Confusion': confusion,
    'Disorientation': disorientation, 'PersonalityChanges': personality_changes,
    'DifficultyCompletingTasks': difficulty_tasks, 'Forgetfulness': forgetfulness
}

st.session_state.form_data = form_data

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Reset Form", use_container_width=True):
        st.session_state.show_prediction = False
        st.rerun()



with col2:
    if st.button("Predict Risk", use_container_width=True, type="primary"):
        st.session_state.show_prediction = True
        st.session_state.update_prediction = True
        
        st.success("Data submitted successfully! Loading Prediction...")
        

with col3:
    if st.button("Randomize Prediction", use_container_width=True, type="secondary"):
        st.session_state.form_data = load_random_row()
        st.session_state.update_prediction = True
        st.session_state.show_prediction = True
        st.success("Random Data submitted successfully! Loading Prediction...")


if st.session_state.show_prediction:
    if st.session_state.update_prediction:
        st.session_state.update_prediction = False
        
        prediction = predict(st.session_state.form_data, st.session_state.model)

        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col2:
            st.markdown('<h2 style="text-align: center;">Risk of Alzheimer\'s</h2>', unsafe_allow_html=True)
            st.markdown(f"""<div style="width: 80px; height: 80px; 
                            border-radius: 50%; background-color: #858481; 
                            display: flex; align-items: center; 
                            justify-content: center; color: white; 
                            margin: 10px auto;">{int(prediction["probability"][0][1] * 100)}%</div>""", 
                        unsafe_allow_html=True)
        

        col1, col2, col3 = st.columns([1, 5, 1])

        with col2:
            with st.expander("User vs Population Distributions", expanded=True):
                
                pop_features = ['FunctionalAssessment', 'ADL' , 'MemoryComplaints', 'BehavioralProblems', 'MMSE', 'CholesterolTriglycerides', 'Age', 'PhysicalActivity']
                tabs = st.tabs(pop_features)

                for tab, feature in zip(tabs, pop_features):
                    with tab:
                        col1, col2 = st.columns([1, 1])
                        with col1:
                            violin_with_user_value(feature, st.session_state.form_data)
                        with col2:
                            pdp_with_user_value(feature, st.session_state.form_data, st.session_state.model)
                
            

        col1, col2, col3, col4 = st.columns([2, 0.5, 2, 0.5])

        with col1:
            explain_force(st.session_state.form_data, st.session_state.model)
            explanantion_data = explain_waterfall(st.session_state.form_data, st.session_state.model)
        
        with col3:
            st.write(explain_shap_values(explanantion_data))
        
        # st.json({k: v for k, v in st.session_state.form_data.items()})
