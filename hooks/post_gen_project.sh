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
    ____                       ____                             
   / ___|  ___   ___          / ___| ___   _ __ ___   _ __ ___  
  | |  _  / _ \ / _ \  _____ | |    / _ \ | '_ ` _ \ | '_ ` _ \ 
  | |_| ||  __/| (_) ||_____|| |___| (_) || | | | | || | | | | |
   \____| \___| \___/         \____|\___/ |_| |_| |_||_| |_| |_|
                                                                
LOGO

echo -e "\033[1m\033[4mNext Steps\033[0m"
echo -e "\033[32mcd {{cookiecutter.project_slug}}\033[0m"
echo -e "\033[32msource venv/bin/activate\033[0m"
echo -e "\033[32m{{cookiecutter.cli_name}} --help\033[0m"