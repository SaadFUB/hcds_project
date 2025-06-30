# Human Centered Data Science Alzheimer's Project

## Our Team

- Nino Sabella (MSc Data Science)
- Saad Waseem (MSc Data Science)
- Jingren Dai (MSc Data Science)
- Yasemin Mutlugil (MSc Computer Science)
- Orkun Akyol (MSc Data Science)

---

## Dataset Description

<!-- Comment: Adjust your already present dataset documentation to fill out the question. Add more information. -->

**Dataset Name**: Alzheimer's Disease Dataset  
**Dataset Owner**: Rabie El Kharoua  
**Source / Link**: https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset/data    
**Domain / Context**: Healthcare, Medicine, Neurology    <!-- Comment: Can be more specific then "medical" -->  
**Number of Instances**: 2149   
**Number of Features**: 32  
**Possible Target Variable(s)**: 0 (= No Alzheimer's), 1 (= Has Alzheimer's).  
**Data Access & License**:  Attribution 4.0 International (CC BY 4.0)  

**Short Description**: The Alzehimer's Disease dataset is synthetic and was intended for educational use. It comprises health records for 2,149 patients, uniquely identified by IDs ranging from 4751 to 6900. The dataset encompasses a wide range of information, including demographics, lifestyle habits, medical history, clinical metrics, cognitive and functional evaluations and Alzheimer's Disease diagnoses. It serves as a valuable resource for researchers and data scientists aiming to investigate factors linked to Alzheimer's, build predictive models, and perform statistical analysis. For further information about the features, see *metadata.md*.
<!-- Comment: Write out in full sentences a short summary of your dataset. -->

---

## Decision-Making Scenario

<!-- 

Describe a real-world decision making scenario that your dataset and ML model could support.  

Goal: A person not familiar with your system should get an idea, when and how your system is being used. The scenario shall be written out in full sentences.

Things your short scenario description should include:
- Decision to be made. Example: A system helping to decide if someone needs to undergo surgery based on certain characteristics.
- How does the ML model support the decision?
- Context / Use Case: Who is using your system in which situation? Is it a surgeant using an explanation interface during surgery? Or a doctor doing a routine control? Or a patient getting information at home via a website? Please place your decision in a certain context.
- Type of ML Task : classification, regression, risk scoring, ...
- Constraints & Requirements: What constraints do you see? time-critical decisions, interpretability, legal constraints, data quality, technical constraints, ... 
- What is at stake in this decision?

-->

Consider a scenario where a primary care physician is assessing if a patient of 60+ years of age is showing signs of Alzheimer's disease. If the physician determines that the patient has a cognitive impairment, the patient is going to be referred to a neurologist for further examination. In this case, an ML model trained on this dataset can be integrated into the diagnostic procedures of the clinic, in which the physician enters certain information and receives a diagnosis prediction and risk score from the model, along with explanations highlighting the most influential factors that caused this prediction. 

Constraints and requirements: 

- The model needs to be interpretable as this is a high-risk domain, the physician needs to be able to justify the decision.
- There might be legal or ethical considerations about what features to use in the model.
- The data ussed in the training must be consistent and investigated for bias.

Stakes:

Early treatment in Alzheimer's disease might slow down disease progression, whereas delays in disease detection might limit treatment options. 

---

## Stakeholder Analysis



<!-- 

Goal: Find & Describe the key Stakeholders of your application

Tasks:
- Who are the key Stakeholders of your application? Start with writing a list.
- For each Stakeholder, decompose the expeted knowledge into the stakeholder expertise matrix you know from the lecture (Transparency Lecture)
- For each Stakeholder, state the stakeholder Goals, Objectives & Tasks according to the stakeholder needs pyramide you know from the lecture (Transparency Lecture)
- Create a set of key questions that you think your key stakeholders might have of your system. The questions from the earlier assignment should be a good start. From there you can re-formulate the questions from the point of view of each Stakeholder.

-->

#### Primary Care Physician
Stakeholder Knowledge:  
Instrumental ML Knowledge: Uses AI-powered tools in decisions  
Formal Data Domain Knowledge: Medical school training gives them expertise in the subject matter   
Formal Milieu Knowledge: Formal engagement with healthcare procedures and institutional practices  

