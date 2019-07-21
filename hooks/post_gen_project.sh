#!/usr/bin/env bash

if ! make venv; then
    echo ""
    echo -e "\e[1m\e[31mCannot create the virtual environment.\e[0m"
    echo ""
    echo -e "\e[1mIs python version {{cookiecutter.python_version}} installed?\e[0m"
    echo ""
    echo -e "\033[1m\033[4mNext Steps\033[0m"
    echo -e "Install python version {{cookiecutter.python_version}}."
    echo -e "Run cookiecutter again."
    echo ""
    exit 1
else
    source venv/bin/activate && make install && make build
fi

cat << "PYTHON"
                 .-------------------------.
                 |         .:::::.         |
                 |        :: ::::::        |
                 |        ````:::::        |
                 |  .:::::::::::::: iiii.  |
                 | :::::::::::::::: iiiiii |
                 | :::::: ..........iiiiii |
                 |  ':::: iiiiiiiiiiiiii'  |
                 |        iiiii....        |
                 |        iiiiii ii        |
                 |         'iiiii'         |
                 '-------------------------'
PYTHON


cat << "LOGO"
                 _       _
                | |     | |
              __| | __ _| |__  _   _ _ __ _   _
             / _` |/ _` | '_ \| | | | '__| | | |
            | (_| | (_| | |_) | |_| | |  | |_| |
             \__,_|\__,_|_.__/ \__,_|_|   \__,_|

LOGO

echo -e "\033[1m\033[4mNext Steps\033[0m"
echo -e "\033[32mcd {{cookiecutter.project_name}}\033[0m"
echo -e "\033[32msource venv/bin/activate\033[0m"
echo -e "\033[32m{{cookiecutter.cli_name}} --help\033[0m"
