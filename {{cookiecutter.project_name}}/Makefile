.DEFAULT_GOAL := build
.PHONY: build publish package coverage test lint docs venv
PROJ_SLUG = {{cookiecutter.package_name}}
CLI_NAME = {{cookiecutter.cli_name}}
PY_VERSION = {{cookiecutter.python_version}}
LINTER = {{cookiecutter.linter}}
{% if cookiecutter.virtualenv == 'python3' %}
SHELL = bash
{% endif %}


build:
{% if cookiecutter.virtualenv == 'pipenv' %}
	pipenv install --dev -e .
{% else %}
	python$(PY_VERSION) install --editable .
{% endif %}

run:
	$(CLI_NAME) run

submit:
	$(CLI_NAME) submit

freeze:
{% if cookiecutter.virtualenv == 'pipenv' %}
	pipenv lock -r > requirements.txt
{% else %}
	python$(PY_VERSION) -m pip freeze > requirements.txt
{% endif %}
lint:
	$(LINTER) $(PROJ_SLUG)

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
	{% if cookiecutter.auto_readme == 'pandoc' %}pandoc --from=markdown --to=rst --output=README.rst README.md{% endif %}

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
{% if cookiecutter.virtualenv == 'pipenv' %}
	pipenv shell
{% endif %}
{% if cookiecutter.virtualenv == 'virtualenv' %}
	virtualenv --python python$(PY_VERSION) venv
{% endif %}
{% if cookiecutter.virtualenv == 'python3' %}
	python3 -m venv venv
	source venv/bin/activate && pip install pip --upgrade --index-url=https://pypi.org/simple
{% endif %}

install:
{% if cookiecutter.virtualenv == 'pipenv' %}
	pipenv install --dev
{% else %}
	pip install -r requirements.txt
{% endif %}

licenses:
	pip-licenses --with-url --format=rst \
	--ignore-packages $(shell cat .pip-lic-ignore | awk '{$$1=$$1};1')
