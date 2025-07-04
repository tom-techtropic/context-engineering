## FEATURE:

Implement a simple Model-Context Protocol (MCP) server that echoes received messages and stores them.

-   **HTTP Server:** A basic Python HTTP server.
-   **Endpoint for Context Storage:** A `POST /context` endpoint that accepts a JSON payload containing a "message" field.
    -   The server should store this message in an in-memory list.
    -   The server should respond with a JSON object echoing the received message.
-   **Endpoint for Context Retrieval:** A `GET /context` endpoint that returns all stored messages as a JSON array.

## EXAMPLES:

-   `examples/cli.py`: Use this as a template for a basic server structure, adapting it for an HTTP server.
-   `examples/agent/`: Review the data structures and organization in this directory for inspiration on how to structure the stored messages, even though it's for a different purpose.

## DOCUMENTATION:

-   FastAPI documentation: https://fastapi.tiangolo.com/ (Recommended for building the HTTP server and handling JSON).
-   Pydantic documentation: https://docs.pydantic.dev/ (For defining the structure of the incoming message payload).

## OTHER CONSIDERATIONS:

-   **Storage:** Use a simple in-memory list to store messages for this initial version. No persistence to disk is required.
-   **Authentication:** No authentication or authorization is needed for this simple prototype.
-   **Error Handling:** Basic error handling for invalid JSON payloads is sufficient.
