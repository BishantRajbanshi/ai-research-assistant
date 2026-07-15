"""
This is agent pipeline 
Question -> Retriever -> LLM -> Answer + Sources
"""

import logging

from app.core.config import settings
from app.services.llm_client import get_llm_client
from app.services.retriever import retriever

logger = logging.getLogger("agent")

PROMPT_TEMPLATE = """You are a helpful research assistant. Answer the user's \
question using ONLY the context below. If the context does not contain the \
answer, say you don't have enough information.

Context:
{context}

Question: {question}

Answer:"""

class ResearchAgent:
    def __init__(self):
        self.llm_client = get_llm_client()

    async def run(self, question: str) -> str:
        # Step 1 : retrieve relevant documents
        docs = retriever.retrieve(question, top_k=settings.top_k)
        logger.info(f"Retrieved {len(docs)} documents for question: {question}")

        # Step 2 : construct context
        context = "\n\n".join(f"[{d.source}]: {d.content}" for d in docs)
        prompt = PROMPT_TEMPLATE.format(context=context, question=question)

        # Step 3 : generate answer using LLM
        answer = await self.llm_client.generate(prompt)

        return {
            "answer": answer,
            "sources": [d.source for d in docs],
        }
    
agent = ResearchAgent()
