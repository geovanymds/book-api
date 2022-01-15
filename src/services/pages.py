from src.models.pages import Pages
from src.models.books import Books
# import src.utils.utils as utils


async def create(page_data: dict):
    try:
        print(f'PAGE DATA(service): ${page_data}')
        book = await Books.filter(magic_code=page_data['magic_code'])
        if(len(book) <= 0):
            raise Exception(
                'Book dont found.')
        if(book[0].total_pages == 6):
            raise Exception(
                'Book already have 6 pages.')
        is_page_number_valid = len(await Pages.filter(book_id=book[0].book_id, page_number=page_data['page_number'])) <= 0
        print(f'IS PAGE VALID: ${is_page_number_valid}')
        if (not is_page_number_valid):
            raise Exception(
                f'This book already has pagen number ${page_data["page_number"]}')
        print(f'BOOK FOUND: ${book[0]}')
        page = await Pages.create(page_number=page_data['page_number'], page_text=page_data['page_text'], book_id=book[0].book_id)
        book[0].total_pages = book[0].total_pages+1
        await book[0].save()
        return page
    except Exception as error:
        print(f'[ERRO]: ${error}')
        raise error
