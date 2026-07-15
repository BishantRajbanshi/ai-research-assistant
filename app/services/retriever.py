"""
This loads out knowledge base and finds most relevent documents for a question.
which uses TF_TDF + cosine similarity 
"""

from dataclasses import dataclass
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.core.config import settings


@dataclass
class Document:
    source: str
    content: str


class Retriever:
    def __init__(self, docs_dir: str):
        self.docs_dir = Path(docs_dir)
        self.documents: list[Document] = []
        self._load()

    def _load(self) -> None:
        """
        Read every .md file in docs_dir and store them into memory, then vectorize.
        """
        for path in sorted(self.docs_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            self.documents.append(
                Document(
                    source=str(path),
                      content=text
                )
            )

        if not self.documents:
            raise RuntimeError(f"No documents found in {self.docs_dir}")

        corpus = [doc.content for doc in self.documents]
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.doc_matrix = self.vectorizer.fit_transform(corpus)

    def retrieve(self, query: str, top_k: int = 2) -> list[Document]:
        """Return the top_k documents most similar to the query."""
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.doc_matrix).flatten()
        ranked_idx = scores.argsort()[::-1]

        results = [self.documents[i] for i in ranked_idx[:top_k] if scores[i] > 0]

        if not results:
            results = [self.documents[ranked_idx[0]]]
        return results


retriever = Retriever(settings.docs_dir)