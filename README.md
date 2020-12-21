# Cookiecutter Click

![](https://github.com/patdaburu/cookiecutter-click/workflows/Build/badge.svg)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![](https://pyup.io/repos/github/patdaburu/cookiecutter-click/shield.svg)
![](https://pyup.io/repos/github/patdaburu/cookiecutter-click/python-3-shield.svg)

## Powered by [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/), Cookiecutter Click generates boilerplate for production-ready [command-line interface (CLI)](http://click.pocoo.org/5/) applications.

## Features

The project you create from this template has a few features to be aware of
including:

* A [Click](http://click.pocoo.org/5/) application to get you going
* [Pytest](https://docs.pytest.org/en/latest/) unit tests
* A documentation project based on
  [Sphinx](http://www.sphinx-doc.org/en/master/usage/quickstart.html).

## Usage

Let's pretend you want to create a CLI tool called "redditcli". Rather than
using standard lib argparse and then editing mundane details to include your
basic cli tool configuration that always get forgotten until the worst possible
moment, get cookiecutter to do all the work.

First, get Cookiecutter. Trust me, it's awesome:

``` bash
pip install "cookiecutter>=1.4.0"`
```

Now run it against this repo:

``` bash
cookiecutter https://github.com/patdaburu/cookiecutter-click
```

You'll be prompted for some values. Provide them, then a cli tool will be
created for you.

Warning: After this point, change 'Vlad Doster', 'vladdoster', etc to your own
information.

Answer the prompts with your own desired options. For example:

``` bash
Cloning into 'cookiecutter-click'...
remote: Counting objects: 550, done.
remote: Compressing objects: 100% (310/310), done.
remote: Total 550 (delta 283), reused 479 (delta 222)
Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
Resolving deltas: 100% (283/283), done.
project_name [my-click-project]: Reddit CLI
package_name [my-click-project]: reddit_cli
cli_name [my_click_project]: reddit-cli
project_version [0.0.1]: 0.0.1
project_description [This is my click command-line app]: Browse Reddit from a cli tool!
Select python_version:
1 - 3.6
2 - 3.7
3 - 3.8
Choose from 1, 2, 3 (1, 2, 3) [1]: 1
Select virtualenv:
1 - virtualenv
2 - python3
Choose from 1, 2 (1, 2) [1]: 1
Select linter:
1 - flake8
2 - pylint
Choose from 1, 2 (1, 2) [1]:
Select sphinx_theme:
1 - alabaster
2 - readthedocs
Choose from 1, 2 (1, 2) [1]: 1
Select auto_readme:
1 - None
2 - pandoc
Choose from 1, 2 (1, 2) [1]: 1
author_name [my_name]: Vlad Doster
author_email [my_email]: mvdoster@gmail.com
Select license:
1 - MIT
2 - BSD
3 - GPLv3
4 - Apache Software License 2.0
5 - None
Choose from 1, 2, 3, 4, 5 (1, 2, 3, 4, 5) [1]: 1
github_user [my_github_user]: vladdoster
```

Enter the project and take a look around:

``` bash
cd reddit_cli/
source venv/bin/activate
reddit_cli --help
ls -a
```

Create a git repo and push it there:

``` bash
git init
git add .
git commit -m "first awesome commit"
git remote add origin git@github.com:vladdoster/reddit_cli.git
git push -u origin master
```

## `make` Targets

The template contains a cookiecutter [post-generate
hook](http://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html) that
will attempt to do the following using targets in the project's
[Makefile](https://www.gnu.org/software/make/):

You may want to go about this differently according to your processes, but if
you want to create a virtual environment for the project, install the
dependencies, and set up the comman-line application, you can use the `make`
targets defined in the project like so.

There are several other `make` targets so have a look at the `Makefile` if
you're interested.

``` bash
cd <project-name>
make venv
make install
make build
```

## Run the Command-Line App

If you have performed the steps above, you should now be able to run the
application by the project name.

``` bash
<project-name> --help
```

If you get the template help message, you're ready to start building.

## Resources

Would you like to learn more?  Check out the links below!

* [Cookiecutter Project
  Documentation](https://cookiecutter.readthedocs.io/en/latest/)
* [Cookiecutter: Project Templates Made
  Easy](https://www.pydanny.com/cookie-project-templates-made-easy.html)
* [Click](http://click.pocoo.org/5/)
* [Pytest](https://docs.pytest.org/en/latest/)
* [Sphinx](http://www.sphinx-doc.org/en/master/usage/quickstart.html)

## Author

This program was created by [Pat Daburu](https://github.com/patdaburu). 

This project is [hosted on GitHub](https://github.com/patdaburu/cookiecutter-click). Please feel free to submit pull requests.

## Contributors

| name        | github link                   |
|-------------|-------------------------------|
| Vlad Doster | https://github.com/vladdoster |

## License

Copyright © 2018–2020 Pat Daburu. This program is released under the GPLv3 license, which you can find in the file [LICENSE](LICENSE).
