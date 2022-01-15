from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from src.schemas import Image, ResponseSingleModel
from src.services.save_file import save_file
from src.utils.validators import file_validator

image_router = APIRouter()


@image_router.post("/", tags=["Image"],
                   response_description="Image uploaded on server")
async def upload_image(magic_code: str = Form(...), file: UploadFile = File(...)):
    try:
        # await save_file(file, magic_code)
        await file_validator(magic_code, file)
        return {'file': file}
    except Exception as error:
        print(f'[ERROR]: {error}')
        raise HTTPException(
            status_code=400,
            detail="Can't upload image.",
        )
