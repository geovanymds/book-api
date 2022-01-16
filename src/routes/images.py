from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
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


@image_router.get("/{magic_code}/{file_name}", tags=["Image"],
                  response_description="Retrieve an image.")
async def get_image(magic_code: str, file_name: str):
    try:
        return FileResponse(f'public/{magic_code}/{file_name}')
    except Exception as error:
        print(f'[ERROR]: {error}')
        raise HTTPException(
            status_code=400,
            detail=f"{error}",
        )
