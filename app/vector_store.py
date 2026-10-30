import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))
PERSIST_DIRECTORY = "./chroma_data"

# Use a lightweight, local HuggingFace embedding model (runs completely offline)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_vector_store():
    """Initialize or connect to the local ChromaDB vector store."""
    return Chroma(
        collection_name="cold_chain_compliance",
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

def ingest_compliance_manuals():
    """Seed standard cold-chain operating procedures and compliance rules into ChromaDB."""
    vector_store = get_vector_store()
    
    # Sample FDE logistics compliance documents
    docs = [
        "Protocol VAX-01: Pfizer and mRNA vaccines must strictly remain between 2°C and 8°C at all times. If temperatures exceed 8°C for more than 30 minutes, quarantine the batch immediately and notify the quality assurance lead.",
        "Protocol FRU-02: Organic strawberries and delicate fresh produce tolerate a range of 4°C to 12°C. Temperatures above 12°C risk rapid fungal growth and decay; inspect for surface moisture and shorten distribution timelines.",
        "General Incident Response: Any telemetry anomaly flag (anomaly_flag = 1) requires immediate driver notification, GPS coordinate logging, and a mandatory root-cause analysis report within 2 hours of excursion detection."
    ]
    
    # Clear existing or add new
    vector_store.add_texts(docs)
    print("Compliance manuals successfully embedded and stored in ChromaDB!")

if __name__ == "__main__":
    ingest_compliance_manuals()