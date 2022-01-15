from fastapi import UploadFile
from src.utils.utils import createDirectoryIfDoesntExist


async def save_file(file: UploadFile, magic_code: str) -> bool:
    try:
        createDirectoryIfDoesntExist(magic_code)
        with open(f'src/public/{magic_code}/{file.filename}', 'wb') as image:
            content = await file.read()
            image.write(content)
            image.close()
            print('File saved !')
            return True
    except Exception as error:
        print(f'[ERRO]: {error}')
        raise error
