import os
from openai import OpenAI
import streamlit as st


openai_api_key = os.getenv("OPENAI_API_KEY")


def generate_marp_markdown(presentation_details):
    st.toast("Extracting Key Points..")
    client = OpenAI(api_key=openai_api_key)

    prompt = (
        f"Create a Marp slide markdown with the main key points for the following presentation:\n\n"
        f"Presentation Details:\n{presentation_details}\n\n"
        f"Markdown format with Marp slide headers and bullet points:"
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""You are an expert writing assistant and you excel at making good slides for presentations. You are given some some notes about a topic on which we want to make a presentation. We are using Marp which can generate slides from markdown. Based on the notes given to you, extract key points and create slides. Don't add much content in any slide. Keep it simple and easy to read. Create the final output in markdown format which can be parsed by the Marp CLI. It supports all markdown content. The slides are separated from each other using three dashes(---) with newlines before and after. Output only in markdown, I will parse it directly.
                
\n\nHere are the Notes\n
-----------------
{prompt}\n\n\n
----------------

Additional Instructions:
1. Don't make up extra things other than what is already given to you in the notes. 
2. Keep each slide simple and easy to read with only minmal content unless necessary.
3. Each slide should not contain more than 5 points. if there are more than 5, then split them evenly into multiple slides.
4. If you are continuing points on the next slide, then give same title as previous with (Contd.) being added.
5. Keep readabiliy in mind while making markdown
6. The first slide should be a title slide. Don't add --- on top of the title slide
7. You can add all types of markdown formatting like italics, bold etc when necessary
8. You can add as many slides as you want.
9. Add comments in the markdown to add pagenumbers
10. Prefer to use numbered list over bulletted unordered list when applicable
""",
            }
        ],
        model="gpt-3.5-turbo-16k",
        temperature=0.2,
        timeout=60,
    )
    markdown = chat_completion.choices[0].message.content.strip()
    return markdown
