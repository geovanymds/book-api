from src.models.books import Books
import src.utils.utils as utils


async def create(book_data: dict):
    try:
        generated_magic_code = utils.generateMagicCode()
        book_data['magic_code'] = generated_magic_code
        print(f'BOOK DATA(service): {book_data}')
        book = await Books.create(magic_code=book_data['magic_code'], title=book_data['title'], author=book_data['author'])
        return book
    except Exception as error:
        print(f'[ERRO]: {error}')
        raise error
