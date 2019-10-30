from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
from base64 import b64encode, b64decode
import hashlib
from Crypto.Hash import SHA256


class MxCrypto:
    @staticmethod
    def sign(private_key, bytes):
        signer = PKCS1_v1_5.new(private_key)
        digest = SHA256.new(bytes)
        return signer.sign(digest)

    @staticmethod
    def verify(pub_key, message, signature):
        """
        Check that the provided signature corresponds to transaction
        signed by the public key (sender_pubkey)
        """
        signer = PKCS1_v1_5.new(pub_key)
        digest = SHA256.new(message)
        return signer.verify(digest, signature)

    @staticmethod
    def encrypt(public_key, message):
        # Instantiating PKCS1_OAEP object with the public key for encryption
        cipher = PKCS1_OAEP.new(public_key)
        return cipher.encrypt(message)

    @staticmethod
    def decrypt(private_key, encrypted_message):
        # Instantiating PKCS1_OAEP object with the private key for decryption
        decrypt = PKCS1_OAEP.new(private_key)
        return decrypt.decrypt(encrypted_message)
