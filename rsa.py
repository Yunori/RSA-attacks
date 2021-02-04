from genprivkey import genprivkey
from genpubkey import genpubkey
from genrandomstring import genrandomstring
from randomprime import randomprime
from rsadecrypt import rsadecrypt
from rsaencrypt import rsaencrypt

def rsa():
    plaintxt = genrandomstring(128)
    # PRIME NUMBERS GENERATION + PRIMALITY TESTS
    p1 = randomprime()
    p2 = randomprime()
    while p1 == p2:
        p2 = randomprime()

    # GET KEYS
    print("[INFO] random prime numbers are", p1, "and", p2, '\n')
    pubkey = genpubkey(p1, p2)
    print("[INFO] exponent is", pubkey.exp, "and modulo is", pubkey.mod, '\n')
    privkey = genprivkey(pubkey.exp, (p1 - 1) * (p2 - 1), p1 * p2)
    print("[INFO] inverse modular of e,phi(n) is", privkey.modinv, '\n')

    # ENCRYPT / DECRYPT
    print("[INFO] Plain text START")
    print(plaintxt)
    print("[INFO] Plain text END\n")
    ciphertxt = rsaencrypt(plaintxt, pubkey, False)
    print("[INFO] Cipher text = ", ciphertxt, '\n')
    result = rsadecrypt(ciphertxt, privkey)
    print("[INFO] Deciphered text START")
    print(result)
    print("[INFO] Deciphered text END\n")
