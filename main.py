import os
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from src.utils.utils import createDirectoryIfDoesntExist
from src.routes.books import book_router
from src.routes.pages import page_router
from src.routes.images import image_router

app = FastAPI(title="Livro mágico")

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
app.include_router(page_router, prefix='/page')
app.include_router(image_router, prefix='/image')

createDirectoryIfDoesntExist('public/')


@app.get("/", tags=["Status"], response_description="Return message Service Up if server is working.")
async def home():
    return Response(status_code=200, content="Service up.")
