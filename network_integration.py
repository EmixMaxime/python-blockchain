from blockchain_factory import blockchain_factory
from wallet import Wallet
from transaction import Transaction


bc, network = blockchain_factory()

wallet = Wallet()
wallet2 = Wallet(1024, True)
transaction = Transaction(wallet.address, wallet2.address, "bonjour")

transaction.sign(wallet)

bc.submit_transaction(transaction)