# app.py
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Example automation: fetch current BTC price from API
    resp = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    price = resp['bpi']['USD']['rate']
    return render_template('index.html', price=price)

if __name__ == '__main__':
    app.run(debug=True)
