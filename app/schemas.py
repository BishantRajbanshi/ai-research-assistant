from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, examples=["What is FastAPI?"])

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]

class HealthResponse(BaseModel):
    status: str

    