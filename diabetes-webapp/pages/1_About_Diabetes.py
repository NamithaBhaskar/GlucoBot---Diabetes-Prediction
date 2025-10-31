#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 12:26:33 2025

@author: namithabhaskar
"""

import streamlit as st

st.set_page_config(page_title="About Diabetes", layout="wide")

st.title("🩺 What is Diabetes?")

# ──────────────────────────────────────────────
# 🧭 Layout: Text Left | Image Right
col1, col2 = st.columns([1.6, 1])

with col1:
    st.markdown("""
    ### 🔍 Overview
    Diabetes is a chronic health condition that affects how your body turns food into energy. It occurs when your blood glucose (blood sugar) is too high due to insufficient insulin production or ineffective insulin use.

    There are **two main types**:
    - **Type 1 Diabetes** – usually diagnosed early in life; caused by autoimmune destruction of insulin-producing cells.
    - **Type 2 Diabetes** – more common and develops due to lifestyle factors, insulin resistance, or both.

    ---

    ### 📊 Global Impact
    - 🌍 Over **500 million** people worldwide live with diabetes.
    - 📈 Prevalence is increasing rapidly due to urbanization, sedentary lifestyles, and poor dietary habits.
    - 🧬 Genetics, age, and obesity significantly increase risk.

    ---

    ### ⚠️ Common Risk Factors
    - High BMI / Obesity
    - Family history of diabetes
    - Sedentary lifestyle
    - Poor diet
    - Age above 45
    - High blood pressure or cholesterol

    ---

    Diabetes can be managed and prevented with early detection, lifestyle changes, and regular medical support.
    """)

with col2:
    # Second image with spacing
    st.markdown("<div style='margin-top: 20px;'>", unsafe_allow_html=True)
    st.image("images/worldstats.jpeg", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # First image with alignment fix
    st.markdown("<div style='margin-top: -100px;'>", unsafe_allow_html=True)
    st.image("images/stats.jpeg", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)



st.markdown("<br>", unsafe_allow_html=True)
st.markdown("#### 👉 Want to see your risk?")

# Reduce the vertical space before buttons
st.markdown("<div style='margin-top: -100px;'>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🧪 Try the Diabetes Prediction Tool"):
        st.switch_page("pages/3_Predict_Diabetes.py")

with col2:
    if st.button("🔙 Back to Home"):
        st.switch_page("app.py")

# st.markdown("</div>", unsafe_allow_html=True)

# if st.button("🧪 Try the Diabetes Prediction Tool"):
#     st.switch_page("pages/3_PREDICT.py")

# # ──────────────────────────────────────────────
# # 🔙 Back to Home button
# st.markdown("<br>", unsafe_allow_html=True)
# if st.button("⬅️ Back to Home"):
#     st.switch_page("app.py")

# ──────────────────────────────────────────────
# 🔏 Footer
st.markdown("""
<hr style='border: 0.5px solid #ccc; margin-top: 50px;'>
<div style='text-align: center; color: grey; font-size: 14px;'>
    &copy; 2025 GlucoBot. Namitha Bhaskar. All rights reserved.
</div>
""", unsafe_allow_html=True)
