# controller/user_controller.py

from flask import Blueprint, request, jsonify
from service.product_service import ProductService
from repository.product_repo import ProductRepository
from extensions import db

product_bp = Blueprint('product_bp', __name__)

product_repo = ProductRepository(db.session)
service_product = ProductService(product_repo)


@product_bp.route('/product/<int:user_id>')
def get_product(product_id):
    product = service_product.get_product(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'id': product.id, 'nome': product.name, 'preco': product.price})

@product_bp.route('/products')
def get_all():
    products = service_product.get_all()
    return jsonify([
        {'id': p.id, 'nome': p.name, 'preco': float(p.price)} for p in products
    ])


@product_bp.route('/product', methods=['POST'])
def create_product():
    data = request.json
    nome = data.get('nome')
    price = data.get('preco')
    
    product = service_product.create_user(nome, price)
    return jsonify({'id': product.id, 'nome': product.name, 'preco': product.price}), 201