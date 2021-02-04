import secrets
from modpow import modpow


def millerwitness(d, n):
    if n < 4:
        return False
    a = secrets.randbelow(n - 2)
    if a < 2 and n > 3:
        a = a + 2
    if a < 1:
        a = 1

    x = modpow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def millerrabinprimalitytest(n, k):
    # Corner cases
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Find r such that n = 2^d * r + 1 for some r >= 1
    d = n - 1
    while d % 2 == 0:
        d //= 2

    for i in range(k):
        if not millerwitness(d, n):
            return False

    return True
