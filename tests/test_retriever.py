from app.services.retriever import retriever


def test_loads_documents():
    assert len(retriever.documents) >= 4


def test_retrieve_relevant_doc():
    results = retriever.retrieve("What is FastAPI?", top_k=1)
    assert "fastapi" in results[0].source.lower()


def test_retrieve_rag_doc():
    results = retriever.retrieve("Explain retrieval augmented generation", top_k=1)
    assert "rag" in results[0].source.lower()