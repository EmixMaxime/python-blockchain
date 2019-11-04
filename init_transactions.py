from transaction import Transaction
import hashlib

def getInitialTransactions():
    txs = []
    appleHash = hashImg('./items/apple.png')
    ironAxeHash = hashImg('./items/iron_axe.png')
    ironSwordHash = hashImg('./items/iron_sword.png')

    for i in range(4):
        tx = Transaction('@sender_address', '@recipient_address', appleHash)
        #tx.sign(wallet)
        txs.append(tx)

        tx = Transaction('@sender_address', '@recipient_address', ironAxeHash)
        #tx.sign(wallet)
        txs.append(tx)

        tx = Transaction('@sender_address', '@recipient_address', ironSwordHash)
        #tx.sign(wallet)
        txs.append(tx)

    return txs
 
def hashImg(img_path):
    img_content = _getImgData(img_path)
    return hashlib.sha256(img_content.encode()).hexdigest()  

def _getImgData(img_path):
    tmp = open(img_path, 'rb').read().hex()
    return tmp
