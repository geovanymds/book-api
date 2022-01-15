from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    title: str
    author: str


class ResponseSingleModel(BaseModel):
    data: Optional[dict]
    message: str
    success: bool


class ErrorResponse(BaseModel):
    message: str
