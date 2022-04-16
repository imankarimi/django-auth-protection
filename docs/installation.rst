Installation
============

* Download and install latest version of `Django Auth Protection`_:

.. code-block:: console

    $ pip install django-auth-protection


How to use it
--------------

Then you have to create a custom ``TokenObtainPairView`` class and change the ``serializer_class`` to ``ProtectTokenObtainPairSerializer`` (follow the sample):

* Make a custom ``TokenObtainPairView`` and change the ``serializer_class``:

.. code-block:: python

    from auth_protection.serializers import ProtectTokenObtainPairSerializer


    class CustomTokenObtainPairView(TokenObtainPairView):
        serializer_class = ProtectTokenObtainPairSerializer

* Change All ``authentication_classes`` on your views and replace it with ``JWTAuthProtection``:

.. code-block:: python

    from auth_protection.authentications import JWTAuthProtection


    class SampleView(TARGET_VIEW):
        authentication_classes = [JWTAuthProtection]

.. _Django Auth Protection: https://pypi.org/project/django-auth-protection/
