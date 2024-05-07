from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

def create_vector_store(corpus, persist_dir):
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(corpus, embeddings, persist_directory=persist_dir)
    vector_store.persist()
    return vector_store

def load_vector_store(persist_dir):
    return Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())