from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)


    from app.controller.login_controller

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)

    return app