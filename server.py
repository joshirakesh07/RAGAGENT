
from fastapi import FastAPI
from pydantic import BaseModel

from agent import internet_agent

app = FastAPI()


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Internet History RAG Agent is Running 🚀"
    }


@app.post("/ask")
def ask(query: Query):

    response = internet_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query.question
                }
            ]
        }
    )

    message = response["messages"][-1]

    if isinstance(message.content, list):
        answer = ""
        for item in message.content:
            if item.get("type") == "text":
                answer += item.get("text", "")
    else:
        answer = message.content

    return {
        "question": query.question,
        "answer": answer
    }
