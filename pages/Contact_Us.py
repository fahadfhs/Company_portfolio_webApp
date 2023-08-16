import pandas as pd
import streamlit as st
from send_email import send_email

# We create a dataframe from the csv file first
df = pd.read_csv("topics.csv")
# we take the "topic" column values and store it under options
options = df["topic"].tolist()

with st.form(key="email_forms"):
    user_email = st.text_input("Please enter your email address below:")

    st.write("What topic do you want to discuss?")
    # here the select box uses the values stored as list above to be displayed in the form
    topic = st.selectbox("Select a topic", options)
    raw_message = st.text_area("Text")

    message = f"""\
Subject: New email from {user_email}

From:{user_email}
Topic:{topic}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")

