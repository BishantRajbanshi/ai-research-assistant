# Retrieval-Augmented Generation (RAG)

RAG combines information retrieval with LLM text generation. Instead of
relying only on training knowledge, RAG retrieves relevant documents from an
external knowledge base at query time and includes them in the prompt.

Typical pipeline:
1. Index documents (embeddings or keyword methods like TF-IDF).
2. On each question, retrieve the most relevant documents.
3. Insert the retrieved text into the LLM prompt as context.
4. Ask the LLM to answer using that context.

RAG reduces hallucination and lets systems answer questions about private or
recent data without fine-tuning a model.
