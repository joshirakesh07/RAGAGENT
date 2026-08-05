from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

big_paragraph = (
    "The Internet is a global system of interconnected computer networks that uses the Internet protocol suite (TCP/IP) to communicate between networks and devices. "
    "It is a network of networks that consists of private, public, academic, business, and government networks of local to global scope.\n\n"

    "The origins of the Internet date back to the development of packet switching and research commissioned by the United States Department of Defense in the 1960s. "
    "The primary precursor network was ARPANET. Later NSFNET and commercial Internet providers expanded it globally.\n\n"

    "Today the Internet supports cloud computing, email, social media, video conferencing, file sharing, online education, healthcare, e-commerce and much more."
)

documents = [Document(page_content=big_paragraph)]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

splits = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.from_documents(
    splits,
    embeddings
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)
