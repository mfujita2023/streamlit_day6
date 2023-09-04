import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the ` .streamlit/config.toml` file of this app')

st.code("""
        [theme]
        primarycolor = "#F39C12"
        backgroundcolor = "#2E86C1"
        secondaryBackgroundcolor = "#AED6F1"
        textcolor ="#FFFFFF"
        font = "monospace"
        """)

number = st.sidebar.slider('Select a number:',0,10,5)
st.write('Selected number from slider widget is:', number )