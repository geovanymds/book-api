from fastapi import UploadFile
from src.utils.utils import createDirectoryIfDoesntExist


async def save_file(file: UploadFile, magic_code: str, file_index: int) -> bool:
    try:
        createDirectoryIfDoesntExist(f'public/{magic_code}')
        image_info = {}
        path = f'public/{magic_code}/{file_index}-{file.filename}'
        with open(path, 'wb') as image:
            content = await file.read()
            image.write(content)
            image.close()
            print('File saved !')
        image_info['path'] = path
        image_info['url'] = f'http://localhost:8000/image/{magic_code}/{file_index}-{file.filename}'
        image_info['name'] = f'{file_index}-{file.filename}'
        return image_info
    except Exception as error:
        print(f'[ERRO]: {error}')
        raise error
