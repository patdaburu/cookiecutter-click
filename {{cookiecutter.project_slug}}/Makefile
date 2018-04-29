.DEFAULT_GOAL := build
.PHONY: build publish package coverage test lint docs venv conda
PROJ_NAME = {{cookiecutter.project_slug}}
PY_VERSION = {{cookiecutter.python_version}}

define echogreen
        @tput bold
        @tput setaf 2
        @echo $1
        @tput sgr0
endef

build:
	pip install --editable .

freeze:
	pip freeze > requirements.txt

lint:
	pylint $(PROJ_NAME)

test:
	py.test --cov . tests/

coverage: test
	mkdir -p docs/build/html
	coverage html

docs: coverage
	mkdir -p docs/source/_static
	mkdir -p docs/source/_templates
	cd docs && $(MAKE) html

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
	@echo To activate the environment, use the 'source' command from the shell.
	$(call echogreen, "source venv/bin/activate")
	@echo
	@echo To install the projects dependencies, run the 'install' target.
	$(call echogreen, "make install")
	@echo
	@echo To build the command-line utility, run the 'build' target.
	$(call echogreen, "make build")

conda:
	conda env create -f environment.yml
	@echo
	@echo To activate the environment, use the following command:
	$(call echogreen, "source activate " $(PROJ_NAME))
	@echo
	@echo To install the projects dependencies, run the 'install' target.
	$(call echogreen, "make install")
	@echo
	@echo To build the command-line utility, run the 'build' target.
	$(call echogreen, "make build")
	@echo
	@echo To remove this environment, use the following command:
	@echo      conda remove --name $(PROJ_NAME) --all

activate:
	@echo Make cannot do this for you, but you can do one of the following...
	@echo
	@echo If you are using a local virtual environment:
	$(call echogreen, "source venv/bin/activate")
	@echo
	@echo If your are using a conda virtual environment:
	$(call echogreen, "source activate "  $(PROJ_NAME))

install:
	pip install -r requirements.txt
