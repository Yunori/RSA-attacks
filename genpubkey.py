from randomexponent import randomexponent
from PublicKey import PublicKey


def genpubkey(p1, p2):
    phi = (p1 - 1) * (p2 - 1)
    return PublicKey(randomexponent(phi), p1 * p2)
