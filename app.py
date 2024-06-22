import streamlit as st
import subprocess
import os

from utils.generateUtils import (
    generate_slides,
    generate_pdf,
    generate_pptx,
    generate_marp_header,
)


# Streamlit app layout
st.set_page_config(page_title="Markdown to Slides Previewer", layout="wide")
st.title("Markdown to Slides Previewer")

st.sidebar.title("Customization")
theme = st.sidebar.selectbox("Theme", ["default", "gaia", "uncover"])
paginate = st.sidebar.checkbox("Paginate", True)
size = st.sidebar.selectbox("Presentation Size", ["4:3", "16:9"], index=0)
color_scheme = st.sidebar.selectbox("Color Scheme", ["Default", "invert"], index=0)
footer = st.sidebar.text_input("Footer", "[@yourname](https://example.com)")


project_details = st.text_area("Enter details about your presentations", height=300)

if project_details.strip() != "":
    st.title("Project Details")
    col1, col2 = st.columns(2)
    with col1:
        markdown_input = st.text_area("Enter your Markdown for slides:", height=600)

    with col2:
        st.header("Slide Preview")
        # if st.button("Generate Preview"):
        if True:
            if markdown_input.strip() != "":
                marp_header = generate_marp_header(
                    theme, paginate, size, footer, color_scheme
                )
                html_output = generate_slides(markdown_input, marp_header)
                st.components.v1.html(html_output, height=500, scrolling=True)
            else:
                st.warning("Please enter some Markdown to generate slides.")

if st.button("Generate PDF"):
    if markdown_input.strip() != "":
        generate_pdf(markdown_input)
        with open("slides.pdf", "rb") as file:
            st.text("PDF generated")
            st.download_button(
                label="Download PDF",
                data=file,
                file_name="slides.pdf",
                mime="application/pdf",
            )
    else:
        st.warning("Please enter some Markdown to generate slides.")
if st.button("Generate as PPTX"):
    if markdown_input.strip() != "":
        generate_pptx(markdown_input)
        with open("slides.pptx", "rb") as file:
            st.text("Slides generated")
            st.download_button(
                label="Download PPTX",
                data=file,
                file_name="slides.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            )
    else:
        st.warning("Please enter some Markdown to generate slides.")