Goals:
- G1, G2

Objectives:
- Understand the decision: O3, O4, O5

Tasks:
- T1, T3, T4, T5

Key Questions:
- How accurate is this system compared to standard diagnostics?
- What factors contributed most to this result?
  

#### Patients

Stakeholder Knowledge:  
Personal or no ML Knowledge: Only from personal experience or media narratives  
No Data Domain Knowledge  
Instrumental Milieu Knowledge: They engage in the environment to receive care  

Goals:
- G2

Objectives:
- Awareness about what data is used and contributed to the diagnosis: O5

Tasks:
- T1, T2

Key Questions:
- What does this result mean for me?
- How certain is the system about this diagnosis?


#### Data Scientist

Stakeholder Knowledge:  
Formal ML Knowledge: Theoretical understanding of ML models  
Instrumental Data Domain Knowledge: Learned through working with data and consulting experts  
Instrumental Milieu Knowledge: Needs to be aware of the needs&requirements  

Goals:
- G1, G2

Objectives:
- Make sure model meets needs: O1, O2, O6

Tasks:
- T2, T3, T4, T5

Key Questions:
- What are the most important features?
- How generalizable is this model?


#### Hospital Management

Stakeholder Knowledge:  
Personal ML Knowledge   
Formal Data Domain Knowledge: Understands hospital regulations, clinical workflows   
Formal Milieu Knowledge: Deep knowledge of healthcare system structure   

Goals:
- G2

Objectives:
- Seamless integration of model to workflows: O2, 03, O4

Tasks:
- T1, T2, T5

Key Questions:
- What are the costs and benefits of using this system?
- Does it reduce diagnostic time or error rates?
- What training does staff need to use it effectively?


#### Regulatory Bodies

Stakeholder Knowledge:  
Formal ML Knowledge: Need to be able to evaluate models based on standards for transparency, bias, and fairness   
Formal Data Domain Knowledge: Legal/ethical knowledge in the domain  
Formal Milieu Knowledge: Needs to operate in the legal/medical environment   

Goals:
- G1, G2

Objectives:
- Make sure it complies with ethical standards: O2, 05, 07

Tasks:
- T1, T2, T5

Key Questions:
- Is the model explainable?
- How is patient consent and data privacy handled?
- Are there biases in the training data?

---

## Primary Stakeholder

Our **primary stakeholder** is the **physician (i.e., the primary care doctor)**. They are the intended end-user of the application and the person who will use the model’s output during patient consultations. Their needs and constraints will guide our design decisions, particularly around interpretability and transparent model explanations, while we prioritize the ethical use of features and bias minimization.

### 1. What prior knowledge do the stakeholders need to use your application?
The physician should have:
- Basic digital literacy to navigate a clinical interface or electronic health records system.
- Some basic medical knowledge related to Alzheimer’s disease and cognitive impairment. (Not strictly required, but it is a plus).  This can help the physician:
  - Better understand the clinical relevance of the model's inputs and outputs
  - Interpret the risk score and feature explanations more confidently
  - Make more informed decisions about next steps (e.g., referrals or additional testing)
The physician does not need prior knowledge of machine learning, statistical modeling, or programming. The application should be intuitive and require only clinically relevant inputs.

