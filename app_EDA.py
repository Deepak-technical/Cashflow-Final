from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai.llm.google_palm import GooglePalm
from pandasai import SmartDataframe
import numpy as np

import matplotlib
matplotlib.use('Tkagg')
load_dotenv()
API_KEY="        "

llm=GooglePalm(api_key='AIzaSyBQYaEA9LQrVKc_k-IbCbjnGnxnxpL7P0U')


st.title("Prompt-driven analysis of data")
uploaded_file=st.file_uploader("Upload a csv file for analysis",type=['csv'])

if uploaded_file is not None:
    df1=pd.read_csv(uploaded_file)
    st.write(df1.head(5))
    prompt=st.text_area("Enter your Query")
    df = SmartDataframe(df1, config={"llm": llm})

    if st.button("Generate"):
        if prompt:
            # st.write("PandasAI is generating your response ..")
            with st.spinner("Generating response..."):
                 st.write(df.chat(prompt))
        else:
            st.warning("please enter a prompt")    