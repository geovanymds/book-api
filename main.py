import os
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from src.routes.books import book_router

app = FastAPI(title="Tortoise ORM FastAPI example")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

register_tortoise(
    app,
    db_url=os.environ['PGSQL_URL'],
    modules={"models": ["src.models.books",
                        "src.models.images", "src.models.pages"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(book_router, prefix='/book')


@app.get("/")
async def home():
    return Response(status_code=200, content="Service up.")
