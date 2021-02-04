import secrets


def getrandom(size):
    prime = secrets.randbits(size)
    return prime
