from flask import Flask, render_template, jsonify

app = Flask(__name__)

Products = [
    {'type': 'metal', 'name':'Necklace', 'Price': 'Rs 1200'},
    {'type':'steel', 'name':'Earring', 'Price':'Rs 800'},
    {'type':'steel', 'name':'Earring', 'Price':'Rs 800'}
]

@app.route('/')
def hello_world():
    return render_template('home.html', products=Products)

@app.route('/products')
def list_products():
    return jsonify(Products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)