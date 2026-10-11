"""Автентифікація (FR-04): вхід за email і паролем."""
from flask import Blueprint, current_app, jsonify, request
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint("auth", __name__, url_prefix="/api/auth")

USERS = {"student@modaline.ua": generate_password_hash("Passw0rd!")}


@bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    email = data.get("email", "")
    password = data["password"]
    pw_hash = USERS.get(email)
    if not pw_hash or not check_password_hash(pw_hash, password):
        return jsonify(error="Невірний email або пароль"), 401
    token = URLSafeTimedSerializer(current_app.config["SECRET_KEY"]).dumps({"email": email})
    return jsonify(access_token=token, token_type="bearer")
