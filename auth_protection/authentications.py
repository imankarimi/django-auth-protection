from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

from auth_protection.utils import get_protect_key


class JWTAuthProtection(JWTAuthentication):
    """
    This class will check the user token, If the user password is changed, the user will be logout from the system.
    """

    def get_user(self, validated_token):
        user = super().get_user(validated_token)

        if validated_token.get('protect_key') != get_protect_key(user):
            raise InvalidToken(_('Token contained no recognizable user identification'))

        return user
