.. {{cookiecutter.project_name}} documentation master file
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{cookiecutter.project_name}}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{cookiecutter.project_description}}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   api
   development
   requirements



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
