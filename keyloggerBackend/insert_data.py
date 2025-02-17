from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
# from keyloggerAgent.manager_keyLogger import manager

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def save_decrypted_data():
    data=request.get_json()
    # decrypted_info = manager.decrypt
    # print("svgcxc",decrypted_info)
    print(data)
    # return jsonify({"decrypted_data": decrypted_info})
    return jsonify({"data": data})
    # return "cccb"
if __name__ == '__main__':
    app.run(debug=True)
