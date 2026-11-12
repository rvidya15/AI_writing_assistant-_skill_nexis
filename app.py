import streamlit as st
import os

from dotenv import load_dotenv
from prompts import PROMPTS

from ai_engine import (
    generate_openai,
    generate_gemini
)

load_dotenv()

# Page configuration

st.set_page_config(
    page_title="AI Writing Assistant",
    page_icon="✍️",
    layout="wide"
)
# Load custom CSS

def load_css():
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )

load_css()

# Application heading

st.html("""
<div style="padding: 30px 0 25px 0;">

    <div style="
        color: #a78bfa;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 3px;
        margin-bottom: 12px;
    ">
        ✦ YOUR INTELLIGENT WRITING WORKSPACE
    </div>

    <h1 style="
        font-family: 'Space Grotesk', sans-serif;
        font-size: 46px;
        font-weight: 800;
        margin: 0;
        background: linear-gradient(
            90deg, #ffffff, #a78bfa, #60a5fa
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    ">
        AI Writing Assistant
    </h1>

    <p style="
        color: #9da5c0;
        font-size: 16px;
        margin-top: 12px;
    ">
        Turn your ideas into exceptional content.
        Write smarter. Create faster.
    </p>

</div>
""")

st.divider()


# Sidebar settings

st.sidebar.header("AI Model Settings")

provider = st.sidebar.selectbox(
    "Choose AI Provider",
    ["Gemini", "OpenAI"]
)

if provider == "Gemini":

    api_key = st.sidebar.text_input(
        "Gemini API Key",
        value=os.getenv("GEMINI_API_KEY", ""),
        type="password"
    )

    model = st.sidebar.selectbox(
        "Choose Model",
    [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite"
    ]
)


else:

    api_key = st.sidebar.text_input(
        "OpenAI API Key",
        value=os.getenv("OPENAI_API_KEY", ""),
        type="password"
    )

    model = st.sidebar.selectbox(
        "Choose Model",
        ["gpt-4.1-mini", "gpt-4.1"]
    )


temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1
)

max_tokens = st.sidebar.slider(
    "Maximum output tokens",
    min_value=256,
    max_value=8192,
    value=2048,
    step=256
)

# Main interface

st.header("Create Your Content")

task = st.selectbox(
    "Select Writing Task",
    list(PROMPTS.keys())
)

content = st.text_area(
    "Enter your topic, instructions or code",
    placeholder="Enter your content here...",
    height=200
)

col1, col2 = st.columns(2)

with col1:

    tone = st.selectbox(
        "Choose Tone",
        [
            "Professional",
            "Friendly",
            "Creative",
            "Academic",
            "Simple",
            "Persuasive"
        ]
    )

with col2:

    length = st.selectbox(
        "Choose Length",
        [
            "Short",
            "Medium",
            "Detailed"
        ]
    )

formatting = st.selectbox(
    "Output Formatting",
    [
        "Markdown",
        "Plain Text"
    ]
)

# Generate button

if st.button("✨ Generate Content", type="primary"):

    if not api_key.strip():

        st.error("Please enter your API key.")

    elif not content.strip():

        st.warning("Please enter some content.")

    else:

        prompt = PROMPTS[task].format(
            content=content,
            tone=tone,
            length=length
        )

        if formatting == "Plain Text":
            prompt += "\nReturn plain text without Markdown formatting."

        try:

            with st.spinner("AI is writing your content..."):

                if provider == "Gemini":

                    result = generate_gemini(
                        prompt,
                        api_key,
                        temperature,
                        model,
                        max_tokens
                    )

                else:

                    result = generate_openai(
                        prompt,
                        api_key,
                        temperature,
                        model,
                        max_tokens
                    )

            if not result.strip():
                st.warning("The model returned an empty response.")

            else:

                st.session_state["generated_content"] = result

                st.success("Content generated successfully!")

        except Exception as error:

            st.error(f"Something went wrong: {error}")

# Display output

if "generated_content" in st.session_state:

    st.divider()

    st.header("Generated Content")

    st.markdown(st.session_state["generated_content"])

    st.download_button(
        label="⬇️ Download Content",
        data=st.session_state["generated_content"],
        file_name="AI_generated_content.md",
        mime="text/markdown"
    )

    if st.button("Clear Output"):

        del st.session_state["generated_content"]

        st.rerun()