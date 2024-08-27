# Automatically format local python code
fmt:
	poetry run ruff format src
	poetry run ruff check src --fix
	make lint

# Check for lint errors
lint:
	poetry run ruff format --check src
	poetry run ruff check src
	make mypy

# Run type checking
mypy:
	poetry run mypy src --config-file setup.cfg
