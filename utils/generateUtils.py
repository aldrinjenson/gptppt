import streamlit as st
import subprocess
import os
from time import time, sleep


# Function to generate Marp Markdown header based on user inputs
def generate_marp_header(theme, paginate, size, footer, color_scheme):
    header = f"""---
theme: {theme}
paginate: {paginate}
size: {size}
footer: "{footer}"
class: "{color_scheme}"
---"""
    return header


def generate_slides(markdown):
    # st.toast("Generating Preview...", icon="🚀")
    with open("slides.md", "w") as f:
        f.write(markdown)
    subprocess.run(["marp", "--html", "slides.md", "-o", "slides.html"])
    with open("slides.html", "r") as f:
        return f.read()


def generate_pdf(markdown_text):
    st.toast("Generating PDF...", icon="🚀")
    if os.path.exists("slides.pdf"):
        os.remove("slides.pdf")
    with open("slides.md", "w") as f:
        f.write(markdown_text)
    print("before marp")
    subprocess.run(["marp", "--pdf", "slides.md", "-o", "slides.pdf"])
    print('after marp')
    with open("slides.pdf", "rb") as file:
        print('inside with')
        pdf_data = file.read()
    return pdf_data


def generate_pptx(markdown_text):
    st.toast("Generating Powerpoint file...", icon="🚀")
    if os.path.exists("slides.pptx"):
        os.remove("slides.pptx")
    with open("slides.md", "w") as f:
        f.write(markdown_text)
    subprocess.run(["marp", "--pptx", "slides.md", "-o", "slides.pptx"])
    with open("slides.pptx", "rb") as file:
        pptx_data = file.read()
    return pptx_data
