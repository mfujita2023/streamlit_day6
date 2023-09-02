import streamlit as st

#ヘッダ行の指定
st.header('st.multiselect')

options = st.multiselect(
    'What are your favorite colors',
    ['Green','Yellow','Red','Blue'],
    ['Yellow','Red']
)

st.write('You selected:', options)