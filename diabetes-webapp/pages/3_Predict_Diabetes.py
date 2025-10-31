#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 12:27:38 2025

@author: namithabhaskar
"""

import streamlit as st
import shap
from streamlit_shap import st_shap
import pandas as pd
import os
import joblib

# st.write("Current working directory:", os.getcwd())
# st.write("File exists:", os.path.exists("../LightGBM_Manual_model.pkl"))
# st.write("Files in working directory:", os.listdir())

if st.query_params.get("reset") == "1":
    st.query_params.clear()
    st.rerun()

# Load the LightGBM model
model_path = os.path.join(os.path.dirname(__file__), "..", "LightGBM_Manual_model.pkl")
lgbm_model = joblib.load(model_path)

# Load the XGBoost model 
xgb_path = os.path.join(os.path.dirname(__file__), "..", "XGBoost_Manual_model.pkl")
xgb_model = joblib.load(xgb_path)

st.title("🧪 Diabetes Risk Prediction")

st.write("Fill out the form below to check your diabetes risk.")

# Model selection
model_option = st.radio("Choose a model:", ("LightGBM", "XGBoost"))

# Input form
with st.form("diabetes_form"):
    col1, col2 = st.columns(2)

    with col1:
        highbp_input = st.radio("Do you have high blood pressure?", ["Yes", "No"])
        HighBP = 1 if highbp_input == "Yes" else 0
        
        highchol_input = st.radio("Do you have high cholestrol?", ["Yes", "No"])
        HighChol = 1 if highchol_input == "Yes" else 0
        
        cholcheck_input = st.radio("Have you checked your Cholestrol in the last 5 years? ", ["Yes", "No"])
        CholCheck = 1 if cholcheck_input == "Yes" else 0
        
        BMI = st.number_input("BMI", min_value=10.0, max_value=90.0, step=0.1)
        
        smoker_input = st.radio("Have you smoked at least 100 cigarettes in your entire life?", ["Yes", "No"])
        Smoker = 1 if smoker_input == "Yes" else 0
        
        stroke_input = st.radio("Have you had a Stroke?", ["Yes", "No"])
        Stroke = 1 if stroke_input == "Yes" else 0
        
        heart_input = st.radio("Have you ever had a heart attack or heart disease?", ["Yes", "No"])
        HeartDiseaseorAttack = 1 if heart_input == "Yes" else 0
        
        physical_input = st.radio("Did you do any physical activity in past 30 days - (not including job)", ["Yes", "No"])
        PhysActivity = 1 if physical_input == "Yes" else 0
        
        fruits_input = st.radio("Consume Fruit 1 or more times per day?", ["Yes", "No"])
        Fruits = 1 if fruits_input == "Yes" else 0
        
        veggies_input = st.radio("Consume Vegetables 1 or more times per day?", ["Yes", "No"])
        Veggies = 1 if veggies_input == "Yes" else 0
        

    with col2:
        
        alcohol_input = st.radio("Are you a heavy drinker?", ["Yes", "No"])
        HvyAlcoholConsump = 1 if alcohol_input == "Yes" else 0
        
        anyHealth_input = st.radio("Have any kind of health care coverage, including health insurance, prepaid plans such as HMO? ", ["Yes", "No"])
        AnyHealthcare = 1 if anyHealth_input == "Yes" else 0
        
        docCost_input = st.radio("Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?", ["Yes", "No"])
        NoDocbcCost = 1 if docCost_input == "Yes" else 0
        
        GenHlth = st.slider("General Health - 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor", 1, 5)
        
        MentHlth = st.slider(
            "Now thinking about your mental health, which includes stress, depression, and problems with emotions, "
            "for how many days during the past 30 days was your mental health not good?", 0, 30)
        
        PhysHlth = st.slider("Now thinking about your physical health, which includes physical illness and injury," 
                "for how many days during the past 30 days was your physical health not good?", 0, 30)
        
        diffWalk_input = st.radio("Do you have serious difficulty walking or climbing stairs?", ["Yes", "No"])
        DiffWalk = 1 if diffWalk_input == "Yes" else 0
        
        sex_input = st.radio("Gender", ["Female", "Male"])
        Sex = 1 if sex_input == "Male" else 0
        
        age_input = st.selectbox(
            "What is your age group?",
            ["18–39", "40–64", "65–99"])

        Age_Categorized = {
            "18–39": 1,
            "40–64": 2,
            "65–99": 3
        }[age_input]
        
        education_input = st.selectbox(
            "What is your highest education level?",
            [
                "High School or below (Up to GED)",
                "Some college or technical school (1–3 years)",
                "College graduate (4+ years)"
                ])
        
        Education_Categorized = {
            "High School or below (Up to GED)": 1,
            "Some college or technical school (1–3 years)": 2,
            "College graduate (4+ years)": 3
        }[education_input]
                
        income_input = st.selectbox(
            "What is your income range?",
            [
                "Less than $35,000",
                "$35,000 – $75,000",
                "More than $75,000"
                ])

        Income_Categorized = {
            "Less than $35,000": 1,
            "$35,000 – $75,000": 2,
            "More than $75,000": 3
        }[income_input]

    submitted = st.form_submit_button("🔍 Predict")

if submitted:

    input_data = pd.DataFrame([[
        HighBP, HighChol, CholCheck, BMI, Smoker, Stroke,
        HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
        HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth,
        MentHlth, PhysHlth, DiffWalk, Sex,
        Age_Categorized, Education_Categorized, Income_Categorized
    ]], columns=[
        'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke',
        'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
        'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
        'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex',
        'Age_Categorized', 'Education_Categorized', 'Income_Categorized'
    ])

    # Choose model and predict
    # model = lgbm_model if model_option == "LightGBM" else xgb_model
    # prob = model.predict_proba(input_data)[0][1]
    # prediction = "🟢 Not Diabetic" if prob < 0.5 else "🔴 Diabetic"

    # st.success(f"**Prediction Result**: {prediction}")
    # st.write(f"**Probability of Diabetes:** {prob:.2f}")
    
    model = lgbm_model if model_option == "LightGBM" else xgb_model
    
    # Predict probability
    prob = model.predict_proba(input_data)[0][1]
    
    # ✅ Set best threshold per model
    if model_option == "LightGBM":
        threshold = 0.563
    elif model_option == "XGBoost":
        threshold = 0.555
    else:
        threshold = 0.5  # fallback/default

    # Predict class using threshold
    prediction = 1 if prob >= threshold else 0

    # Display results
    if prediction == 1:
        st.error("🛑 At risk of diabetes")
    else:
        st.success("✅ Not at risk of diabetes")

    st.write(f"**Prediction Probability:** {prob:.3f}")
    
    # Step: SHAP Interpretability
    explainer = shap.Explainer(model)  # LightGBM or XGBoost
    shap_values = explainer(input_data)

    st.markdown("### 🔍 Why this prediction?")
    st_shap(shap.plots.waterfall(shap_values[0]), height=500)
    
    # Brief explanation
    st.info("The waterfall plot shows how each feature pushed the prediction toward diabetic or not diabetic. "
            "Features in red increase risk, and features in blue decrease it.")
    
    st.markdown("### 💡 Recommendations")

    if prediction == 1:
        st.warning("You may be at risk of diabetes.")
        st.write("- Consider consulting a healthcare provider for a professional diagnosis.")
        st.write("- Adopt a balanced diet and regular physical activity routine.")
        st.write("- Manage stress and monitor blood pressure and weight.")
    else:
        st.success("You are not currently at risk of diabetes.")
        st.write("- Continue maintaining healthy lifestyle habits.")
        st.write("- Schedule regular health check-ups to stay informed.")
        st.write("- Keep track of changes in physical or mental health.")


    
# Reset form
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🧹 Clear Form"):
        st.query_params["reset"] = "1"
        st.rerun()

with col2:
    if st.button("🔙 Back to Home"):
        st.switch_page("app.py")
    

# 🔏 Footer
st.markdown("""
<hr style='border: 0.5px solid #ccc; margin-top: 50px;'>
<div style='text-align: center; color: grey; font-size: 14px;'>
    &copy; 2025 GlucoBot. Namitha Bhaskar. All rights reserved.
</div>
""", unsafe_allow_html=True)
