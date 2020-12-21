#!/usr/bin/env python
import os

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

def remove_pylintrc_file():
    os.remove(".pylintrc")
    
def remove_flake8_file():
    os.remove(".pylintrc")

def main():
    linter = "{{ cookiecutter.linter }}".lower()
    if linter == "flake8":
        remove_pylintrc_file()
    if linter == "pylint":
        remove_flake8_file()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
