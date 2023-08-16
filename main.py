import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("Techno Genius Solutions")

maincontent = """ Welcome to TechnoGenius Solutions! At TechnoGenius, we're on a mission to redefine the future 
through cutting-edge technology. Our team of innovators and experts is dedicated to developing groundbreaking software
solutions that transform industries and empower businesses worldwide. Join us as we pave the way for a smarter, 
more connected tomorrow."""

st.write(maincontent)

st.subheader("Our Team")


col1, col_a, col2, col_b,col3 = st.columns([2.0, 0.5, 2.0, 0.5, 2.0])
df = pd.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("Images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("Images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("Images/" + row["image"])
