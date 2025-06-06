# Human Centered Data Science Alzheimer's Project

## Our Team

- Nino Sabella (MSc Data Science)
- Saad Waseem (MSc Data Science)
- Jingren Dai (MSc Data Science)
- Yasemin Mutlugil (MSc Computer Science)
- Orkun Akyol (MSc Data Science)

---

## 1. Dataset Description

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

## 2. Decision-Making Scenario

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

## 3. Stakeholder Analysis



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
