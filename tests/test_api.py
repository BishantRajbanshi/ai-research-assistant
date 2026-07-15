from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "Healthy"}


def test_chat_returns_answer_and_sources():
    with patch(
        "app.services.agent.ResearchAgent.run",
        new=AsyncMock(
            return_value={
                "answer": "FastAPI is a web framework.",
                "sources": ["fastapi.md"],
            }
        ),
    ):
        resp = client.post("/chat", json={"question": "What is FastAPI?"})
    assert resp.status_code == 200
    body = resp.json()
    assert "answer" in body
    assert "sources" in body


def test_chat_rejects_empty_question():
    resp = client.post("/chat", json={"question": ""})
    assert resp.status_code == 422