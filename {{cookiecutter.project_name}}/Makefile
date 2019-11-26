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
	pip install --editable .

run:
	$(CLI_NAME) run

submit:
	$(CLI_NAME) submit

freeze:
	pip freeze > requirements.txt

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
{% if cookiecutter.virtualenv == 'virtualenv' %}
	virtualenv --python python$(PY_VERSION) venv
{% endif %}
{% if cookiecutter.virtualenv == 'python3' %}
	python3 -m venv venv
	source venv/bin/activate && pip install pip --upgrade --index-url=https://pypi.org/simple
{% endif %}

install:
	pip install -r requirements.txt

licenses:
	pip-licenses --with-url --format=rst \
	--ignore-packages $(shell cat .pip-license-ignore | awk '{$$1=$$1};1')
