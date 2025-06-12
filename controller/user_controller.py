# controller/user_controller.py

from flask import Blueprint, request, jsonify
from service.user_service import UserService 
from repository.user_repo import UserRepository
from extensions import db

user_bp = Blueprint('user_bp', __name__)

user_repo = UserRepository(db.session)
service_user = UserService(user_repo)


@user_bp.route('/users/<int:user_id>')
def get_user(user_id):
    user = service_user.get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'id': user.id, 'nome': user.nome, 'email': user.email})

@user_bp.route('/users', methods=['POST'])
def create_users():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    
    user = service_user.create_user(nome, email)
    return jsonify({'id': user.id, 'nome': user.nome, 'email': user.email}), 201