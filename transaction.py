from collections import OrderedDict
import hashlib

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
from base64 import b64encode, b64decode
from Crypto.Hash import SHA256
from mx_crypto import MxCrypto
import json
import jsonpickle


class Transaction:

    def __init__(self, sender_address, recipient_address, value):
        # @ = public keys
        self.sender_address = sender_address
        self.recipient_address = recipient_address

        self.value = value
        self.signature = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        
        return False

    def to_dict(self):
        return OrderedDict({'sender_address': self.sender_address,
                            'recipient_address': self.recipient_address,
                            'value': self.value})

    def toJSON(self):
        # return json.dumps({
        #     'sender_address': self.sender_address,
        #     'recipient_address': self.recipient_address,
        #     'value': self.value
        # }, sort_keys=True)
        return jsonpickle.encode(self)

    @property
    def to_sign(self):
        return jsonpickle.encode({'sender_address': self.sender_address,
                                  'recipient_address': self.recipient_address,
                                  'value': self.value}).encode()

    def sign(self, wallet):
        self.signature = wallet.sign_transaction(self.to_sign)

    def verify_signature(self):
        """
        Check that the provided signature corresponds to transaction
        signed by the public key (sender_address)
        """

        # sender_address = string. I need RSA Object.
        pubkey = RSA.import_key(self.sender_address)
        return MxCrypto.verify(pubkey, self.to_sign, self.signature)
