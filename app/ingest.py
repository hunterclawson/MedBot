import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 

# Define paths dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/")  # Adjust the path relative to the current script
DB_FAISS_PATH = os.path.join(BASE_DIR, "../vectorstore/db_faiss")  # Ensure the vectorstore path is correct

# Create vector database
def create_vector_db():
    loader = DirectoryLoader(DATA_PATH,
                             glob='*.txt',
                             loader_cls=TextLoader,
                             loader_kwargs={'autodetect_encoding': True})

    # Check if data directory exists
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Data directory not found: {DATA_PATH}")

    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512,
                                                   chunk_overlap=256)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    db = FAISS.from_documents(texts, embeddings)
    os.makedirs(os.path.dirname(DB_FAISS_PATH), exist_ok=True)  # Ensure the directory exists
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    create_vector_db()
