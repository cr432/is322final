import os
import glob
from langchain.document_loaders import TextLoader

def load_corpus(corpus_dir):
    corpus = []
    for filename in glob.glob(os.path.join(corpus_dir, "*.txt")):
        loader = TextLoader(filename)
        docs = loader.load()
        corpus.extend(docs)
    return corpus