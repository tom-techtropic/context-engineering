from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models import SaveRequest, SaveResponse, RetrieveResponse, ErrorResponse
import uvicorn

# In-memory storage
_storage: dict[str, str] = {}

app = FastAPI()

class SaveRequest(BaseModel):
    filename: str
    content: str

class SaveResponse(BaseModel):
    message: str

class RetrieveResponse(BaseModel):
    content: str

class ErrorResponse(BaseModel):
    detail: str

@app.post("/tool/save", response_model=SaveResponse)
async def save_string(request: SaveRequest):
    _storage[request.filename] = request.content
    return SaveResponse(message=f"Content saved to {request.filename}")

@app.get("/tool/retrieve/{filename}", response_model=RetrieveResponse)
async def retrieve_string(filename: str):
    if filename not in _storage:
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found")
    return RetrieveResponse(content=_storage[filename])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
