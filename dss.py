import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64


def rsakeys():
    length = 1024
    privatekey = RSA.generate(length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey


def encrypt(rsa_publickey, plain_text):
    cipher_text = rsa_publickey.encrypt(plain_text, 32)[0]
    b64cipher = base64.b64encode(cipher_text)
    return b64cipher


def decrypt(rsa_privatekey, b64cipher):
    decoded_ciphertext = base64.b64decode(b64cipher)
    plaintext = rsa_privatekey.decrypt(decoded_ciphertext)
    return plaintext


def sign(privatekey, data):
    return base64.b64encode(str((privatekey.sign(data, ''))[0]).encode())


def verify(publickey, data, sign):
    return publickey.verify(data, (int(base64.b64decode(sign)),))


if __name__ == "__main__":
    privatekey, publickey = rsakeys()  # generating keys
    text = b"Hello baby!"  # Text to encrypt
    ct = encrypt(publickey, text)
    print(ct)
    dt = decrypt(privatekey, ct)  # decryption
    print(dt)
    sig = sign(privatekey, dt)
    print(sig)
    ver = verify(publickey, dt, sig)
    print(ver)
