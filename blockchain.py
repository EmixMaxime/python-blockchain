import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4
from collections import OrderedDict
import jsonpickle

from block import Block
from transaction import Transaction
from wallet import Wallet
from network.network import Network

"""
Lq je reçois une transaction je dois la validera avant de l'enregister dans mon block.
Lq je créé une transaction, c'est différent.
"""

"""
Our Blockchain class is responsible for managing the chain. It will store transactions and have some helper methods for adding new blocks to the chain.
"""

MINING_SENDER = "THE BLOCKCHAIN"
NB_TRANSACTIONS_MAX = 2


class Blockchain():

    def __init__(self, network):
        if not isinstance(network, Network):
            raise ValueError('network should be an instance of Network.')

        self.current_transactions = []
        self.chain = []
        self.nodes = set()
        self.network = network

        # Create the genesis block
        self._genesis_block()

    def _genesis_block(self):
        t1 = Transaction('@sender_address', '@recipient_address', 50)

        nonce = 55
        previous_hash = 0
        b1 = Block(nonce, t1, 0, 0)

        self.chain.append(b1)

        # genesis_hash = Block.hash(b1)
        # print('genesis_hash = ', genesis_hash)

    @property
    def last_block(self):
        return self.chain[-1]

    @property
    def chain_for_network(self):
        return jsonpickle.encode(self.chain)

    def submit_transaction(self, transaction):
        """
        Add a transaction to transactions array if the signature verified
        Return index of block that the transaction will be.
        """

        # from the network, is a str that contains a json.
        if isinstance(transaction, str):
            transaction = jsonpickle.decode(transaction)
            print('I received a new Transaction', transaction)
        else:
            print("I'm sending a new Transaction", transaction)

        if transaction == self.current_transactions:
            print('I received an transaction, but I already know it, so I ignore it.')
            return False

        if not isinstance(transaction, Transaction):
            raise ValueError(
                'transaction parameter should be a Transaction instance.')

        transaction_verification = transaction.verify_signature()

        self.network.broadcast_transaction(jsonpickle.encode(transaction))

        if transaction_verification:
            self.current_transactions.append(transaction)
            return len(self.chain) + 1

        # Should I mine?
        # if len(self.current_transactions) == NB_TRANSACTIONS_MAX:
            # self.mine() 

        return False

    def create_block(self, nonce, previous_hash):
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
        self.network.broadcast_block(jsonpickle.encode(block))

        return block

    def submit_block(self, block):
        print('handling block: ', block)

        if isinstance(block, str):
            block = jsonpickle.decode(block)

        if not isinstance(block, Block):
            raise ValueError('block should be an instance of Block')

        """
        Add a Block in the Blockchain if the Block signature is valid.
        """
        # @TODO:
        # What should I do if in this block it contains transactions that I'm currently mining? I should stop mining these transactions maybe? To see with Merkle Tree.
        if not Block.valid_block(block, self.last_block):
            return False

        self.chain.append(block)

        return True

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: A blockchain
        :return: True if valid, False if not
        """

        chain = jsonpickle.decode(chain)

        previous_block = chain[0]

        current_index = 1
        lenChain = len(chain)

        while current_index < lenChain:
            # Check with previous_block & current_block
            current_block = chain[current_index]

            if (not Block.valid_block(current_block, previous_block)):
                return False

            previous_block = current_block
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
        block = self.create_block(nonce, previous_hash)

        response = {
            'message': "New Block Forged",
            'index': block.index,
            'transactions': block.transactions,
            'nonce': block.nonce,
            'previous_hash': block.previous_hash,
        }

        return response
