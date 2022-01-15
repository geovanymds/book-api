up:
	docker-compose up
# down:
# 	docker-compose down
stop:
	docker-compose stop
build: 
	docker-compose up --build
freeze:
	docker exec -it container_book_api pip freeze > requirements.txt
install:
	docker exec -it container_book_api pip install -r requirements.txt
api:
	docker exec -it container_book_api /bin/sh
db:
	docker exec -it container_pgsql_db bash -c "psql -h 127.0.0.1 -U geo_dev -d book_api_db -W"