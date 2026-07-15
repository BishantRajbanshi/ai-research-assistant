import logging

from fastapi import FastAPI

from app.routers import chat, health

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [ %(name)s]  [%(message)s]",)

app = FastAPI(
    title="AI Research Assistant API",
    description="Answers questions using a local knowledge base + LLM.",
    version="1.0.0",
)

app.include_router(health.router, tags=["Health"])
app.include_router(chat.router, tags=["Chat"])

