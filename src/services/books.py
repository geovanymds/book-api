from src.models.books import Books
from src.models.images import Images
from src.models.pages import Pages
import src.utils.errors as errors

import src.utils.utils as utils


async def create(book_data: dict):
    try:
        generated_magic_code = utils.generateMagicCode()
        book_data['magic_code'] = generated_magic_code
        print(f'BOOK DATA(service): {book_data}')
        book = await Books.create(magic_code=book_data['magic_code'], title=book_data['title'], author=book_data['author'], teacher=book_data['teacher'])
        return book
    except Exception as error:
        print(f'[ERRO]: {error}')
        raise error


async def get_all():
    try:
        books = await Books.filter()
        returned_books = []
        for book in books:
            returned_books.append(
                {'title': book.title, 'magic_code': book.magic_code})
        return returned_books
    except Exception as error:
        print(f'[ERRO]: {error}')
        raise error


async def get_book_info_by_magic_code(magic_code: str):
    try:
        books = await Books.filter(magic_code=magic_code)
        if(not books or len(books) <= 0):
            raise Exception(errors.BOOK_DONT_FOUND)
        images = await Images.filter(book_id=books[0].book_id)
        pages = await Pages.filter(book_id=books[0].book_id)
        images_info = []
        pages_info = []
        for image in images:
            images_info.append({'name': image.name, 'url': image.url})
        for page in pages:
            pages_info.append(
                {'text': page.text, 'number': page.number})
        book_info = {
            'title': books[0].title, 'magic_code': books[0].magic_code, 'images': images_info, 'pages': pages_info}
        return book_info
    except Exception as error:
        raise error
