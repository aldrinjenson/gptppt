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
        st.session_state.size = "16:9"
    if "color_scheme" not in st.session_state:
        st.session_state.color_scheme = "Default"
    if "yaml_markdown" not in st.session_state:
        st.session_state.yaml_markdown = ""
    if "footer" not in st.session_state:
        st.session_state.footer = "Created with GPTPPT | [Buy me a coffee](https://www.buymeacoffee.com/aldrinjenson)"


# Callback functions for input changes
def update_project_details():
    st.session_state.generated_markdown = ""


def generate_markdown():
    if st.session_state.project_details:
        with st.spinner("Generating presentation outline..."):
            st.session_state.generated_markdown = generate_marp_markdown(
                st.session_state.project_details
            )
    else:
        st.session_state.skip_project_details = True


def get_markdown_with_header_yaml(markdown_text):
    marp_header = generate_marp_header(
        st.session_state.theme,
        st.session_state.paginate,
        st.session_state.size,
        st.session_state.footer,
        st.session_state.color_scheme,
    )
    return marp_header + "\n\n" + markdown_text


def main():
    st.set_page_config(
        page_title="GPTPPT - Notes to Slides Generator",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    init_session_state()

    st.title("GPTPPT: Notes to Slides Generator ✨")
    st.write(
        "Transform your notes into professional, minimalistic presentations with AI!"
    )

    with st.sidebar:
        st.title("Customization")
        st.session_state.theme = st.selectbox("Theme", ["default", "gaia", "uncover"])
        st.session_state.paginate = st.checkbox("Paginate", st.session_state.paginate)
        st.session_state.size = st.selectbox(
            "Presentation Size", ["16:9", "4:3"], index=0
        )
        st.session_state.color_scheme = st.selectbox(
            "Color Scheme", ["Default", "invert"], index=0
        )
        st.session_state.footer = st.text_input("Footer", st.session_state.footer)

        st.markdown("---")
        st.markdown(
            """
            <div style="text-align: center;">
                <p>Think this is useful?</p>
                <a href="https://www.buymeacoffee.com/aldrinjenson" target="_blank">
                    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" >
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Main content
    st.text_area(
        "Enter your notes or presentation details",
        key="project_details",
        height=200,
        on_change=update_project_details,
        placeholder="Ex. Here are my notes on AquaPuncture. This is to be shown and told to young students of medicine....",
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Generate Presentation", type="primary"):
            generate_markdown()
    with col2:
        st.download_button(
            label="Download Example Notes",
            data="Example notes content...",  # Replace with actual example notes
            file_name="example_notes.txt",
            mime="text/plain",
        )

    if st.session_state.project_details or st.session_state.skip_project_details:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Presentation Outline")
            markdown_input = st.text_area(
                "Edit Markdown for slides:",
                value=st.session_state.generated_markdown,
                height=500,
                key="markdown_input",
            )

        with col2:
            st.subheader("Slide Preview")
            st.write("Auto preview based on the markdown entered")
            if markdown_input.strip():
                with st.spinner("Generating preview..."):
                    markdown_with_header_yaml = get_markdown_with_header_yaml(
                        markdown_input
                    )
                    st.session_state.yaml_markdown = markdown_with_header_yaml
                    html_output = generate_slides(st.session_state.yaml_markdown)
                    st.components.v1.html(html_output, height=470, scrolling=True)
            else:
                st.info("Enter some Markdown to preview slides.")

        col3, col4 = st.columns(2)

        with col3:
            if st.button("Generate PDF", type="primary"):
                if markdown_input.strip():
                    with st.spinner("Generating PDF..."):
                        pdf_data = generate_pdf(st.session_state.yaml_markdown)
                        st.download_button(
                            label="Download PDF",
                            data=pdf_data,
                            file_name="gptppt_presentation.pdf",
                            mime="application/pdf",
                        )
                else:
                    st.warning("Please enter Markdown to generate PDF.")

        with col4:
            if st.button("Generate PPTX", type="primary"):
                if markdown_input.strip():
                    with st.spinner("Generating PPTX..."):
                        pptx_data = generate_pptx(st.session_state.yaml_markdown)
                        st.download_button(
                            label="Download PPTX",
                            data=pptx_data,
                            file_name="gptppt_presentation.pptx",
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                        )
                else:
                    st.warning("Please enter Markdown to generate PowerPoint.")

    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center;">
            <p>Made with ❤️ by <a href="https://linkedin.com/in/aldrinjenson" target="_blank">Aldrin Jenson</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
