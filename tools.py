from langchain_core.tools import tool
from rag import documents

@tool
def retrieve_internet_context(query: str) -> str:
    """
    Retrieve Internet history context.
    """

    print("🔧 TOOL CALLED")
    print("Query:", query)

    return documents[0].page_content
