# from gmpy2 import root

from PublicKey import PublicKey
from crt import crt
from egcd import egcd
from genrandomstring import genrandomstring
from randomprime import randomprime
from rsaencrypt import rsaencrypt


def hastadbroadcast():
    plaintxt = genrandomstring(128)
    good = False
    mod1, mod2, mod3 = 0, 0, 0
    while good is not True:
        p1 = randomprime()
        p2 = randomprime()
        mod1 = p1 * p2
        p3 = randomprime()
        p4 = randomprime()
        mod2 = p3 * p4
        p5 = randomprime()
        p6 = randomprime()
        mod3 = p5 * p6
        print("[INFO] random prime 1 numbers are", p1, "and", p2, '\n')
        print("[INFO] random prime 2 numbers are", p3, "and", p4, '\n')
        print("[INFO] random prime 3 numbers are", p5, "and", p6, '\n')
        print("[INFO] modulo 1 is", mod1, '\n')
        print("[INFO] modulo 2 is", mod2, '\n')
        print("[INFO] modulo 3 is", mod3, '\n')
        good = True
        if egcd(mod1, mod2)[0] != 1:
            print("mod1 & mod2 aren't coprime")
            good = False
        if egcd(mod1, mod3)[0] != 1:
            print("mod1 & mod3 aren't coprime")
            good = False
        if egcd(mod2, mod3)[0] != 1:
            print("mod2 & mod3 aren't coprime")
            good = False
    e = 3
    print("[INFO] exponent is", mod1, '\n')
    c1 = rsaencrypt(plaintxt, PublicKey(e, mod1), False)
    c2 = rsaencrypt(plaintxt, PublicKey(e, mod2), False)
    c3 = rsaencrypt(plaintxt, PublicKey(e, mod3), False)
    print("[INFO] Plain text START")
    print(plaintxt)
    print("[INFO] Plain text END\n")
    print("[INFO] Cipher text 1 = ", c1, '\n')
    print("[INFO] Cipher text 2 = ", c2, '\n')
    print("[INFO] Cipher text 3 = ", c3, '\n')
    result = ""
    for i in range(0, len(c1)):
        crtres = crt([(c1[i], mod1), (c2[i], mod2), (c3[i], mod3)])
        print("[ATTACK] crt result =", crtres)
        crtroot = round(crtres ** (1 / e))
        print("[ATTACK] racine cubique =", crtroot)
        result = result + chr(round(crtroot))
    print("[INFO] Deciphered text START")
    print(result)
    print("[INFO] Deciphered text END\n")
