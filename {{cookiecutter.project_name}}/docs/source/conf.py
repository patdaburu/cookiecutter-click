# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys

# Determine the absolute path to the directory containing the python modules.
_pysrc = os.path.abspath(
    os.path.join(
        os.path.abspath(__file__), '..', '..', '..'
    )
)

# Insert it into the path.
sys.path.insert(0, _pysrc)
# Now we can import local modules.
import {{cookiecutter.package_name}}


# -- Project information -----------------------------------------------------

project = '{{cookiecutter.package_name}}'
copyright = '2019, {{cookiecutter.author_name}}'
author = '{{cookiecutter.author_name}}'

# The full version, incl{{cookiecutter.package_name}}uding alpha/beta/rc tags
release = {{cookiecutter.package_name}}.__release__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_theme_options = {
    'logo': 'logo.png',
    'github_user': '{{cookiecutter.github_user}}',
    'github_repo': '{{cookiecutter.project_name}}',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
