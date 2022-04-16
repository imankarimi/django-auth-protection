import hashlib

from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ProtectTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Protect TokenObtainPairSerializer: This class is a custom TokenObtainPairSerializer to detect change passwords and
     logout user when password changed in REST API
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['protect_key'] = __get_protect_key(user)
        return token


class JWTAuthProtection(JWTAuthentication):
    """
    This class will check the user token, If the user password is changed, the user will be logout from the system.
    """

    def get_user(self, validated_token):
        user = super().get_user(validated_token)

        if validated_token.get('protect_key') != __get_protect_key(user):
            raise InvalidToken(_('Token contained no recognizable user identification'))

        return user


def __get_protect_key(user):
    """
    Generate Protection Key based on user Password
    """
    return hashlib.md5(user.password.encode()).hexdigest().upper()
