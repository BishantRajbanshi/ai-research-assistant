# Agentic AI

Agentic AI refers to systems where a language model follows a multi-step
workflow to accomplish a task, often involving tool use and decision-making,
rather than just responding to a single prompt.

A simple agent pipeline:
1. Receive a user question.
2. Decide what information is needed (e.g., search a knowledge base).
3. Gather that information.
4. Use the LLM to reason over it and produce an answer.
5. Return the result.

Frameworks like LangChain provide abstractions for this, but a simple agent
can be implemented directly as an explicit, modular pipeline, which is easier
to reason about and debug.
