from base64 import b64encode, b64decode
from mx_crypto import MxCrypto
from wallet import Wallet

w = Wallet()

public_key = w.public_key
private_key = w.private_key

print(public_key)
print(private_key)


def test_decrypt():
    msg = b"hello world!"
    encrypted = MxCrypto.encrypt(public_key, msg)
    original = MxCrypto.decrypt(private_key, encrypted)

    assert msg == original


def test_sign():
    bytes = b"Hello world!"

    signature = MxCrypto.sign(private_key, bytes)
    verify = MxCrypto.verify(public_key, bytes, signature)

    altered_bytes = b"Hello woorld!"
    altered_verify = MxCrypto.verify(public_key, altered_bytes, signature)

    assert verify == True
    assert altered_verify == False


# msg1_str = "Hello Tony, I am Jarvis!"
# msg1 = b"Hello Tony, I am Jarvis!"
# msg2 = b"Hello Toni, I am Jarvis!"

# encrypted = b64encode(w.encrypt(msg1))
# decrypted = w.decrypt(b64decode(encrypted))

# print(decrypted)
# print(w.sign(msg1_str.encode('utf-8')))
# signature = b64encode()
# verify = w.verify(msg1, b64decode(signature), w.public_key)
# print(verify)
