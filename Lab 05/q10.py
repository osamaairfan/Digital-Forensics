import os
import socket


def xor(message, key):

    message = bytes.fromhex(message)
    key = key.encode()

    xor_key = (key * (len(message) // len(key) + 1))[:len(message)]

    result = bytes([a ^ b for a, b in zip(message, xor_key)])

    return result.decode()


def main():
    HOST = ''
    PORT = 5555
    KEY = "super_secret_key"
    
    print(xor("1616180a527d150902151e176f05020b1201033a43392c1c53073a196b0f562642012f1143331f3a0b41174700080d4d1e050d47522353120b1d04193661", KEY))


if __name__ == "__main__":
    main()
