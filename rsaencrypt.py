from modpow import modpow


def rsaencrypt(plaintxt, pubkey, isint):
    if isint:
        cipher = [modpow(char, pubkey.exp, pubkey.mod) for char in plaintxt]
    else:
        cipher = [modpow(ord(char), pubkey.exp, pubkey.mod) for char in plaintxt]

    return cipher
