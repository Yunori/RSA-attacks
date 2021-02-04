from PublicKey import PublicKey
from genrandomstring import genrandomstring
from getrandom import getrandom
from modinv import modinv
from randomprime import randomprime
from rsaencrypt import rsaencrypt


def franklinreiter():
    plaintxt = genrandomstring(128)
    p1 = randomprime()
    p2 = randomprime()
    while p1 == p2:
        p2 = randomprime()
    mod = p1 * p2
    crpubkey = PublicKey(3, mod)
    cipher1 = []
    cipher2 = []
    r = 0
    while r == 0:
        r = getrandom(4)
    plaintxt = list(plaintxt)

    for i in plaintxt:
        cipher1.append(ord(i))
        cipher2.append(ord(i) + r)

    enccipher1 = rsaencrypt(cipher1, crpubkey, True)
    enccipher2 = rsaencrypt(cipher2, crpubkey, True)

    a = 1
    # ATTACK
    result = ""
    for i in range(0, len(enccipher1)):
        f = r * (enccipher2[i] + 2 * (a ** 3) * enccipher1[i] - r ** 3) % mod
        print("[ATTACK] f =", f)
        g = a * (enccipher2[i] - a ** 3 * enccipher1[i] + 2 * r ** 3) % mod
        print("[ATTACK] g =", g)
        # f / g: f / g = f * g**(-1) = f * inverse_mod(g, n)
        gi = modinv(g, mod)
        print("[ATTACK] gi =", gi)
        m = f * gi % mod
        result = result + chr(m)
    print(result)
