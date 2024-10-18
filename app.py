#pip install streamlit 
# Define the function to perform calculations based on user input
import streamlit as st
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part

# Set up the Streamlit app
st.title("Language Translator")

languages = ["English", "French", "Spanish", "German", "Chinese", "Japanese","Portuguese","Russian"]

# Input box for text
text_input = st.text_area("Enter text to translate:")

# Dropdown for language selection
from_language = st.selectbox("From Language", languages)
to_language = st.selectbox("To Language", languages)
ouput_placeholder=st.empty()
trans,summ,sent=st.columns(3)
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
    model = GenerativeModel("gemini-1.5-pro-001",)
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

def summary_text(text):
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
    prompt='''
    Please Summarize the below text with Not more than 50 Words
    The Summary should be in Pure British English
    Focus on Lidl/Kaufland/Schwarz Group
    Should be Short, Precise & to the point
    You should concentrate more on Context, Numerical Values & Noun when you give Summarized output

    '''
    translation_prompt = f"{prompt}:\n{text}"
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
    summary_text=''
    for response in responses:
        summary_text+=response.text
    return summary_text
def sent_text(text):
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
    prompt='''
    Please give the sentiment of the below text. It should be either Positive/Negative/Neutral
    The response should be crisp - do not give any explinations

    '''
    translation_prompt = f"{prompt}:\n{text}"
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
    sent_text=''
    for response in responses:
        sent_text+=response.text
    return sent_text
global translated_text
translated_text = ''
# Button to trigger translation
with trans:
    if st.button("Translate"):
        if text_input:
            # Translate the text
            global translated_text
            translated_text = translate_text(text_input, from_language.lower(), to_language.lower())
            ouput_placeholder.write(translated_text)
        else:
            st.warning("Please enter text to translate.")
with summ:
    if st.button("Summary"):
        if translated_text:
            # Summary of Text
            
            summary_text = summary_text(translated_text)
            ouput_placeholder.write(summary_text)
        else:
            st.warning("Please enter text to translate & then get the Summary")
with sent:
    if st.button("Sentiment"):
        if translated_text:
            # Translate the text
            sentiment_text=sent_text(translated_text)
            ouput_placeholder.write(sentiment_text)
        else:
            st.warning("Please enter text to translate & then get the Sentiment")
