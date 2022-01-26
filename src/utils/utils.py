import os
from src.models.books import Books
import string
import random
import src.utils.errors as errors


def generate_random_code():
    return ''.join(random.choice(string.ascii_uppercase)
                   for _ in range(6))


async def generateMagicCode() -> str:
    try:
        candidate_code = generate_random_code()
        books = await Books.filter(magic_code=candidate_code)
        tries = 0
        while(len(books) > 0 and tries < 5):
            candidate_code = generate_random_code()
            books = await Books.filter(magic_code=candidate_code)
            tries = tries + 1
        if(tries == 5):
            raise Exception(errors.COUDNT_CREATE_MAGIC_CODE)
        return candidate_code
    except Exception as error:
        raise error


def createDirectoryIfDoesntExist(path: str) -> bool:
    exists = os.path.exists(path)
    if(not exists):
        os.makedirs(path)
        print(f'Directory "{path}" created !')
        return True
    return False
