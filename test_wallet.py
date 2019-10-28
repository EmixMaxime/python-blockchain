from base64 import b64encode, b64decode
from wallet import Wallet

w = Wallet()


def test_decrypt():
    msg = b"hello world!"
    crypted = w.encrypt(b"hello world!")
    original = w.decrypt(crypted)

    assert msg == original


def test_sign():
    bytes = b"Hello world!"
    signature = w.sign(bytes)
    verify = w.verify(message=bytes, signature=signature, pub_key=w.public_key)

    altered_bytes = b"Hello woorld!"
    altered_verify = w.verify(message=altered_bytes,
                              signature=signature, pub_key=w.public_key)

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
