from commonmodulus import commonmodulus
from franklinreiter import franklinreiter
from hastadbroadcast import hastadbroadcast
from rsa import rsa


def main():
    # RSA test = 1
    # Common modulus attack = 2
    # Hastad broadcast attack = 3
    # Franklin-Reiter related-message attack = 4
    action = 4

    if action == 1:
        rsa()
    elif action == 2:
        commonmodulus()
    elif action == 3:
        hastadbroadcast()
    elif action == 4:
        franklinreiter()


main()
