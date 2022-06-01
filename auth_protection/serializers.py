from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from auth_protection.utils import get_protect_key
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.exceptions import InvalidToken
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ProtectTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Protect TokenObtainPairSerializer: This class is a custom TokenObtainPairSerializer to detect change passwords and
     logout user when password changed in REST API
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['protect_key'] = get_protect_key(user)
        return token


class ProtectTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attr):
        refresh = RefreshToken(attr['refresh'])

        user = self.get_user(user_id=refresh.get('user_id'))

        if not refresh.get('protect_key') or (refresh.get('protect_key') != get_protect_key(user)):
            raise InvalidToken(_('Token contained no recognizable user identification'))

        return super(ProtectTokenRefreshSerializer, self).validate(attr)

    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise InvalidToken(_('Token contained no recognizable user identification'))
        return user
