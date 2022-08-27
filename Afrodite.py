import streamlit as st

st.title('importacao')
st.file_uploader('uploader')
btn = st.button('click')
if btn:
    import Hefesto
