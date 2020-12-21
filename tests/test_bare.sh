#!/usr/bin/env bash
#
# Tests the default configuration for cookiecutter-click
# Run from the root directory of the repository
# eg: ./tests/test_bard.sh
#

set -o errexit

# helper function
install_python_deps() {
  pip install --use-feature=2020-resolver \
              --user \
              --requirement requirements.txt
}

# make clean python env
pip install virtualenv
python --module virtualenv venv
source venv/bin/activate

# install test deps
install_python_deps

# create project using cookiecutter.json default values
cookiecutter --no-input \
             --overwrite-if-exists use_docker=n \
             $@
cd my_awesome_project

# install project python deps
install_python_deps

# Output project for sanity
ls -alt

# run tests
pytest
