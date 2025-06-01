# 📁 backend/app/routes/student_routes.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..controllers import student_controller

student_bp = Blueprint('student', __name__)

@student_bp.route('/courses', methods=['GET'])
@jwt_required()
def list_courses():
    return jsonify(student_controller.list_all_courses())

@student_bp.route('/register', methods=['POST'])
@jwt_required()
def register_course():
    student_id = get_jwt_identity()
    data = request.get_json()
    return jsonify(student_controller.register_student_to_course(student_id, data['course_id']))
