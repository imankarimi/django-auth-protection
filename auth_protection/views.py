from rest_framework_simplejwt.views import TokenRefreshView

from auth_protection.serializers import ProtectTokenRefreshSerializer


class ProtectTokenRefreshView(TokenRefreshView):
    """
        Takes a refresh type JSON web token and returns an access type JSON web
        token if the refresh token is valid.
        """
    serializer_class = ProtectTokenRefreshSerializer