### 2. What explanations might the stakeholder need?
The physician might need:
- A clear and concise prediction output, such as whether the patient is at risk of Alzheimer’s or not.
- Some kind of score or risk probability (e.g., "78% chance of Alzheimer’s).
- One or more visual summaries (e.g., bar charts) showing which features contributed most to the decision (e.g., SHAP values), presented in a simple, meaningful way.
- An explanation of the key factors influencing the prediction (e.g., "Based on the patient’s age, history, etc.“).
These can help the physician understand, trust, and justify the model's recommendation.

### 3. What prior knowledge in data science is needed to understand the decision?
None to minimal. The physician does not need to understand how the machine learning model works. The system should translate technical decisions into interpretable medical insights, similar to tools they already use.

---

## Individual Paper Prototypes

![Individual Paper Prototype 1](https://github.com/user-attachments/assets/b411a527-d90e-42b5-a895-311f4f21481a)
![Individual Paper Prototype 2](https://github.com/user-attachments/assets/bc57cc1f-80a0-42c4-bc64-a24b0d15568d)
![Individual Paper Prototype 3](https://github.com/user-attachments/assets/4c7c9a2f-84e2-468d-9e7a-012acc64099e)
![Individual Paper Prototype 4](https://github.com/user-attachments/assets/a505363e-873a-4a89-bb5e-d6fd35479618)
![Individual Paper Prototype 5](https://github.com/user-attachments/assets/b97f19bf-eda4-457e-9e6c-13e8938f9dc4)

## Group Paper Prototype

![Group Paper Prototype](https://github.com/user-attachments/assets/01827246-e064-4244-8f9c-7702c1d03389)

## Scenario Walkthrough

### Group Sketch with Paper Prototypes

![Paper Prototype Scenario Walkthrough](https://github.com/user-attachments/assets/5b0318cb-684b-42b1-87e7-947b8a8d4f78)

### Scenario Walkthrough with Wireframes

![Wireframe Scenario Walkthrough](https://github.com/user-attachments/assets/64689bf6-8299-4a99-a507-e916bbcb4966)

---

## Interview Guide

### 1. Define User Needs & Key Questions

**Main User Needs:**

- Predict Alzheimer’s risk.
- Understand the reasoning behind the prediction.
- Decide what actions to take based on the prediction.
- Find trustworthy information/resources for patient education.
- Understand how the model works and how reliable it is.

**Possible user interview questions:**

- What do you expect from a tool that helps assess Alzheimer’s risk?
- How important is it for you to understand how the prediction was made?
- What would help you trust a prediction made by a tool like this?
- Would such a tool change how you interact with your patients

### 2. Ask for Consent

*Before we begin, we would like to ask for your consent to use your responses anonymously for our project presentation and evaluation.*

### 3. Introduce the Scenario

*We developed a tool that assesses a patient’s risk of developing Alzheimer’s based on their demographic, health and lifestyle data. The prediction of the tool is not supposed to replace medical advice, it is only meant to support the physicians in their decision making process. Today, you will imagine that you are a physician and you are trying out our tool for the first time.*

### 4. Warm-up Questions

- Have you ever used any apps or tools to track your well-being?
- If yes, what were your expectations when using such tools?
- Have you or someone close to you ever worried about cognitive issues?
- Who do you think would use an app like this?

### 5.1 Tasks - Prototype Walkthrough

*Now we’ll walk through the prototype together. Please think aloud as you go - describe what you see, what you’re thinking, and what you expect to happen.*

**Homepage**
**Q:** What do you think you can do here?
**Task 1:** You now want to make a prediction - how would you proceed?

**Making a Prediction**
**Q:** What do you think you can do here?
**Q:** Are any of the input fields unclear?
**Task 2:** Please fill in the patient’s data and make a prediction.

**Understanding the Prediction**
**Task 3:** Now try to understand the prediction shown without clicking further. What do you understand from it?
**Task 4:** Can you interpret the graphs to understand why this prediction was made? Is the text explanation helpful?
**Task 5:** Does this result lead you to take any specific action (e.g., referral, patient education)? If so, what?

**Providing Resources**
**Task 6:** Now you would like to provide your patient with some relevant resources. Where would you look?
**Q:** What do you think about this page?

**Understanding the Model**
**Task 7:** Now you want to understand how the model works. Where do you expect to find this information?
**Q:** What do you think about this page?

### 5.2 Post-Interview Feedback Questions: 

- What did you like (or dislike) most about the app?
- If you could change one thing about the app, what would it be?
- Would you trust this app’s predictions? Why or why not?
- Is there anything missing that you would expect to see in this kind of app?
- How do you feel about privacy in this context?

### 6. Finish and Goodbyes

*That is all on our side! Thank you so much for your feedback. Is there anything else you would like to share?*
