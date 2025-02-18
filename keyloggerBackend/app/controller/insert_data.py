from flask import Flask, jsonify, request
from flask_cors import CORS
# from keyloggerAgent.manager_keyLogger import manager
from keyloggerBackend.logic.save_data import WriteToNetwork
from keyloggerBackend.logic import login as login_logic

app = Flask(__name__)
CORS(app)


# @app.route('/', methods=['POST'])
# def save_decrypted_data():
#     data=request.get_json()
#     host_name = request.headers.get("host_name")
#     write_to_network=WriteToNetwork(host_name)
#     write_to_network.write(data)
#
#     print(data)
#     if not data:
#         return jsonify({"error": "No data received"}), 400
#     return jsonify({"status": "success"}), 200


@app.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    login_status = login_logic.check_login(username, password)

    if login_status:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "fail", "error": "Invalid credentials"}), 401


@app.route('/', methods=['Get'])
def f():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
