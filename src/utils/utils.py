import uuid
import os


def generateMagicCode() -> str:
    return str(uuid.uuid4())


def createDirectoryIfDoesntExist(path: str) -> bool:
    exists = os.path.exists(path)
    if(not exists):
        os.makedirs(path)
        print(f'Directory "{path}" created !')
        return True
    return False
