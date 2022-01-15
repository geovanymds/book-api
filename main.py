import os
from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(title="Tortoise ORM FastAPI example")

register_tortoise(
    app,
    db_url=os.environ['PGSQL_URL'],
    modules={"models": ["src.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
