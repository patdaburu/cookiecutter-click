#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: setup.py
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This file is used to create the package we'll publish to PyPI.
"""

import os
import {{cookiecutter.project_slug}}
from setuptools import setup, find_packages, Command  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

# Get the base version from the library.
version={{cookiecutter.project_slug}}.__version__

# If the environment has a build number set...
if os.getenv('buildnum') is not None:
    # ...append it to the version.
    version = "{version}.{buildnum}".format(version=version, buildnum=os.getenv('buildnum'))

setup(
  name='{{cookiecutter.project_slug}}',
  description="{{cookiecutter.project_description}}",
  long_description=long_description,
  packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
  version=version,
  install_requires=[
    # Include your dependencies here.
    # Here are a couple of examples...
    # 'numpy>=1.13.3,<2',
    # 'measurement>=1.8.0,<2'
    'Click'
  ],
  entry_points="""
    [console_scripts]
    {{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.cli:cli
  """,
  python_requires=">={{cookiecutter.project_version}}",
  license='{{cookiecutter.license}}',
  author='{{cookiecutter.author_name}}',
  author_email='{{cookiecutter.author_email}}',
  url='http://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/index.html',  # Use the URL to the github repo.
  download_url='https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_slug}}/archive/{version}.tar.gz'.format(version=version),
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

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',

    # Pick your license as you wish (should match "license" above)
    {%- if cookiecutter.license != "None" -%}
    'License :: OSI Approved :: {{cookiecutter.license}} License',
    {%- endif -%}

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: {{cookiecutter.license}}',
  ],
)
