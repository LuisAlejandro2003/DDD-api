# ===== Config =====
PY       ?= python3
VENV     ?= .venv
PIP      := $(VENV)/bin/pip
UVICORN  := $(VENV)/bin/uvicorn
APP_DIR  ?= src
APP_MOD  ?= api_app:app
HOST     ?= 0.0.0.0
PORT     ?= 8000

COMPOSE_FILE := src/core/docker/compose.yml

.PHONY: venv install run db-up db-down db-logs

venv:
	$(PY) -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	$(PIP) install -r requirements.txt

run:
	$(UVICORN) $(APP_MOD) --app-dir $(APP_DIR) --reload --host $(HOST) --port $(PORT)

# ===== Docker Postgres =====
db-up:
	docker compose -f $(COMPOSE_FILE) up -d

db-down:
	docker compose -f $(COMPOSE_FILE) down

db-logs:
	docker compose -f $(COMPOSE_FILE) logs -f postgres
