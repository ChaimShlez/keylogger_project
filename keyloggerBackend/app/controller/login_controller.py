from flask import Blueprint, jsonify, request
from app.logic import login_logic as login

# login_bp = Blueprint('login', __name__, url_prefix='/login/')
login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/', methods=['POST'])
def login_user():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    token = login.check_login(username, password)
    if token:
        return jsonify({"token": token}), 200
    else:
        return jsonify({"status": "fail", "error": "Invalid credentials"}), 401
