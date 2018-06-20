#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_cli.py
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This module contains tests of the click command line application.

.. note::

    To learn more about Click testing visit the
    `project documentation <http://click.pocoo.org/5/testing/>`_.
"""

import unittest
from click.testing import CliRunner, Result
import {{cookiecutter.project_slug}}.cli as cli


class TestCliSuite(unittest.TestCase):
    """
    This is a set of starter tests for the initial commands in the
    :py:module:`clickme.cli` module.
    """
    def test_noArguments_greet_defaultOutput(self):
        """
        Arrange: Supply no arguments.
        Act: Run the `greet` subcommand.
        Assert: Default output.
        :return:
        """
        runner: CliRunner = CliRunner()
        result: Result = runner.invoke(cli.greet)
        self.assertEqual(0, result.exit_code)
        self.assertEqual("Hello World!\n", result.output)

    def test_verbose_greet_verboseOutput(self):
        """
        Arrange: Supply the `--verbose` argument to the `cli` group command.
        Act: Call the `greet` subcommand.
        Assert: Verbose output.
        :return:
        """
        runner: CliRunner = CliRunner()
        # Note: To run a subcommand with arguments to the group, we must run the
        # group and pass the name of the subcommand as an argument.
        result: Result = runner.invoke(cli.cli, ['--verbose', 'greet'])
        self.assertEqual(0, result.exit_code)
        self.assertIn("The CLI is running in verbose mode.",
                      result.output)


if __name__ == '__main__':
    unittest.main()
