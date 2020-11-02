.PHONY: help test lint

MODULE_NAME ?= cloudwatch_alarm_to_slack
VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make test"
	@echo "       run unit tests"
	@echo "make lint"
	@echo "       run flake8 and isort"
	@echo "make devbuild"
	@echo "       environment for local development"
	@echo "make clean"
	@echo "       clean venv"


test: venv pytest


lint: venv flake8 isort


venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r test_requirements.txt
	touch $(VENV_NAME)/bin/activate


pytest:
	$(info Make: Running unit tests)
	@${PYTHON} -m pytest -vv --cov ${MODULE_NAME} --cov-report term-missing
	

flake8:
	$(info Make: Running flake8)
	@flake8 cloudwatch_alarm_to_slack/


isort:
	$(info Make: Running isort)
	@isort cloudwatch_alarm_to_slack/


devbuild: venv
	${PYTHON} setup.py install


clean:
	rm -rf venv
