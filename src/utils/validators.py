from tarfile import SUPPORTED_TYPES
from fastapi import File, UploadFile, Form

SUPPORTED_FILES = ['png', 'jpg', 'jpeg']


async def file_validator(magic_code: str = Form(...), file: UploadFile = File(...)) -> int:
    try:
        content_type = file.content_type.rsplit("/")[1]
        if(content_type not in SUPPORTED_FILES):
            raise Exception('File not supported.')
    except Exception as error:
        print(f'[ERROR] : {error}')
        raise error
