# cookiecutter-cli

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template designed to help you get started with your [command-line interface (CLI)](http://click.pocoo.org/5/) project.

## Getting Started

### Prerequisites

What things you need to install the software and how to install them

```bash
pip install cookiecutter
```

### Using the Template

#### Step One: Build the project.
You can build a project directly from the github repository.

```bash
cookiecutter https://github.com/patdaburu/cookiecutter-click
```

#### Run the `make` Targets

The template contains a cookiecutter [post-generate hook](http://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html) that will attempt to do the following using targets in the project's [Makefile](https://www.gnu.org/software/make/):

You may want to go about this differently according to your processes, but if you want to create a virtual environment for the project, install the dependencies, and set up the comman-line application, you can use the `make` targets defined in the project like so.

There are several other `make` targets so have a look at the `Makefile` if you're interested.

```bash
cd <project-name>
make venv
make install
make build
```

#### Run the Command-Line App

If you have performed the steps above, you should now be able to run the application by the project name.

```bash
<project-name> --help
```

If you get the template help message, you're ready to start building.

## Project Features

The project you create from this template has a few features to be aware of including:

* a [click](http://click.pocoo.org/5/) application to get you going;
* [pytest](https://docs.pytest.org/en/latest/) unit tests; and
* a documentation project based on [Sphinx](http://www.sphinx-doc.org/en/master/usage/quickstart.html).

## Resources

Would you like to learn more?  Check out the links below!

* [Cookiecutter Project Documentation](https://cookiecutter.readthedocs.io/en/latest/)
* [Cookiecutter: Project Templates Made Easy](https://www.pydanny.com/cookie-project-templates-made-easy.html)
* [Click](http://click.pocoo.org/5/)
* [pytest](https://docs.pytest.org/en/latest/)
* [Sphinx](http://www.sphinx-doc.org/en/master/usage/quickstart.html)


## Authors

* **Pat Daburu** - *Initial work* - [github](https://github.com/patdaburu)

See also the list of [contributors](https://github.com/patdaburu/cookiecutter-gc-cli/graphs/contributors) who participated in this project.

## License

All rights reserved.

