import time
from flask import Flask, render_template
from network_integration import run

app = Flask(__name__)

"""
- List transactions that are currently not in a block.
- List blocks

"""


@app.route('/')
def accueil():
    my_blockchain, network = run()

    chain = my_blockchain.chain
    current_transactions = my_blockchain.current_transactions
    return render_template('index.html', chain=chain, current_transactions=current_transactions)


if __name__ == '__main__':
    app.run(port=3333, debug=True)
