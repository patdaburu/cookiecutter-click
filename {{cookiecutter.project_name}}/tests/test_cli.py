#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_cli
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This is the test module for the project's command-line interface (CLI)
module.
"""
import logging
from click.testing import CliRunner, Result
import {{cookiecutter.package_name}}.cli as cli
from {{cookiecutter.package_name}} import __version__

# To learn more about testing Click applications, visit the link below.
# http://click.pocoo.org/5/testing/

"""
This case contains tests of the command-line interface (CLI).
"""
def test_version_displaysLibraryVersion():
    """
    Arrange/Act: Run the `version` subcommand.
    Assert: The output matches the library version.
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ['version'])
    assert (
        __version__ in result.output.strip(),
        'Version number should match library version.'
    )

def test_verbose_outputVerbose():
    """
    Arrange/Act: Run the `version` subcommand with the '-v' flag.
    Assert: The output indicates verbose logging is enabled.
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ['-v', 'version'])
    assert (
        'Verbose' in result.output.strip(),
        'Verbose logging should be indicated in output.'
    )

def test_hello_displaysExpectedMessage():
    """
    Arrange/Act: Run the `version` subcommand.
    Assert:  The output matches the library version.
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ['hello'])
    assert (
        '{{cookiecutter.cli_name}}' in result.output.strip(),
        "'Hello' messages should contain the CLI name."
    )

if __name__ == '__main__':
    unittest.main()
