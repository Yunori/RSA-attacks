from PrivateKey import PrivateKey
from modinv import modinv


def genprivkey(e, phi, n):
    return PrivateKey(modinv(e, phi), n)
