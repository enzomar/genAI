# Makefile

VENV_NAME = venv
PYTHON = python3

venv:
	$(PYTHON) -m venv $(VENV_NAME)

install:
	@echo "Activating virtual environment..."
	@source $(VENV_NAME)/bin/activate && \
	pip install -r requirements.txt

run:
	@echo "Running the application..."
	@source $(VENV_NAME)/bin/activate && \
	$(PYTHON) ui.py

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

.PHONY: venv install run clean
