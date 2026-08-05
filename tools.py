
from langchain_core.tools import tool
from rag import retriever


@tool
def retrieve_internet_context(query: str) -> str:
    """
    Retrieve relevant context from the Internet History document.
    """

    print("\n==============================")
    print("🔧 TOOL CALLED")
    print("Query:", query)
    print("==============================")

    docs = retriever.invoke(query)

    context = "\n\n".join(doc.page_content for doc in docs)

    print("Retrieved Chunks:", len(docs))

    return context
