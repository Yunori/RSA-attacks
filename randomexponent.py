from getrandom import getrandom
from gcd import gcd


def randomexponent(phi):
    e = 0
    good = False
    while not good:
        e = getrandom(16)
        e = e % 19193
        e += 46341
        e += 1 - e % 2
        if e > 65535:
            e = 46341
        while gcd(e, phi) != 1:
            e = e + 2
        if e <= phi:
            good = True
    return e
