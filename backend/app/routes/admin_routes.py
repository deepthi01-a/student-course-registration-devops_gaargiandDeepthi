# 📁 backend/app/routes/admin_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..controllers import admin_controller
from ..models import User

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/course', methods=['POST'])
@jwt_required()
def add_course():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    data = request.get_json()
    return jsonify(admin_controller.create_course(data))