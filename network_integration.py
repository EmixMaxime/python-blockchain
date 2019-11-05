from blockchain_factory import blockchain_factory
from wallet import Wallet
from transaction import Transaction
from init_transactions import hashImg
import time

appleHash = hashImg('./items/apple.png')


bc, network = blockchain_factory()

time.sleep(5)

wallet = Wallet(testDatas=True)
wallet2 = Wallet(testDatas=True)

transaction = Transaction(wallet.address, wallet2.address, appleHash)
transaction2 = Transaction(wallet.address, wallet2.address, appleHash)
transaction3 = Transaction(wallet.address, wallet2.address, appleHash)

transaction.sign(wallet)
transaction2.sign(wallet)
transaction3.sign(wallet)

bc.submit_transaction(transaction)
bc.submit_transaction(transaction2)
bc.submit_transaction(transaction3)

print("Les transaction : ", bc.current_transactions)

time.sleep(15)

print("Les transaction : ", bc.current_transactions)