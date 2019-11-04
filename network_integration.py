from blockchain_factory import blockchain_factory
from wallet import Wallet
from transaction import Transaction


bc, network = blockchain_factory()

wallet = Wallet()
wallet2 = Wallet(1024, True)
transaction = Transaction(wallet.addresse, wallet2.addresse, "bonjour")

transaction.sign(wallet)

bc.submit_transaction(transaction)