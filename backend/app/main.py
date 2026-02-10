from fastapi import FastAPI
from app.api.agent import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Mini AI Agent API is running. See /docs for API docs."}
