import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg", width=250)

with col2:
    st.title("Mihir Patil")
    content = """
    Mihir Patil is a highly skilled Automation Engineering Technician 
    and Electrical Engineer with experience in optimizing operational 
    efficiency through innovative PCB design. He holds a Master’s 
    degree in Electrical and Information Engineering from 
    Hochschule Wismar, Germany, and a Bachelor's in Electrical 
    Engineering from Gujarat Technical University. Mihir's expertise 
    spans automation systems, circuit design, machine learning, and 
    data engineering. His technical proficiencies include Python, C++,
     deep learning frameworks such as TensorFlow and PyTorch, and 
     database management with MySQL and PostgreSQL. He has developed 
     multiple technical projects, including a movie recommendation 
     system and an automatic door system using Arduino. Fluent in 
     English (C1) and German (B1), Mihir combines strong technical 
     knowledge with problem-solving and critical thinking skills.
    """
    st.info(content)
