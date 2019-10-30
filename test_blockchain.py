from blockchain import Blockchain
from wallet import Wallet
from client import Client

blockchain = Blockchain()

wallet = Wallet()
guy_wallet = Wallet(1024, True)


def test_submit_transaction():
    transaction, signature = Client.generate_transaction(
        wallet, guy_wallet.address, 10)

    # don't forget genesis block
    assert len(blockchain.current_transactions) == 0
    blockchain.submit_transaction(transaction, signature)
    assert len(blockchain.chain) == 1


def test_mine():
    for i in range(10):
        transaction, signature = Client.generate_transaction(
            wallet, guy_wallet.address, 10)
        blockchain.submit_transaction(transaction, signature)

    print(blockchain.mine())
