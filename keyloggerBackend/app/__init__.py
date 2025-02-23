from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.controller.insert_data_controller import sava_data_bp
    from app.controller.login_controller import login_bp
    from app.controller.computers_controller import computers_bp
    from app.controller.computers_controller import get_data_by_computer_bp

    app.register_blueprint(login_bp)
    app.register_blueprint(sava_data_bp)
    app.register_blueprint(computers_bp)
    app.register_blueprint(get_data_by_computer_bp)
    return app
