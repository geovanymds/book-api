import uuid
import os

PUBLIC_PATH = 'src/public/'


def generateMagicCode() -> str:
    return str(uuid.uuid4())


def createDirectoryIfDoesntExist(magic_code: str) -> bool:
    exists = os.path.exists(f'{PUBLIC_PATH}/{magic_code}')
    if(not exists):
        os.makedirs(f'{PUBLIC_PATH}/{magic_code}')
        print(f'Directory "{PUBLIC_PATH}/{magic_code}" created !')
        return True
    return False
