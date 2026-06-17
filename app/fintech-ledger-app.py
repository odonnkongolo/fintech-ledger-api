from flask import Flask, jsonify, render_template

# 1. Initialize the app
app = Flask(__name__)


# 2. Define the web URL paths
@app.route('/', methods=['GET'])
def home():
    return render_template(
        'index.html',
        service='Ledger Synchronization Dashboard API',
        status='142000 Transactions'
    )


@app.route('/transaction-status', methods=['GET'])
def get_status():
    return jsonify({
        'ledger-status': 'Synchronized to AWS Managed Database',
        'processed-transactions': '142000'
    })


# 3. Run the development server
if __name__ == '__main__':
    app.run(debug=False)
