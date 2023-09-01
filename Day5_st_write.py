import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

#例1 文字形式

st.write('Hello, *World!* :sunglasses:')

#例2 数値形式
st.write(1234)

#例3 複数行リスト 配列設定
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

st.write(df)

# 例4 複数行リスト＋注釈をwriteする
st.write('Below is a Dataframe:',df,'Above is a dataframe')

#例5
df2 = pd.DataFrame(
   np.random.randn(200,3),
   columns = ['a','b','c'] 
)

#マークcircle→散布図を書こう
c= alt.Chart(df2).mark_circle().encode(
    x='a', y = 'b', size = 'c', color = 'c', tooltip=(['a','b','c'])
)
st.write(c)