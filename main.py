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
🌟 Welcome to My Coding Journey!\n
Hi, I’m Mihir Patil—a Software Developer and Automation Engineer with a knack for turning ideas into functional, elegant solutions. Passionate about Python, I build tools that simplify workflows, automate tasks, and solve real-world problems. From AI-driven web apps to smart automation scripts, my projects blend creativity with technical precision.\n\n

Here’s a glimpse of what I’ve crafted:\n\n

🚀 Productivity Boosters: Todo apps, PDF generators, and systems that manage data seamlessly.\n\n

🤖 Smart Automation: Tools that scrape websites, detect motion, or notify you about concert tours.\n\n

🌐 Web Solutions: Full-stack apps for restaurants, portfolios, and even a positive news hub powered by sentiment analysis.\n\n

Let’s build something impactful! Whether you’re here to explore my work or discuss a collaboration, I’m just a message away.\n\n

📩 Get in touch—I’d love to connect!
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
