from flask import Flask, render_template

class Transaction:
    def __init__(self, sender_public_key, sender_private_key, recipient_public_key, amount):
        self.sender_public_key = sender_public_key
        self.sender_private_key = sender_private_key
        self.recipient_public_key = recipient_public_key
        self.amount = amount

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')    
@app.route('/make/transaction')
def make_transactions():
    return render_template('./make_transaction.html') 
@app.route('/wallet/new')
def new_wallet():
    return ''

@app.route('/view/transactions')
def view_transactions():
    return render_template('./make_transaction.html') 

@app.route('/jacob')
def jacob():
    return 'Hello, Jacob!'


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='127.0.0.1', port=port, debug=True)
