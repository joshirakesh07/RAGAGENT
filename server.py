from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "SUCCESS",
        "message": "Render is working!"
    }

@app.get("/hello")
def hello():
    return {
        "message": "Hello World"
    }
