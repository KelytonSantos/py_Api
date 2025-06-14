from flask import Blueprint, request, jsonify
from service.order_service import OrderService
from repository.order_repo import OrderRepository
from extensions import db

order_bp = Blueprint('order_bp', __name__)

order_repo = OrderRepository(db.session)
service_order = OrderService(order_repo)


@order_bp.route('/order/<int:order_id>')
def get_customer(order_id):
    order = service_order.get_customer(order_id)
    if not order:
        return jsonify({'error': 'Customer not found'}), 404
    return jsonify({'id': order.id, 'name': order.name})

@order_bp.route('/orders')
def get_all():
    order = service_order.get_all()
    return jsonify([
        {'id': o.id, 'name': o.name} for o in order
    ])

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    customer_id = data.get('customer_id')
    items = data.get('items', [])

    if not customer_id or not items:
        return jsonify({'error': 'Dados incompletos'}), 400

    try:
        order = service_order.create_order(customer_id, items)
        return jsonify({
            'order_id': order.id,
            'total_amount': order.total_amount,
            'customer_id': order.customer_id,
            'items': [
                {'product_id': item.product_id, 'quantity': item.quantity}
                for item in order.order_lines
            ]
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
