import jwt
import os
from flask import request, jsonify

def check_authorization():

    try:
        authorization_header = request.headers.get("Authorization")
        if not authorization_header or not authorization_header.startswith("Bearer "):
            return jsonify({"error": "Unauthorized"}), 401

        token = authorization_header[len("Bearer "):]
        verify_token(token)
    except Exception as e:
        return jsonify({"error": str(e)}), 401

def verify_token(token):

    try:
        secret_key = os.getenv("TOKEN_SECRET_KEY")
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])

        if not decoded_token or "tokenData" not in decoded_token:
            raise jwt.InvalidTokenError("INVALID_TOKEN")

        request.user_name = decoded_token["tokenData"]["userName"]
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise jwt.InvalidTokenError("TOKEN_EXPIRED")
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError("INVALID_TOKEN")
