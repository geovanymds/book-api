from fastapi import APIRouter, File, UploadFile, HTTPException, Form
import src.services.images as image_service
from src.schemas import ResponseSingleModel

from src.utils.validators import file_validator

image_router = APIRouter()


@image_router.post("/{magic_code}", tags=["Image"],
                   response_description="Image uploaded on server")
async def upload_image(magic_code: str, file: UploadFile = File(...)):
    try:
        await file_validator(magic_code, file)
        image = await image_service.upload(magic_code, file)
        return ResponseSingleModel(success=True, data=image,
                                   message="Image attatched successfully.")
    except Exception as error:
        print(f'[ERROR]: {error}')
        raise HTTPException(
            status_code=400,
            detail=f"{error}",
        )
