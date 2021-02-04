import secrets
from modpow import modpow


def fermatprimalitytest(n, k):
    if n == 1 or n == 4:
        return False
    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = secrets.randbelow(n - 1)
        if a < 1:
            a = 1

        #   if gcd(n, a) != 1:
            #   return False

        if modpow(a, n - 1, n) != 1:
            return False

    return True
