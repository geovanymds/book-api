from fastapi import File, UploadFile
from src.models.images import Images
from src.models.books import Books
from src.services.save_file import save_file
import src.utils.errors as errors


async def upload(magic_code: str, file: UploadFile = File(...)):
    try:
        book = await Books.filter(magic_code=magic_code)
        print(f'BOOK: {book[0]}')
        if(not book or len(book) <= 0):
            raise Exception(errors.BOOK_DONT_FOUND)
        if(book[0].total_images == 6):
            raise Exception(errors.LIMIT_IMAGES_BY_BOOK)
        file_index = book[0].total_images + 1
        image_info = await save_file(file, magic_code, file_index)
        image_stored_data = await Images.create(url=image_info['url'], name=image_info['name'], path=image_info['path'], book_id=book[0].book_id)
        book[0].total_images = book[0].total_images+1
        await book[0].save()
        return image_stored_data
    except Exception as error:
        raise error
