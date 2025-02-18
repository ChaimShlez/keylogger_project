from flask import Blueprint, jsonify, request
from app.logic import login

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    login_status = login.check_login(username, password)
    if login_status:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "fail", "error": "Invalid credentials"}), 401
