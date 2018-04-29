#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_example.py
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This is a sample test module.
"""

from parameterized import parameterized
import unittest
import {{cookiecutter.project_slug}}


class ExampleTestSuite(unittest.TestCase):
    """
    This is just an example test suite.  It will check the current project version
    numbers against the original version numbers and will start failing as soon as
    the current version numbers change.
    """
    def test_import_getVersions_originalVersions(self):
        """
        Arrange: Load the primary module.
        Act: Retrieve the versions.
        Assert: The versions match the version numbers at the time of project creation.
        """
        self.assertEqual('{{cookiecutter.project_version}}', {{cookiecutter.project_slug}}.__version__)
        self.assertEqual('{{cookiecutter.project_version}}', {{cookiecutter.project_slug}}.__release__)


class ParamaterizedExampleTestSuite(unittest.TestCase):
    """
    This is just an example test suite that demonstrates the very useful
    `parameterized` module.  It contains a test in which the squares of the
    first two parameters are added together and passes if that sum equals the
    third parameter.
    """
    @parameterized.expand([
        (1, 2, 5),
        (3, 4, 25)
    ])
    def test_ab_addSquares_equalsC(self, a, b, c):
        """
        Arrange: Acquire the first two parameters (a and b).
        Act: Add the squares of the first two parameters (a and b).
        Assert: The sum of the squares equals the third parameter (c).

        :param a: the first parameter
        :param b: the second parameter
        :param c: the result of adding the squares of a and b
        """
        self.assertEqual(c, a*a + b*b)
