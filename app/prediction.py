import streamlit as st
from production.inference import REQUIRED_FEATURES
from production.inference import predict, load_random_row, explain_waterfall, explain_force, violin_with_user_value, pdp_with_user_value, explain_shap_values
import matplotlib.colors as mcolors


#st.set_page_config(page_title="Alzheimer's Risk Assessment", layout="wide")

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

recommendations = [
  {
    "title": "Healthy Lifestyle and Mental Stimulation",
    "description": "Encourage regular physical activity, a balanced diet (e.g., Mediterranean), social interaction, and brain-stimulating activities like reading or puzzles. These can help slow cognitive decline in the early stages or even as a preventive measure.",
    "stage": 1
  },
  {
    "title": "Routine Monitoring and Medication Review",
    "description": "Schedule periodic check-ups to monitor memory and cognitive function. Consider discussing medications like cholinesterase inhibitors (e.g., donepezil) with a specialist to potentially manage early symptoms.",
    "stage": 2
  },
  {
    "title": "Establishing Safety Measures at Home",
    "description": "As symptoms progress, make environmental adjustments such as labeling drawers, using reminder notes, installing safety locks, and minimizing trip hazards to promote safe, independent living.",
    "stage": 3
  },
  {
    "title": "Involving Caregivers and Advanced Planning",
    "description": "Include family or professional caregivers in the care routine. Discuss legal and financial planning early (e.g., power of attorney, advance directives) while the patient can still participate meaningfully.",
    "stage": 4
  },
  {
    "title": "Palliative and Full-Time Care Options",
    "description": "In advanced stages, consider hospice or specialized memory care facilities. Focus shifts to comfort, managing distressing symptoms, and supporting caregivers emotionally and practically.",
    "stage": 5
  }
]


def value_to_color(value):
    norm_value = value / 100.0

    cmap = mcolors.LinearSegmentedColormap.from_list(
        "custom_gradient", ["green", "yellow", "red"]
    )
    
    rgba = cmap(norm_value)
    
    return mcolors.to_hex(rgba)


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

with col2:
    diet_quality = st.slider("Diet Quality (0-10)", **numerical_config['DietQuality'],
                             help="self reported, 0=a very poor diet, 10=very healthy diet")
    sleep_quality = st.slider("Sleep Quality (4-10)", **numerical_config['SleepQuality'],
                              help ="self reported, 4=very poor sleep, 10=excellent, restful sleep")
    physical_activity = st.slider("Physical Activity Level (0-10)", **numerical_config['PhysicalActivity'],
                                  help="Weekly physical activity in hours")

st.markdown("---")

st.header("🏥 Health History & Medical Conditions")
col1, col2 = st.columns(2)

with col1:
    family_history = st.selectbox("Family History of Alzheimer's", categorical_options['FamilyHistoryAlzheimers'])
    head_injury = st.selectbox("History of Head Injury", categorical_options['HeadInjury'])
    cardiovascular = st.selectbox("Cardiovascular Disease", categorical_options['CardiovascularDisease'])

with col2:
    depression = st.selectbox("Depression", categorical_options['Depression'])
    hypertension = st.selectbox("Hypertension", categorical_options['Hypertension'])
    diabetes = st.selectbox("Diabetes", categorical_options['Diabetes'])

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


with col2:
    adl = st.slider("Activities of Daily Living (0-10)", **numerical_config['ADL'],
                   help="Independence in daily activities")
    functional_assessment = st.slider("Functional Assessment (0-10)", **numerical_config['FunctionalAssessment'],
                                    help="Overall functional ability")

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

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Reset Form", use_container_width=True):
        st.session_state.show_prediction = False
        st.rerun()



with col2:
    if st.button("Predict Risk", use_container_width=True, type="primary"):
        st.session_state.show_prediction = True
        st.session_state.update_prediction = True
        
        st.success("Data submitted successfully! Loading Prediction...")
    


def get_top_features(form_data, model_name, n=5):
    shap_values = explain_waterfall(form_data, model_name, return_fig=False)
    top_features = sorted(shap_values, key=lambda x: abs(shap_values[x]), reverse=True)
    return top_features[:n]


