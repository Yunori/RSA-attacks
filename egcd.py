def egcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        #(q, a), b = divmod(b, a), a
        q, a, b = b // a, b % a, a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0
