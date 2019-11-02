from blockchain import Blockchain
from wallet import Wallet
from client import Client

blockchain = Blockchain()

wallet = Wallet()
guy_wallet = Wallet(1024, True)


def test_submit_transaction():
    transaction = Client.generate_transaction(
        wallet, guy_wallet.address, 10)

    # don't forget genesis block
    assert len(blockchain.current_transactions) == 0
    blockchain.submit_transaction(transaction)
    assert len(blockchain.chain) == 1


def test_mine():
    for i in range(10):
        transaction = Client.generate_transaction(
            wallet, guy_wallet.address, 10)
        blockchain.submit_transaction(transaction)

    print(blockchain.mine())


def test_chain_for_network():
    for i in range(3):
        transaction = Client.generate_transaction(
            wallet, guy_wallet.address, 10)
        blockchain.submit_transaction(transaction)

    blockchain.mine()

    s = blockchain.chain_for_network
    assert isinstance(s, str) == True


def test_valid_chain():
    s = blockchain.chain_for_network
    valid = blockchain.valid_chain(s)

    assert valid == True
