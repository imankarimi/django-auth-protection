Django Auth Protection Documentation
##########################################

Logout users when the passwords changed in REST API.

Why Django Auth Protection?
==============================

Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework. It aims to cover the most common use cases of JWTs by offering a conservative set of default features. It also aims to be easily extensible in case a desired feature is not present. But one of the problems is that when the users change the password, they can continue to work on the system with the previous token until it expires. This package overrides the Simple JWT to solve this problem.

Contents:
=========

.. toctree::
   :maxdepth: 2

   requirements
   installation

I would love to hear your feedback on this package. If you run into
problems, please file an issue on GitHub_, or contribute to the project by
forking the repository and sending some pull requests.

.. _GitHub: https://github.com/imankarimi/django-auth-protection/issues
