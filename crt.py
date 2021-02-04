from egcd import egcd


def crt(items):
    # Determine N, the product of all n_i
    N = 1
    for a, n in items:
        N *= n

    # Find the solution (mod N)
    result = 0
    for a, n in items:
        m = N // n
        d, r, s = egcd(n, m)
        if d != 1:
            raise Exception("Input not pairwise co-prime")
        result += a * s * m

    return result % N
