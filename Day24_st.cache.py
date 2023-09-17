import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

#キャッシュを使用する
a0 = time()
st.subheader=('Using st.cache')

#ここでキャッシュを定義している
#@st.cache(suppress_st_warning=True)
@st.cache_data
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(200000,5),
        columns=['a','b','c','d','e']
    )
    return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

#キャッシュを使用しない
b0 = time()
st.subheader=('Not using st.cache')

def load_data_b():
    df = pd.DataFrame(
        np.random.rand(200000,5),
        columns=['a','b','c','d','e']
    )
    return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)