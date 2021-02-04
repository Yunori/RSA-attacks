from getrandom import getrandom
from fermatprimalitytest import fermatprimalitytest
from millerrabinprimalitytest import millerrabinprimalitytest


def randomprime():
    # random number between 46341 and 65535
    prime = getrandom(16)
    prime = prime % 19193
    prime += 46341
    prime += 1 - prime % 2
    if prime > 65521:
        prime = 65521
    while not fermatprimalitytest(prime, 40) or not millerrabinprimalitytest(prime, 40):
        prime = prime + 2
    return prime
