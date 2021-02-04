from modpow import modpow


def rsadecrypt(ciphertxt, privkey):
    aux = [str(modpow(char, privkey.modinv, privkey.mod)) for char in ciphertxt]
    plain = [chr(int(char)) for char in aux]
    return ''.join(plain)
