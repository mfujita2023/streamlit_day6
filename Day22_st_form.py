import streamlit as st

st.title('st.form')

#with表記の使用例　パターン1完全なやつ

st.header('1.Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    #入力欄
    coffee_bean_val = st.selectbox('Coffee bean',['Arabica','Robsta'])
    cofeen_roast_val = st.selectbox('Coffee roast',['Light','Medium','Dark'])
    brewing_val = st.selectbox('Brewing method',['Aeropress','Drip','French press','Moka pot','Siphon'])
    serving_type_val = st.selectbox('Serving format',['Hot','Iced','Frappe'])
    milk_val = st.select_slider('Milk intensity',['None','Low','Medium','High'])
    owncap_val = st.checkbox('Bring own cup')

    #フォームには送信ボタンが必要
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
                ☕ You have ordered::
                - Coffee bean: `{coffee_bean_val}`
                - Coffee roast:`{cofeen_roast_val}`
                - Brewing: `{brewing_val}`
                - Serving type: `{serving_type_val}`
                - Milk: `{milk_val}`
                - Bring own cup:`{owncap_val}`
                ''')
else:
    st.write('☝️Place youre order !')


#オブジェクトを使用した短い例
st.header('2.Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a Value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)