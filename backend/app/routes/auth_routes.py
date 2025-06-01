
# # 📁 backend/app/routes/auth_routes.py
# from flask import Blueprint, request, jsonify
# from app.controllers import auth_controller

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     print("Income json: ", data)
#     return jsonify(auth_controller.register_user(data))

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     return jsonify(auth_controller.login_user(data))
# 📁 backend/app/routes/auth_routes.py

from flask import Blueprint, request, jsonify
from app.controllers import auth_controller

# ✅ Correct Blueprint declaration
auth_bp = Blueprint('auth', __name__)


# 🔐 REGISTER Route
@auth_bp.route('/register', methods=['POST'])
def register():
    print("📥 Register route hit")
    print("📦 Raw request data:", request.data)

    data = request.get_json(silent=True)
    print("🔍 Incoming JSON:", data)

    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    response = auth_controller.register_user(data)

    if isinstance(response, tuple):
        return jsonify(response[0]), response[1]
    return jsonify(response), 200


# 🔐 LOGIN Route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    print("🔐 Login JSON:", data)

    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    response = auth_controller.login_user(data)

    if isinstance(response, tuple):
        return jsonify(response[0]), response[1]
    return jsonify(response), 200