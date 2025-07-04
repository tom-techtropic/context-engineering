from pydantic import BaseModel

class SaveRequest(BaseModel):
    filename: str
    content: str

class SaveResponse(BaseModel):
    message: str

class RetrieveResponse(BaseModel):
    content: str

class ErrorResponse(BaseModel):
    detail: str
