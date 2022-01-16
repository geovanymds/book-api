from email import message
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from src.schemas import Page, ResponseSingleModel
import src.services.pages as page_service
import src.utils.errors as errors

page_router = APIRouter()


@page_router.post("/", tags=["Page"],
                  response_description="Page attatched to book.")
async def add_page(page: Page):
    try:
        if(page.number <= 0 or page.number > 6):
            raise Exception(errors.PAGE_NUMBER_OUT_OF_RANGE)
        page = jsonable_encoder(page)
        new_page = await page_service.create(page)
        return ResponseSingleModel(success=True, data=new_page,
                                   message="Page attached to the book succefully.")
    except Exception as error:
        print(f'[ERROR]: {error}')
        raise HTTPException(
            status_code=400,
            detail=f"{error}",
        )
