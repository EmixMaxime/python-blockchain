import json
from time import time
import hashlib

MINING_DIFFICULTY = 2


class Block(object):

    def __init__(self, nonce, transactions, index, previous_hash):
        self.index = index
        self.nonce = nonce
        self.transactions = transactions
        self.timestamp = time()
        self.previous_hash = previous_hash

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        """

        if not isinstance(block, Block):
            raise ValueError(
                'block should be a Block instance but its .', type(block))

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block.__dict__, sort_keys=True).encode()

        # @TODO: algorithm of hash as class parameter.
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def valid_proof(last_proof, last_hash, nonce, difficulty=MINING_DIFFICULTY):
        """
        Validates the Proof of work
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :param last_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{nonce}{last_hash}'.encode()

        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:difficulty] == '0'*difficulty

    @staticmethod
    def proof_of_work(last_block):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof

        :param last_block: <dict> last Block
        :return: <int>
        """

        last_nonce = last_block.nonce
        last_hash = Block.hash(last_block)

        nonce = 0
        while Block.valid_proof(last_nonce, last_hash, nonce) is False:
            nonce += 1

        return nonce
