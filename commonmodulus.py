from PublicKey import PublicKey
from egcd import egcd
from gcd import gcd
from genrandomstring import genrandomstring
from modinv import modinv
from modpow import modpow
from randomexponent import randomexponent
from randomprime import randomprime
from rsaencrypt import rsaencrypt


def commonmodulus():
    plaintxt = genrandomstring(128)
    p1 = randomprime()
    p2 = randomprime()
    while p1 == p2:
        p2 = randomprime()
    print("[INFO] random prime numbers are", p1, "and", p2, '\n')
    phi = (p1 - 1) * (p2 - 1)
    e1 = randomexponent(phi)
    e2 = randomexponent(phi)
    while e1 == e2 != 1 or egcd(e1, e2)[0] != 1 or egcd(e1, p1*p2)[0] != 1 or egcd(e2, p1*p2)[0] != 1:
        e2 = randomexponent(phi)
    print("[INFO] exponent 1 is", e1, "and exponent 2 is", e2, '\n')
    mod = p1 * p2
    print("[INFO] modulo is", mod, '\n')
    print("[INFO] Plain text START")
    print(plaintxt)
    print("[INFO] Plain text END\n")
    c1 = rsaencrypt(plaintxt, PublicKey(e1, mod), False)
    c2 = rsaencrypt(plaintxt, PublicKey(e2, mod), False)
    print("[INFO] Cipher text 1 = ", c1, '\n')
    print("[INFO] Cipher text 2 = ", c2, '\n')
    x = modinv(e1, e2)
    y = (gcd(e1, e2) - e1 * x) / e2
    result = ""
    for i in range(0, len(c1)):
        temp = modinv(c2[i], mod)
        print("[ATTACK] modinv c =", temp)
        m1 = modpow(c1[i], x, mod)
        print("[ATTACK] exp mod c1^x =", m1)
        m2 = modpow(temp, -y, mod)
        print("[ATTACK] exp mod temp-y =", m2)
        result = result + chr((m1 * m2) % mod)
    print("[INFO] Deciphered text START")
    print(result)
    print("[INFO] Deciphered text END\n")
