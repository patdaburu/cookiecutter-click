.DEFAULT_GOAL := build
.PHONY: build publish package coverage test lint docs venv
PROJ_SLUG = {{cookiecutter.package_name}}
CLI_NAME = {{cookiecutter.cli_name}}
PY_VERSION = {{cookiecutter.python_version}}

GREEN = 2
RED = 1

define colorecho
        @tput bold
        @tput setaf $1
        @echo $2
        @tput sgr0
endef

build:
	pip install --editable .

run:
	$(CLI_NAME) run

submit:
	$(CLI_NAME) submit

freeze:
	pip freeze > requirements.txt

lint:
	pylint $(PROJ_SLUG)

test: lint
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

quicktest:
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

coverage: lint
	py.test --cov-report html --cov=$(PROJ_SLUG) tests/

docs: coverage
	mkdir -p docs/source/_static
	mkdir -p docs/source/_templates
	cd docs && $(MAKE) html

answers:
	cd docs && $(MAKE) html
	xdg-open docs/build/html/index.html

package: clean docs
	python setup.py sdist

publish: package
	twine upload dist/*

clean :
	rm -rf dist \
	rm -rf docs/build \
	rm -rf *.egg-info
	coverage erase

venv :
	virtualenv --python python$(PY_VERSION) venv
	@echo
	@echo To activate the environment, use the following command:
	@echo
	$(call colorecho, $(GREEN), "source venv/bin/activate")
	@echo
	@echo Once activated, you can use the 'install' target to install dependencies:
	@echo
	$(call colorecho, $(GREEN), "source venv/bin/activate")

install:
	pip install -r requirements.txt

licenses:
	pip-licenses --with-url --format-rst \
	--ignore-packages $(shell cat .pip-license-ignore | awk '{$$1=$$1};1')
