from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome Giovanni Andres'

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/products/<string:product_name>')
def get_product_by_name(product_name):
    productFounded = [product for product in products if product['name'] == product_name]
    if len(productFounded) > 0:
        return jsonify(productFounded[0])
    else:
        return jsonify({"message" : "Product not found"})
    
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products})

@app.route('/products', methods=['POST'])
def create_product():
    product = {
        "name" : request.json['name'],
        "price" : request.json['price'],
        "quantity" : request.json['quantity']
    }
    products.append(product)
    return 'Recibido'

if __name__ == '__main__':
    app.run(debug=True, port=4000)
