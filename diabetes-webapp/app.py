#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 12:24:44 2025

@author: namithabhaskar
"""

import streamlit as st

st.set_page_config(page_title="GlucoBot - A Modern Diabetes App", layout="centered")

# Title and tagline
st.markdown("""
<h1 style='text-align: center; color: #333;'> <a href="#" style='text-decoration:none; color:#1976D2;'>GlucoBot</a> </h1>
<h4 style='text-align: center;'>A virtual screening assistant for diabetes</h4>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Image section
st.image("images/diabetes_img.webp", use_column_width=True)


st.markdown("<br><br>", unsafe_allow_html=True)

# Button layout
col1, col2, col3 = st.columns([1.5, 1.5, 1.5], gap="large")

with col1:
    
    st.markdown("""
        <style>
        div.stButton > button {
            height: 100px;
            width: 100%;
            font-size: 20px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if st.button("**🩺 What is Diabetes ?**"):
        st.switch_page("pages/1_About_Diabetes.py")

with col2:
    
    st.markdown("""
        <style>
        div.stButton > button {
            height: 100px;
            width: 100%;
            font-size: 20px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if st.button("**📊 About this Project**"):
        st.switch_page("pages/2_Project_Description.py")

with col3:
    
    st.markdown("""
        <style>
        div.stButton > button {
            height: 100px;
            width: 100%;
            font-size: 20px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if st.button("**🧪 PREDICT !**"):
        st.switch_page("pages/3_Predict_Diabetes.py")

st.markdown("""
<hr style='border: 0.5px solid #ccc; margin-top: 50px;'>
<div style='text-align: center; color: grey; font-size: 14px;'>
    &copy; 2025 GlucoBot. Namitha Bhaskar. All rights reserved.
</div>
""", unsafe_allow_html=True)
