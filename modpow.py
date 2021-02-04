def modpow(a, n, p):
    res = 1
    a = a % p

    while n > 0:
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2

    return res % p
