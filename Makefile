# Automatically format local python code
fmt:
	poetry run ruff format src ci
	poetry run ruff check src ci --fix
	make lint

# Check for lint errors
lint:
	poetry run ruff format --check src ci
	poetry run ruff check src ci
	make mypy

# Run type checking
mypy:
	poetry run mypy src ci --config-file setup.cfg

# Deploy the finetuned label model with Modal
deploy-vision-model:
	@if [ -z "${env}" ]; then echo "ERROR: 'env' variable is required" 1>&2; exit 1; fi
	poetry run modal deploy --env=${env} listening.utils.vision_model
