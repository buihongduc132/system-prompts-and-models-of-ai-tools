# Makefile for timestamp utilities development

.PHONY: help install install-dev test test-verbose test-coverage lint format type-check clean run-example all-checks

# Default target
help:
	@echo "Available targets:"
	@echo "  install      - Install the package"
	@echo "  install-dev  - Install with development dependencies"
	@echo "  test         - Run tests"
	@echo "  test-verbose - Run tests with verbose output"
	@echo "  test-coverage - Run tests with coverage report"
	@echo "  lint         - Run linting (flake8)"
	@echo "  format       - Format code (black + isort)"
	@echo "  type-check   - Run type checking (mypy)"
	@echo "  clean        - Clean build artifacts"
	@echo "  run-example  - Run the basic usage example"
	@echo "  all-checks   - Run all quality checks"

# Installation targets
install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

# Testing targets
test:
	python -m pytest tests/

test-verbose:
	python -m pytest tests/ -v

test-coverage:
	python -m pytest tests/ --cov=timestamp_utils --cov-report=html --cov-report=term-missing

# Code quality targets
lint:
	flake8 src/ tests/ examples/

format:
	black src/ tests/ examples/
	isort src/ tests/ examples/

type-check:
	mypy src/

# Utility targets
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run-example:
	python examples/basic_usage.py

# Run all quality checks
all-checks: lint type-check test-coverage
	@echo "All quality checks completed successfully!"

# Development workflow
dev-setup: install-dev
	@echo "Development environment set up successfully!"
	@echo "Run 'make all-checks' to verify everything is working."

