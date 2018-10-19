#!/usr/bin/env bash
make venv && source venv/bin/activate && make install && make build

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
echo -e "\033[32mcd {{cookiecutter.package_name}}\033[0m"
echo -e "\033[32msource venv/bin/activate\033[0m"
echo -e "\033[32m{{cookiecutter.cli_name}} --help\033[0m"
