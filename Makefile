.PHONY: help up down build logs shell lint format check clean

help:
	@echo "Available commands:"
	@echo "  make up       - Build and start services"
	@echo "  make down     - Stop services"
	@echo "  make build    - Build Docker images"
	@echo "  make logs     - View backend logs"
	@echo "  make shell    - Open backend shell"
	@echo "  make lint     - Run Ruff linter"
	@echo "  make format   - Format Python code"
	@echo "  make check    - Run pre-commit hooks"
	@echo "  make clean    - Remove stopped containers"

up:
	docker compose up --build

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f backend

shell:
	docker compose exec backend sh

lint:
	ruff check backend

format:
	ruff format backend

check:
	pre-commit run --all-files

clean:
	docker compose down --remove-orphans
