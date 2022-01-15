from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    title: str
    author: str


class Page(BaseModel):
    page_number: int
    page_text: str
    magic_code: str


class Image(BaseModel):
    magic_code: str


class ResponseSingleModel(BaseModel):
    data: Optional[dict]
    message: str
    success: bool


class ErrorResponse(BaseModel):
    message: str
