PROJ_SLUG = {{cookiecutter.package_name}}
CLI_NAME = {{cookiecutter.cli_name}}
PY_VERSION = {{cookiecutter.python_version}}
LINTER = {{cookiecutter.linter}}
{% if cookiecutter.virtualenv == 'python3' %}
SHELL = bash
{% endif %}

.PHONY: build run submit freeze lint test coverage docs package publish install-deps licenses clean

build: clean
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
	pip freeze > requirements.txt

lint:
	$(LINTER) $(PROJ_SLUG)

test: lint
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

coverage: lint
	py.test --cov-report html --cov=$(PROJ_SLUG) tests/

docs: coverage
	mkdir -p docs/source/{_static,_templates}
	cd docs && $(MAKE) html
{% if cookiecutter.auto_readme == 'pandoc' %}
	pandoc --from=markdown --to=rst --output=README.rst README.mdiiii{% endif %}

package: clean docs
	python setup.py sdist

publish: package
	twine upload dist/*

venv:
{% if cookiecutter.virtualenv == 'virtualenv' %}
	python$(PY_VERSION) -m virtualenv --python python$(PY_VERSION) venv
{% elif cookiecutter.virtualenv == 'pipenv' %}
	python$(PY_VERSION) -m pipenv shell
{% else %}
	python$(PY_VERSION) -m venv venv
	source venv/bin/activate 
	pip install pip --upgrade --index-url=https://pypi.org/simple
{% endif %}

install-deps:
{% if cookiecutter.virtualenv == 'pipenv' %}
	pipenv install --dev
{% else %}
	pip install -r requirements.txt
{% endif %}

licenses:
	pip-licenses \
		--with-url --format=rst \
		--ignore-packages $(shell cat .pip-lic-ignore | awk '{$$1=$$1};1')

clean:
	rm -rf dist \
		   docs/build \
		   *.egg-info
	coverage erase
