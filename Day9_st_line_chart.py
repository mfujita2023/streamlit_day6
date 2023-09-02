import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
C:/Users/madoka.fujita/Anaconda3/envs/stenv/python.exe -m streamlit run c:/mfujita/streamlit/Day9_st_line_chart.py    np.random.randn(20,3),
    columns=(['a','b','c'])
)
st.line_chart(chart_data)