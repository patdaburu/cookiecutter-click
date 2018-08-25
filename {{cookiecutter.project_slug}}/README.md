# {{cookiecutter.package_name}}

{{cookiecutter.project_description}}

## Project Features

* [{{cookiecutter.package_name}}](http://www.comingsoon.net)
* a [Click](http://click.pocoo.org/5/) command-line application that you can use to generate hashes
* automated unit tests you can run with [pytest](https://docs.pytest.org/en/latest/)
* a [Sphinx](http://www.sphinx-doc.org/en/master/) documentation project

## Getting Started

The project's documentation contains a section to help you [get started](http://www.comingsoon.net) as a developer on the project.

## Prerequisites

To work with this project you'll need a few things.

* [Python GDAL/OGR](https://pcjericks.github.io/py-gdalogr-cookbook/)
* [GNU Make](https://www.gnu.org/software/make/)

## Resources

Below are some handy resource links.

* [Project Documentation](http://docs.daburu.net.s3-website.us-east-2.amazonaws.com/gc_shapehash/0.0.1/html/index.html#)
* [Click](http://click.pocoo.org/5/) is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary.
* [Sphinx](http://www.sphinx-doc.org/en/master/) is a tool that makes it easy to create intelligent and beautiful documentation, written by Geog Brandl and licnsed under the BSD license.
* [pytest](https://docs.pytest.org/en/latest/) helps you write better programs.
* [GNU Make]  is a tool which controls the generation of executables and other non-source files of a program from the program's source files.


## Authors

* **{{cookiecutter.author_name}}** - *Initial work* - [github](https://github.com/{{cookiecutter.github_user}})

See also the list of [contributors](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_slug}}/contributors) who participated in this project.

## License

{%- if cookiecutter.license == "MIT" -%}
MIT License

Copyright (c) {{cookiecutter.github_user}}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
{%- else -%}
Copyright (c) {{cookiecutter.author_name}}

All righs reserved.
{%- endif -%}