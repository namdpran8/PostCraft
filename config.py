import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

def load_api():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key and "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY was not found. Set it in your environment, .env file, or Streamlit secrets."
        )
    
    return api_key


def configure_api():
    api_key = load_api()
    genai.configure(api_key=api_key)


def get_model():
    configure_api()
    gemini_model = "gemini-2.5-flash"
    model = genai.GenerativeModel(gemini_model)

    return model


if __name__ == "__main__":
    get_model()
    resp = get_model().generate_content("What is capital of India?")
    print(resp.text)