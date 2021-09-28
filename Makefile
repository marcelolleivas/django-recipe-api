.PHONY: clean test security-checker code-convention typing-checker pipeline

PROJECT_NAME := django-recipe-api
PYTHON_VERSION := 3.8.10
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

.clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


.clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


.clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr reports/
	rm -fr .pytest_cache/

clean: .clean-build .clean-pyc .clean-test ## remove all build, test, coverage and Python artifacts

code-convention:
	flake8
	pycodestyle

test:
	pytest --cov-report=term-missing  --cov-report=html --cov=. --disable-warnings