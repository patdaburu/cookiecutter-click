#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
.. currentmodule:: pre_gen_project
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This is the script that runs before template generation.
"""
import sys


module_name = "{{ cookiecutter.package_name }}"

if not module_name.isidentifier():
    sys.exit(f"ERROR: {module_name} is not a valid Python module name!")
