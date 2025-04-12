import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.title("My portfolio website")
    st.image("images/photo.jpeg", width=300)

with col2:
    st.title("Mihir Patil")
    content = """
            I am Mihir Patil, an Automation Engineering Technician and Electrical 
            Engineer with a Master's in Electrical and Information Engineering from 
            Hochschule Wismar, Germany, and a Bachelor's from Gujarat Technical 
            University. I have experience in automation, circuit design, machine 
            learning, and data engineering, with expertise in Python, TensorFlow, 
            PyTorch, MySQL, and PostgreSQL. My projects include developing a movie 
            recommendation system and designing an automatic door system with Arduino. 
            Fluent in English (C1) and proficient in German (B1), I excel in 
            problem-solving, critical thinking, and project management.
            """
    st.info(content)
contact_content = "Below you can find some of the apps I have built in python. " \
              "Feel free to contact me!"
st.write(contact_content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:5].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[6:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
