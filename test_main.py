import json
import pytest
import src.services.books as books_service
import src.services.pages as pages_service


def test_main(test_app):
    response = test_app.get("/")
    assert response.status_code == 200


def test_create_book(test_app, monkeypatch):
    test_request_payload = {"title": "something",
                            "author": "something else", "teacher": "some teacher"}
    test_response_payload = {
        "data": {
            "total_images": 0,
            "title": "Meu primeiro livro",
            "book_id": 1,
            "teacher": "Bruna",
            "magic_code": "BOMJGS",
            "author": "Geovany",
            "total_pages": 0
        },
        "message": "Book added successfully.",
        "success": True}

    async def mock_post(payload):
        return {"total_images": 0,
                "title": "Meu primeiro livro",
                "book_id": 1,
                "teacher": "Bruna",
                "magic_code": "BOMJGS",
                "author": "Geovany",
                "total_pages": 0}

    monkeypatch.setattr(books_service, "create", mock_post)

    response = test_app.post("/book/", data=json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_create_page(test_app, monkeypatch):
    test_request_payload = {"number": 1,
                            "text": "my text", "magic_code": "123"}
    test_response_payload = {
        "data": {"number": 1,
                 "text": "my text", "magic_code": "123"},
        "message": "Page attached to the book succefully.",
        "success": True}

    async def mock_post(payload):
        return {"number": 1,
                "text": "my text", "magic_code": "123"}

    monkeypatch.setattr(pages_service, "create", mock_post)

    response = test_app.post("/page/", data=json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_retrieve_all_books(test_app, monkeypatch):
    test_response_payload = [{"title": "livro 1", "magic_code": "ABCDEF"}, {
        "title": "livro 2", "magic_code": "ABCGEF"}]

    async def mock_get():
        return test_response_payload

    monkeypatch.setattr(books_service, "get_all", mock_get)

    response = test_app.get("/book/")

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_retrieve_book_by_magic_code(test_app, monkeypatch):
    test_response_payload = {"title": "Meu primeiro livro",
                             "magic_code": "ABCDEF",
                             "images": [
                                 {
                                     "name": "1-nodejs-new-white.png",
                                     "url": "http://localhost:8000/image/ABCDEF/1-nodejs-new-white.png"
                                 }
                             ],
                             "pages": [
                                 {
                                     "text": "Some text ",
                                     "number": 5
                                 }
                             ]}

    async def mock_get(query_param):
        return test_response_payload

    monkeypatch.setattr(books_service, "get_book_info_by_magic_code", mock_get)

    response = test_app.get("/book/ABCDEF")

    assert response.status_code == 200
    assert response.json() == test_response_payload
