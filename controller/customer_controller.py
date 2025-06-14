from flask import Blueprint, request, jsonify
from service.customer_service import CustomerService
from repository.customer_repo import CustomerRepository
from extensions import db

customer_bp = Blueprint('customer_bp', __name__)

customer_repo = CustomerRepository(db.session)
service_customer = CustomerService(customer_repo)


@customer_bp.route('/customer/<int:customer_id>')
def get_customer(customer_id):
    customer = service_customer.get_customer(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    return jsonify({'id': customer.id, 'name': customer.name})

@customer_bp.route('/customers')
def get_all():
    customer = service_customer.get_all()
    return jsonify([
        {'id': c.id, 'name': c.name} for c in customer
    ])

@customer_bp.route('/customer', methods=['POST'])
def create_customer():
    data = request.json
    nome = data.get('name')
    

    customer = service_customer.create_customer(nome)
    return jsonify({'id': customer.id, 'name': customer.name}), 201