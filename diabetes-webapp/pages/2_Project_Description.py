#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 12:27:06 2025

@author: namithabhaskar
"""

import streamlit as st

st.set_page_config(page_title="About the Project", layout="wide")

st.title("📊 About the Project")

col1, col2 = st.columns([1, 1.5])


with col1:
    st.image("images/dataset-analysis.png", use_column_width=True)


with col2:
    # 🔹 Dataset Overview
    st.markdown("### 🧬 Dataset Overview")
    
    st.markdown("""
    - **Dataset Name**: CDC Diabetes Health Indicators  
    - **Source**: Centers for Disease Control and Prevention (CDC)  
    - **Total Instances**: `253,680`  
    - **Number of Features**: `21`  
    - **Feature Types**: Categorical, Integer  
    - **Target Variable**: `Diabetes_binary`  
        - `0` = No diabetes  
        - `1` = Pre-diabetes or diabetes  
    - **Purpose**: Understand the relationship between lifestyle factors and diabetes prevalence  
    """)
    
    # 🔹 Tools and Techniques Used
    st.markdown("---")
    st.markdown("### 🛠️ Tools and Techniques Used")
    
    st.markdown("""
    - **Language**: Python  
    - **ML Models Used**:  
      - AdaBoostClassifier  
      - LightGBM  
      - XGBoost  
    - **Feature Selection**:  
      - Chi-Square Test  
      - T-test  
      - L1-penalty Logistic Regression  
    - **Resampling Technique**:  
      - SMOTE-Tomek (balanced precision & recall)  
    - **Hyperparameter Tuning**:  
      - Optuna with Stratified K-Fold CV  
    - **Evaluation Metrics**:  
      - Accuracy, Precision, Recall, F1 Score  
      - Confusion Matrix  
    - **Interpretability**:  
      - SHAP Value Plots (Bar + Beeswarm)  
    - **Web App Framework**:  
      - Streamlit (multi-page + custom styling)  
    """)

# 🔹 Navigation
st.markdown("---")
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🧪 Try the Diabetes Prediction Tool"):
        st.switch_page("pages/3_Predict_Diabetes.py")

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