from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from auth_protection.utils import get_protect_key


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
