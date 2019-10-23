from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
from base64 import b64encode, b64decode

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key


class Wallet:
    """
    Manage my priv/pub key.
    """

    def __init__(self):
        try:
            public_key, private_key = Wallet._import_keys()
        except FileNotFoundError:
            public_key, private_key = Wallet.generate_keys()

        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate_keys():
        public_key, private_key = Wallet._new_keys(2048)
        Wallet._save_key(public_key, private_key)

        return public_key, private_key

    @staticmethod
    def _new_keys(keysize):
        private_key = RSA.generate(keysize)
        public_key = private_key.publickey()

        return public_key, private_key

    @staticmethod
    def _save_key(public_key, private_key):
        # Converting the RsaKey objects to string
        private_pem = private_key.export_key().decode()
        public_pem = public_key.export_key().decode()

        # Writing down the private and public keys to 'pem' files
        with open('./keys/private.pem', 'w') as pr:
            pr.write(private_pem)
        with open('./keys/public.pem', 'w') as pu:
            pu.write(public_pem)

        # DOESN'T WORK
        # Thanks https://stackoverflow.com/questions/9197507/saving-rsa-keys-to-a-file-using-pycrypto
        # with open("./keys/private.pem", "w") as prv_file:
        #     print("{}".format(private_key.exportKey(format='PEM')), file=prv_file)

        # with open("./keys/public.pem", "w") as pub_file:
        #     print("{}".format(public_key.exportKey(format='PEM')), file=pub_file)

    @staticmethod
    def _import_keys():
        """
        Importing keys from files, converting it into the RsaKey object 
        """
        private_key = RSA.import_key(open('./keys/private.pem', 'r').read())
        public_key = RSA.import_key(open('./keys/public.pem', 'r').read())

        return public_key, private_key

    def crypt(self, message):
        # Instantiating PKCS1_OAEP object with the public key for encryption
        cipher = PKCS1_OAEP.new(key=self.public_key)
        cipher_text = cipher.encrypt(message)

        return cipher_text

    def decrypt(self, encrypted_message):
        # Instantiating PKCS1_OAEP object with the private key for decryption
        decrypt = PKCS1_OAEP.new(key=self.private_key)
        return decrypt.decrypt(encrypted_message)
