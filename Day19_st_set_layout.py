import streamlit as st

st.set_page_config(layout="wide")

#タイトル
st.title('How to layout your Streamlit app')

#About this appをクリックしたら注釈が下に出てくる
with st.expander('About this app'):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

#左のサイドバー
st.sidebar.header('Input')
user_name=st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji',['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is you favorite food',['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1,col2,col3= st.columns(3)

#１列目
with col1:
    if user_name !='':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈Please enter your  **name**!')


#2列目
with col2:
    if user_emoji != '':
        st.write(f'{user_emoji} is your favorite **emoji**!')
    
    else:
        st.write('👈Please choose an **emoji**!')

#3列目
with col3:
    if user_food !='':
        st.write(f'🍴 **{user_food}** is your favorite **food**!')
    else:
        st.write('👈 Please choose your favorite **food**!')