import streamlit as st
from utils.aiUtils import generate_marp_markdown
from utils.generateUtils import (
    generate_slides,
    generate_pdf,
    generate_pptx,
    generate_marp_header,
)


# Initialize session state variables
def init_session_state():
    if "skip_project_details" not in st.session_state:
        st.session_state.skip_project_details = False
    if "project_details" not in st.session_state:
        st.session_state.project_details = ""
    if "generated_markdown" not in st.session_state:
        st.session_state.generated_markdown = ""
    if "theme" not in st.session_state:
        st.session_state.theme = "default"
    if "paginate" not in st.session_state:
        st.session_state.paginate = True
    if "size" not in st.session_state:
        st.session_state.size = "4:3"
    if "color_scheme" not in st.session_state:
        st.session_state.color_scheme = "Default"
    if "footer" not in st.session_state:
        st.session_state.footer = "[@yourname](https://example.com)"


# Callback functions for input changes
def update_project_details():
    st.session_state.generated_markdown = ""


def generate_markdown():
    if st.session_state.project_details:
        st.session_state.generated_markdown = generate_marp_markdown(
            st.session_state.project_details
        )
    else:
        st.session_state.skip_project_details = True


def main():
    st.set_page_config(page_title="Markdown to Slides Generator", layout="wide")
    init_session_state()

    st.title("Markdown to Slides Generator")

    with st.sidebar:
        st.title("Customization")
        st.session_state.theme = st.selectbox("Theme", ["default", "gaia", "uncover"])
        st.session_state.paginate = st.checkbox("Paginate", st.session_state.paginate)
        st.session_state.size = st.selectbox(
            "Presentation Size", ["4:3", "16:9"], index=0
        )
        st.session_state.color_scheme = st.selectbox(
            "Color Scheme", ["Default", "invert"], index=0
        )
        st.session_state.footer = st.text_input("Footer", st.session_state.footer)

    # Main content
    st.text_area(
        "Enter details about your presentations",
        key="project_details",
        height=300,
        on_change=update_project_details,
    )

    if st.button("Generate Markdown"):
        generate_markdown()

    if st.session_state.project_details or st.session_state.skip_project_details:
        st.title("Project Details")
        col1, col2 = st.columns(2)

        with col1:
            markdown_input = st.text_area(
                "Enter your Markdown for slides:",
                value=st.session_state.generated_markdown,
                height=600,
                key="markdown_input",
            )

        with col2:
            st.header("Slide Preview")
            if markdown_input.strip():
                marp_header = generate_marp_header(
                    st.session_state.theme,
                    st.session_state.paginate,
                    st.session_state.size,
                    st.session_state.footer,
                    st.session_state.color_scheme,
                )
                html_output = generate_slides(markdown_input, marp_header)
                st.components.v1.html(html_output, height=500, scrolling=True)
            else:
                st.warning("Please enter some Markdown to generate slides.")

        # Generate PDF and PPTX buttons
        col3, col4 = st.columns(2)
        with col3:
            if st.button("Generate PDF"):
                if markdown_input.strip():
                    pdf_data = generate_pdf(markdown_input)
                    st.download_button(
                        label="Download PDF",
                        data=pdf_data,
                        file_name="slides.pdf",
                        mime="application/pdf",
                    )
                else:
                    st.warning("Please enter Markdown to generate PDF.")

        with col4:
            if st.button("Generate as PPTX"):
                if markdown_input.strip():
                    pptx_data = generate_pptx(markdown_input)
                    st.download_button(
                        label="Download PPTX",
                        data=pptx_data,
                        file_name="slides.pptx",
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    )
                else:
                    st.warning("Please enter Markdown to generate Powerpoint")


if __name__ == "__main__":
    main()
