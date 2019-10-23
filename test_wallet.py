from wallet import Wallet

w = Wallet()


def test_decrypt():
    msg = b"hello world!"
    crypted = w.crypt(b"hello world!")
    original = w.decrypt(crypted)

    assert msg == original
