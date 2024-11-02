import streamlit as st

st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address: ")
    message = st.text_area("Write your message to us.")
    button = st.form_submit_button()

