#!/usr/bin/env python3
import os, subprocess

TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def main():
    linter = "{{ cookiecutter.linter }}".lower()
    if linter == "flake8":
        os.remove(".pylintrc")
    if linter == "pylint":
        os.remove(".flake8")

    venv = "{{ cookiecutter.virtualenv }}".lower()
    if venv != "venv":
        subprocess.run(["pip3", "install", "--user", venv], check=True)

    print(f"{SUCCESS} CLI tool initialized, keep up the good work!{TERMINATOR}")


if __name__ == "__main__":
    main()
