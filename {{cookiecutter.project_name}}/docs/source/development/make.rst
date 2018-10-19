.. _make:

.. image:: ../_static/images/logo.svg
   :width: 100px
   :alt: {{cookiecutter.package_name}}
   :align: right

.. toctree::
    :glob:

.. _using-the-makefile:

Using the `Makefile`
====================

This project includes a ``Makefile`` that you can use to perform common tasks such as running
tests and building documentation.

Targets
-------

This section contains a brief description of the targets defined in the ``Makefile``.

``clean``
^^^^^^^^^

Remove generated packages, documentation, temporary files, *etc*.

``lint``
^^^^^^^^

Run `pylint <https://www.pylint.org/>`_ against the project files.

``test``
^^^^^^^^

Run the unit tests.

``docs``
^^^^^^^^

Build the documentation for production.

``answers``
^^^^^^^^^^^

Perform a quick build of the documentation and open it in your browser.

``package``
^^^^^^^^^^^

Build the package for publishing.

.. _make-publish:

``publish``
^^^^^^^^^^^

Publish the package to your repository.

``build``
^^^^^^^^^

Install the current project locally so that you may run the command-line application.

``venv``
^^^^^^^^

Create a virtual environment.

``install``
^^^^^^^^^^^

Install (or update) project dependencies.

``licenses``
^^^^^^^^^^^^

Generate a report of the projects dependencies and respective licenses.

.. note::

    If project dependencies change, please update this documentation.
