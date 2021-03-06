from src.models.pages import Pages
from src.models.books import Books
import src.utils.errors as errors


async def create(page_data: dict):
    try:
        print(f'PAGE DATA(service): {page_data}')
        book = await Books.filter(magic_code=page_data['magic_code'])
        if(len(book) <= 0):
            raise Exception(
                errors.BOOK_DONT_FOUND)
        if(book[0].total_pages == 6):
            raise Exception(
                errors.LIMIT_PAGES_BY_BOOK)
        is_page_number_valid = len(await Pages.filter(book_id=book[0].book_id, number=page_data['number'])) <= 0
        print(f'IS PAGE VALID: {is_page_number_valid}')
        if (not is_page_number_valid):
            raise Exception(
                errors.PAGE_ALREADY_RECORDED)
        print(f'BOOK FOUND: {book[0]}')
        page = await Pages.create(number=page_data['number'], text=page_data['text'], book_id=book[0].book_id)
        book[0].total_pages = book[0].total_pages+1
        await book[0].save()
        return page
    except Exception as error:
        raise error
