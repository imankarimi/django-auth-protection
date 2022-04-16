# Django Auth Protection
**Django Auth Protection** This package logout users from the system by changing the password in REST API.

<br />

## Why Django Auth Protection?
Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework. It aims to cover the most common use cases of JWTs by offering a conservative set of default features. It also aims to be easily extensible in case a desired feature is not present. But one of the problems is that when the users change the password, they can continue to work on the system with the previous token until it expires. This package overrides the Simple JWT to solve this problem.

<br>

## How to use it

<br />

* Download and install latest version of Django Auth Protection:

```bash
$ pip install django-auth-protection
# or
$ easy_install django-auth-protection
```

Then you have to create a custom `TokenObtainPairView` class and change the `serializer_class` to `ProtectTokenObtainPairSerializer` (follow the sample):

- Make a custom `TokenObtainPairView` and change the `serializer_class`:
```python
from auth_protection.utils import ProtectTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = ProtectTokenObtainPairSerializer
```

- Change All `authentication_classes` on your views and replace it with `JWTAuthProtection`:
```python
from auth_protection.utils import JWTAuthProtection


class SampleView(TARGET_VIEW):
    authentication_classes = [JWTAuthProtection]
```