from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vector_database(features, openai_api_key):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = FAISS.from_texts(features, embeddings)
    return db

# Usage
openai_api_key = 'your_openai_api_key'
vector_db = create_vector_database(features, openai_api_key)
