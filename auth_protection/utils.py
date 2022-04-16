import hashlib


def get_protect_key(user):
    """
    Generate Protection Key based on user Password
    """
    return hashlib.md5(user.password.encode()).hexdigest().upper()
