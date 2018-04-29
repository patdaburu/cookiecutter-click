#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This is the entry point for the command-line interface (CLI) application.

.. note::

    To learn more about Click visit the `project website <http://click.pocoo.org/5/>`_.  There is
    also a very helpful `tutorial video <https://www.youtube.com/watch?v=kNke39OZ2k0>`_.
"""

import os
from pathlib import Path
from typing import TextIO
import click


class Info(object):
    """
    This is an information object that can be used to pass data between CLI functions.
    """
    def __init__(self):  # Note that this object must have an empty constructor.
        self.verbose: bool = False
        self.home_directory: os.PathLike = None


# pass_info is a decorator for functions that pass 'Info' objects.
pass_info = click.make_pass_decorator(Info, ensure=True) #: pylint: disable=invalid-name


@click.group()
@click.option('--verbose', is_flag=True, help="Turn on 'verbose' mode.")
@click.option('--home-directory', type=click.Path())
@pass_info
def cli(info: Info, verbose: bool, home_directory: os.PathLike):
    """
    This is a sample Click command-line application.
    """
    # If we're running in verbose mode...
    if verbose:
        # ...let's announce that.
        click.echo('The CLI is running in verbose mode.')
    # We'll also add it to the collection of information for the future.
    info.verbose = verbose
    # If no home directory is specified...
    if home_directory is None:
        # ...we'll specify one now.
        home_directory = Path.home()
    # Anybody else using the information we're passing will know this as well.
    info.home_directory = home_directory


@cli.command()  # This is a sub-command of 'cli'.
@click.option('--string', default='World', type=str,
              metavar='<string>',
              help="To whom would you like to say 'hello'?")
@click.option('--repeat', default=1, type=int,
              metavar='<repeat>',
              help='How many times should the greeting be repeated?')
@click.argument('out', type=click.File('w'), default='-', required=False)
@pass_info
def greet(info: Info, string: str, repeat: int, out: TextIO):
    """
    Print 'Hello <string>!' <repeat> times.
    """
    if info.verbose:
        click.echo("'greet' is running in verbose mode.")
    click.echo('Home directory is {}'.format(info.home_directory))
    for _ in range(0, repeat):
        click.echo('Hello {}!'.format(string), file=out)
