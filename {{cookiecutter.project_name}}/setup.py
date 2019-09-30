#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: setup.py
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This file is used to create the package we'll publish to PyPI.
"""

import importlib.util
import os
from pathlib import Path
from setuptools import setup, find_packages
from codecs import open  # Use a consistent encoding.
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get the base version from the library.  (We'll find it in the `version.py`
# file in the src directory, but we'll bypass actually loading up the library.)
vspec = importlib.util.spec_from_file_location(
  "version",
  str(Path(__file__).resolve().parent /
      '{{cookiecutter.package_name}}'/"version.py")
)
vmod = importlib.util.module_from_spec(vspec)
vspec.loader.exec_module(vmod)
version = getattr(vmod, '__version__')

# If the environment has a build number set...
if os.getenv('buildnum') is not None:
    # ...append it to the version.
    version = "{version}.{buildnum}".format(
        version=version,
        buildnum=os.getenv('buildnum')
    )

setup(
    name='{{cookiecutter.package_name}}',
    description="{{cookiecutter.project_description}}",
    long_description=long_description,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version=version,
    install_requires=[
        # Include dependencies here
        'click>=7.0,<8'
    ],
    entry_points="""
    [console_scripts]
    {{cookiecutter.cli_name}}={{cookiecutter.package_name}}.cli:cli
    """,
    python_requires=">={{cookiecutter.project_version}}",
    license={% if cookiecutter.license != "None" %}'{{cookiecutter.license}}'{% else %}None{% endif %},  # noqa
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    # Use the URL to the github repo.
    url= 'https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.package_name}}',
    download_url=(
        f'https://github.com/{{cookiecutter.github_user}}/'
        f'{{cookiecutter.package_name}}/archive/{version}.tar.gz'
    ),
    keywords=[
        # Add package keywords here.
    ],
    # See https://PyPI.python.org/PyPI?%3Aaction=list_classifiers
    classifiers=[
      # How mature is this project? Common values are
      #   3 - Alpha
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 3 - Alpha',

      # Indicate who your project is intended for.
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Libraries',

      # Pick your license.  (It should match "license" above.)
      {% if cookiecutter.license != 'None' %}  # noqa
        '''License :: OSI Approved :: {{cookiecutter.license}} License''',
      {% else %}'''License :: OSI Approved :: <Your Preferred License>''',  # noqa
      {%endif%}  # noqa

      # Specify the Python versions you support here. In particular, ensure
      # that you indicate whether you support Python 2, Python 3 or both.
      'Programming Language :: Python :: {{cookiecutter.python_version}}',
    ],
    include_package_data=True
)
