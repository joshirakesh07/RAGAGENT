from langchain_core.documents import Document

big_paragraph = (
    "The Internet is a global system of interconnected computer networks that uses the Internet protocol suite (TCP/IP) to communicate between networks and devices. "
    "It is a network of networks that consists of private, public, academic, business, and government networks of local to global scope.\n\n"

    "The origins of the Internet date back to the development of packet switching and research commissioned by the United States Department of Defense in the 1960s. "
    "The primary precursor network was ARPANET. Later NSFNET and commercial Internet providers expanded it globally.\n\n"

    "Today the Internet supports cloud computing, email, social media, video conferencing, file sharing, online education, healthcare, e-commerce and much more."
)

documents = [
    Document(page_content=big_paragraph)
]
