import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4
from collections import OrderedDict

from block import Block
from transaction import Transaction
from wallet import Wallet
from node import Node

"""
Lq je reçois une transaction je dois la validera avant de l'enregister dans mon block.
Lq je créé une transaction, c'est différent.
"""

"""
Our Blockchain class is responsible for managing the chain. It will store transactions and have some helper methods for adding new blocks to the chain.
"""

MINING_SENDER = "THE BLOCKCHAIN"


class Blockchain():

    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        # Create the genesis block
        self.new_block(100, '1')

    def register_node(self, node):
        """
        Add a new node to the list of nodes.
        """
        if not isinstance(node, Node):
            raise ValueError('node parameter should be a Node instance.')

        self.nodes.add(node)

    @property
    def last_block(self):
        return self.chain[-1]

    def submit_transaction(self, transaction, signature):
        """
        Add a transaction to transactions array if the signature verified
        Return index of block that the transaction will be.
        """
        if not isinstance(transaction, Transaction):
            raise ValueError(
                'transaction parameter should be a Transaction instance.')

        transaction_verification = transaction.verify_signature(signature)

        if transaction_verification:
            self.current_transactions.append(transaction)
            return len(self.chain) + 1

        return False

    def new_block(self, nonce, previous_hash):
        """
        Create a new Block in the Blockchain
        :param nonce: The nonce given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        # Why we have this OR condition? Seems useless.
        block = Block(nonce, self.current_transactions, len(self.chain) +
                      1, previous_hash or Block.hash(self.chain[-1]))

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: A blockchain
        :return: True if valid, False if not
        """

        last_block = chain[0]

        current_index = 1
        lenChain = len(chain)

        while current_index < lenChain:
            current_block = chain[current_index]

            # Check with last_block & current_block

            print(f'{last_block}')
            print(f'{current_block}')
            print("\n-----------\n")

            # Check that the hash of the block is correct
            last_block_hash = Block.hash(last_block)
            if current_block['previous_hash'] != last_block_hash:
                return False

            # Check that the Proof of Work is correct
            if not Block.valid_proof(last_block['proof'], current_block['proof'], last_block_hash):
                return False

            last_block = current_block
            current_index += 1

        return True

    def mine(self):
        """
        Take the last Block, mine it and add it to the Blockchain.
        """
        # We run the proof of work algorithm to get the next proof...
        last_block = self.last_block

        nonce = Block.proof_of_work(last_block)

        # @TODO
        # We must receive a reward for finding the proof.
        # The sender is "0" to signify that this node has mined a new coin.
        # blockchain.new_transaction(
        #     sender=MINING_SENDER,
        #     recipient=node_identifier,
        #     amount=1,
        # )

        # Forge the new Block by adding it to the chain
        previous_hash = Block.hash(last_block)
        block = self.new_block(nonce, previous_hash)

        response = {
            'message': "New Block Forged",
            'index': block.index,
            'transactions': block.transactions,
            'nonce': block.nonce,
            'previous_hash': block.previous_hash,
        }

        return response
