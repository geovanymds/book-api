from email import message
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from src.schemas import Book, ResponseSingleModel
import src.services.books as book_service

book_router = APIRouter()


@book_router.post("/", tags=["Book"],
                  response_description="Book data added into the database")
async def add_book(book: Book):
    try:
        book = jsonable_encoder(book)
        new_book = await book_service.create(book)
        return ResponseSingleModel(success=True, data=new_book,
                                   message="Book added successfully.")
    except:
        raise HTTPException(
            status_code=400,
            detail="Can't added the book.",
        )
