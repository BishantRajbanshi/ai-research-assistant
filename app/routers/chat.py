import logging

from fastapi import APIRouter, HTTPException

from app.schemas import ChatRequest, ChatResponse
from app.services.agent import agent

logger = logging.getLogger("chat_router")
router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    try:
        result = await agent.run(request.question)
        return ChatResponse(**result)
    except Exception as e:
        logger.exception(f"Error handling /chat request")
        raise HTTPException(status_code=500, detail=str(e)) from e