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


@book_router.get("/", tags=["Book"],
                 response_description="Return all books from the database.")
async def get_books():
    try:
        return await book_service.get_all()
    except:
        raise HTTPException(
            status_code=400,
            detail="Can't find books.",
        )


@book_router.get("/{magic_code}", tags=["Book"], response_description="Return books info.")
async def get_book_info(magic_code: str):
    try:
        return await book_service.get_book_info_by_magic_code(magic_code)
    except:
        raise HTTPException(
            status_code=400,
            detail="Can't find book info.",
        )
