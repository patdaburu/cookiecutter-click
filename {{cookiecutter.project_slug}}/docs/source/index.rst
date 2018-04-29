.. modlit_template documentation master file
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: _static/images/logo.svg
   :width: 150px
   :alt: modlit_template
   :align: right

{{cookiecutter.project_slug}}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{cookiecutter.project_description}}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   requirements


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
