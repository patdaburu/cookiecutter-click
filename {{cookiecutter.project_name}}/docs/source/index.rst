.. {{cookiecutter.package_name}} documentation master file
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: _static/images/logo.svg
   :width: 150px
   :alt: {{cookiecutter.package_name}}
   :align: right

{{cookiecutter.package_name}}
{% for _ in cookiecutter.package_name %}={% endfor %}

{{cookiecutter.project_description}}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   cli
   api
   development
   requirements


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
