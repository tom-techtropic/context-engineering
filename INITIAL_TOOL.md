## FEATURE:

Implement a simple HTTP server that acts as a key-value store for strings, where the key is a filename.

-   **HTTP Server:** A basic Python HTTP server.
-   **Endpoint for Saving String:** A `POST /tool/save` endpoint that accepts a JSON payload with `filename` and `content` fields.
    -   The server should store the `content` associated with the `filename` in an in-memory dictionary.
    -   The server should respond with a success message.
-   **Endpoint for Retrieving String:** A `GET /tool/retrieve/{filename}` endpoint that retrieves the `content` associated with the given `filename`.
    -   If the `filename` exists, return its `content`.
    -   If the `filename` does not exist, return an appropriate error.

## EXAMPLES:

-   `examples/cli.py`: Use this as a template for a basic server structure, adapting it for an HTTP server.
-   `examples/agent/`: Review the data structures and organization in this directory for inspiration on how to structure the in-memory store.

## DOCUMENTATION:

-   FastAPI documentation: https://fastapi.tiangolo.com/ (Recommended for building the HTTP server and handling JSON).
-   Pydantic documentation: https://docs.pydantic.dev/ (For defining the structure of the incoming payload and response).

## OTHER CONSIDERATIONS:

-   **Storage:** Use a simple in-memory Python dictionary to store the strings. No persistence to disk is required for this initial version.
-   **Authentication:** No authentication or authorization is needed for this simple prototype.
-   **Error Handling:** Basic error handling for missing files or invalid payloads is sufficient.
