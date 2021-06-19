#!/usr/bin/env python3
import os, subprocess

TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

def remove_file(f_name):
    os.remove(f_name)

def main():
    linter = "{{ cookiecutter.linter }}".lower()
    if linter != "flake8":
        remove_file(".flake8")
    if linter != "pylint":
        remove_file(".pylintrc")

    venv = "{{ cookiecutter.virtualenv }}".lower()
    if venv == "pipenv":
        subprocess.run(["pip3", "install", "pipenv"])
    if venv == "virtualenv":
        subprocess.run(["pip3", "install", "virtualenv"])

    print(f"{SUCCESS} Project initialized, keep up the good work!{TERMINATOR}")


if __name__ == "__main__":
    main()
