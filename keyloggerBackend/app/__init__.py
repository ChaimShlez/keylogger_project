from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)


    from app.controller.login_controller import login_bp
    from app.controller.insert_data import sava_data_bp
    app.register_blueprint(login_bp)
    app.register_blueprint(sava_data_bp)

    return app