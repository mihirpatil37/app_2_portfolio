import streamlit as st
from Send_Emails import send_email
st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address: ")
    raw_message = st.text_area("Write your message to us.")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        print(button)
        send_email(message)
        st.info("Your email was sent successfully.")
