import streamlit as st
import subprocess
import os


# Function to generate HTML slides using Marp CLI
def generate_slides(markdown_text):
    with open("slides.md", "w") as f:
        f.write(markdown_text)
    subprocess.run(["marp", "--html", "slides.md", "-o", "slides.html"])
    with open("slides.html", "r") as f:
        return f.read()


# Streamlit app layout
st.set_page_config(layout="wide")
st.title("Markdown to Slides Previewer")

# Left column for Markdown input
markdown_input = st.text_area("Enter your Markdown for slides:", height=300)

# Right column for slide preview
col1, col2 = st.columns(2)
with col1:
    st.header("Markdown Input")
    st.write(markdown_input)

with col2:
    st.header("Slide Preview")
    if st.button("Generate Preview"):
        if markdown_input.strip() != "":
            html_output = generate_slides(markdown_input)
            st.components.v1.html(html_output, height=500, scrolling=True)
        else:
            st.warning("Please enter some Markdown to generate slides.")