if st.session_state.show_prediction:
    if st.session_state.update_prediction:
        st.session_state.update_prediction = False
        st.session_state.avg_score = 0

        predictions = {model: predict(st.session_state.form_data, model) for model in models}

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.markdown('<h2 style="text-align: center;">Risk of Alzheimer\'s: Model Comparison</h2>', unsafe_allow_html=True, help="We use three models—Logistic Regression, Random Forest, and Neural Network—to balance accuracy and interpretability. Logistic Regression offers transparency, Random Forest adds robustness and handles complex patterns, while Neural Networks capture subtle nonlinearities with high performance. This combination ensures both clinical trust and predictive strength.")
            st.markdown(
                        """
                        <div style='text-align: center;'>
                            <a href="/methodology" style='text-decoration: none;'>
                                <button style='
                                    padding: 0.5em 1.2em;
                                    font-size: 1rem;
                                    background-color: transparent;
                                    color: #615842;
                                    border: 2px solid #615842;
                                    border-radius: 5px;
                                    cursor: pointer;
                                '>
                                    More Info
                                </button>
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
             


        cols = st.columns(len(models))
        for i, model in enumerate(models):
            with cols[i]:

                prediction_val = int(predictions[model]["probability"][0][1] * 100)
                st.session_state.avg_score += prediction_val/3

                st.markdown(f"<div style='font-size:1.1rem; font-weight:600; margin-bottom:10px; text-align: center;'>{model}</div>",
                            unsafe_allow_html=True)
                st.markdown(
                    f"""<div style="width: 80px; height: 80px; 
                            border-radius: 50%; background-color: {value_to_color(prediction_val)}; 
                            display: flex; align-items: center; 
                            justify-content: center; color: white; 
                            margin: 10px auto;">{prediction_val}%</div>""",
                    unsafe_allow_html=True
                )

        exp_tabs = st.tabs(models)
        for i, model in enumerate(models):
            with exp_tabs[i]:
                explain_force(st.session_state.form_data, model)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    data, fig = explain_waterfall(st.session_state.form_data, model, return_fig=True)
                    st.pyplot(fig)
                    st.write(explain_shap_values(data))

        st.markdown("---")
        st.markdown(f"### Top Influential Features: Patient vs Population", help="""
Violin Plot:
The violin plot shows you how a specific feature is distributed across patients with and without Alzheimer’s. Your patient’s value is marked on the plot, helping you see where they fall relative to typical cases. This gives you quick visual insight into whether the input aligns more with low- or high-risk groups.

Partial Dependence Plot:
The partial dependence plot helps you understand how changes in one feature affect the model’s prediction, while all other factors are held constant. It shows you the model’s learned relationship between that feature and Alzheimer’s risk. This helps you assess how influential that feature is in your patient’s case.                    

""")


        for model in models:
            top_features = get_top_features(st.session_state.form_data, model, n=5)
            with st.expander(f"{model}: Patient vs Population for Top Features", expanded=(model == models[0])):
                tabs = st.tabs(top_features)
                for tab, feature in zip(tabs, top_features):
                    with tab:
                        c1, c2 = st.columns([1, 1])
                        with c1:
                            violin_with_user_value(feature, st.session_state.form_data, key=f"{model}_{feature}_violin")
                        with c2:
                            pdp_with_user_value(feature, st.session_state.form_data, model, key=f"{model}_{feature}_pdp")

            
    if st.session_state.avg_score > 60:
        recoms = recommendations[2:5]
    elif st.session_state.avg_score > 30:
        recoms = recommendations[1:4]
    else:
        recoms = recommendations[0:3]

    st.markdown("### Recommendations")
    cols = st.columns([1, 1, 1])
    for i, recom in enumerate(recoms):
        with cols[i]:
            with st.container(border=True):
                st.markdown("<div style='text-align: center; font-weight: bold;'>"+recom["title"]+"</div>", unsafe_allow_html=True)
                st.write(recom["description"])
                st.markdown(
                        """
                        <div style='text-align: center;'>
                            <a href="/resources" style='text-decoration: none;'>
                                <button style='
                                    padding: 0.5em 1.2em;
                                    font-size: 1rem;
                                    background-color: transparent;
                                    color: #615842;
                                    border: 2px solid #615842;
                                    border-radius: 5px;
                                    cursor: pointer;
                                    margin-bottom: 10px;
                                '>
                                    More Resources
                                </button>
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
