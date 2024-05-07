from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
import requests
import os
import streamlit as st
from corpus_loader import load_corpus
from vector_store import load_vector_store

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# img2text
def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)[0]["generated_text"]
    print(text)
    return text

# llm
def generate_story(scenario, qa):
    result = qa.run(scenario)
    print(result)
    return result

# text to speech
def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payloads = {
        "inputs": message
    }
    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)

def main():
    st.set_page_config(page_title="img 2 audio story", page_icon="🤖")
    st.header("Turn your image into an audio story")

    # Load the vector store
    corpus_dir = os.getcwd()  # Get the current working directory
    persist_dir = os.path.join(corpus_dir, "vector_store")  # Create a 'vector_store' directory in the current directory
    os.makedirs(persist_dir, exist_ok=True)  # Create the 'vector_store' directory if it doesn't exist

    corpus = load_corpus(corpus_dir)
    vector_store = load_vector_store(persist_dir)

    # Create the RetrievalQA chain
    llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        print(uploaded_file)
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)

        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        scenario = img2text(uploaded_file.name)
        story = generate_story(scenario, qa)
        text2speech(story)

        with st.expander("Scenario:"):
            st.write(scenario)
        with st.expander("Story:"):
            st.write(story)
        st.audio("audio.flac")

if __name__ == '__main__':
    main()