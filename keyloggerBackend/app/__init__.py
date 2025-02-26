from flask import Flask, request
from flask_cors import CORS
# from middleware.check_authorization import check_authorization
from keyloggerBackend.middleware.check_authorization import check_authorization

EXCLUDED_ROUTES_METHODS = {
    ("/login/", "POST")
}
def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.before_request
    def authorize_request():
        if request.method == "OPTIONS":
            return "", 200
        if (request.path, request.method) in EXCLUDED_ROUTES_METHODS:
            return
        check_authorization()

    from app.controller.insert_data_controller import sava_data_bp
    from app.controller.login_controller import login_bp
    from app.controller.computers_controller import computers_bp
    from app.controller.computers_controller import get_data_by_computer_bp
    from app.controller.profile_controller import get_profile_by_computer_bp



    app.register_blueprint(login_bp)
    app.register_blueprint(sava_data_bp)
    app.register_blueprint(computers_bp)
    app.register_blueprint(get_data_by_computer_bp)
    app.register_blueprint(get_profile_by_computer_bp)
    return app
