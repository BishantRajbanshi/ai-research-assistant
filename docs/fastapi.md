# FastAPI

FastAPI is a modern, high-performance Python web framework for building APIs.
It is built on top of Starlette (for the web parts) and Pydantic (for data
validation and serialization).

Key features:
- Automatic interactive API documentation (Swagger UI) generated from code.
- Data validation using Python type hints via Pydantic models.
- Native support for asynchronous request handlers (async def).
- Dependency injection for shared logic like authentication.
- High performance because it is built on ASGI rather than WSGI.

FastAPI is commonly used for REST APIs, microservices, and machine learning
backends because it validates request and response schemas automatically.
