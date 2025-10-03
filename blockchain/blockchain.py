from flask import Flask
from flask import render_template
from time import time
class Blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []
        self.create_block(0, '0000')
    def create_block(self, nonce, previous_hash):
        block = {
            'blocknumber': len(self.chain) + 1,
            'timestamp': time(),
            'nonce': nonce,
            'previous_hash': previous_hash,
            'transactions': self.transactions
        }
        self.transactions = []
        self.chain.append(block)
        return block
    
blockchain = Blockchain()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')    

@app.route('/jacob')
def jacob():
    return 'Hello, Jacob!'


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='127.0.0.1', port=port, debug=True)

