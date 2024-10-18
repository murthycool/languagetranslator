#pip install streamlit 
# Define the function to perform calculations based on user input
import streamlit as st
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part

# Set up the Streamlit app
st.title("Language Translator")
trans,summ,sent=st.columns(3)
languages = ["English", "French", "Spanish", "German", "Chinese", "Japanese","Portuguese","Russian"]

# Input box for text
text_input = st.text_area("Enter text to translate:")

# Dropdown for language selection
from_language = st.selectbox("From Language", languages)
to_language = st.selectbox("To Language", languages)

def translate_text(text, from_language, to_language):
    """Translates text using Gemini.

    Args:
        text (str): The text to be translated.
        from_language (str): The language code of the original text.
        to_language (str): The language code to translate to.

    Returns:
        str: The translated text.
    """
    vertexai.init(project="devopshcl", location="us-central1")
    model = GenerativeModel("gemini-1.5-flash-001",)
    translation_prompt = f"Translate the following text from {from_language} to {to_language}:\n{text}"
    #translation = llm(translation_prompt)
    generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,}
    responses = model.generate_content(
        [translation_prompt],
        generation_config=generation_config,
        stream=True,
    )
    translated_text=''
    for response in responses:
        translated_text+=response.text
    return translated_text

# Button to trigger translation
with trans:
    if st.button("Translate"):
        if text_input:
            # Translate the text
            translated_text = translate_text(text_input, from_language.lower(), to_language.lower())
            st.success(translated_text)
        else:
            st.warning("Please enter text to translate.")
with summ:
    if st.button("Summary"):
        if text_input:
            # Translate the text
            translated_text = translate_text(text_input, from_language.lower(), to_language.lower())
            st.success(translated_text)
        else:
            st.warning("Please enter text to translate.")
with sent:
    if st.button("Sentiment"):
        if text_input:
            # Translate the text
            translated_text = translate_text(text_input, from_language.lower(), to_language.lower())
            st.success(translated_text)
        else:
            st.warning("Please enter text to translate.")
