up:
	docker-compose up
down:
	docker-compose down
stop:
	docker-compose stop
api:
	docker exec -it container_book_api /bin/sh
db:
	docker exec -it container_pgsql_db bash -c "psql -h 127.0.0.1 -U geo_dev -d book_api_db -W"