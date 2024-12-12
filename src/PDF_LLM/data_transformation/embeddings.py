from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_embeddings(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(text_chunks, embeddings)
    return vectorstore
