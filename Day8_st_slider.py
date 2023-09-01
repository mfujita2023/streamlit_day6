import streamlit as st
from datetime import time, datetime

st.header('st.slider')

#例1
#スライダーで年齢位置を指定(0～130まで デフォルトは3つ目のパラメータの25)
st.subheader=('Slider')
age = st.slider('How old are you?',0,130,25)
st.write("I'm",age,'years old')

#例2
#スライダーで小数点以下の定義も可能　デフォルト範囲指定
st.subheader=('Range slider')
values = st.slider(
    'Select a range of values',
    0.0, 100.0,(25.0,75.0))

st.write('Values:',values)

#例3
#時間のスライダーの設定　デフォルトが11時半～12時45分

st.subheader=('Range time slider')

appointment = st.slider(
   "Schedule your appointment:",
   value = (time(11,30),time(12,45)) 
)

st.write("You're scheduled for:",appointment)

#例4
st.subheader=('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value = datetime(2020,1,1,9,30),
    format = "YYYY/MM/DD-hh:mm")

st.write("Start time:",start_time)
