# 📁 backend/app/controllers/student_controller.py
from ..models import Course, Registration
from .. import db

def list_all_courses():
    courses = Course.query.all()
    return [{'id': c.id, 'title': c.title, 'description': c.description} for c in courses]

def register_student_to_course(student_id, course_id):
    existing = Registration.query.filter_by(student_id=student_id, course_id=course_id).first()
    if existing:
        return {'error': 'Already registered'}
    reg = Registration(student_id=student_id, course_id=course_id)
    db.session.add(reg)
    db.session.commit()
    return {'message': 'Registration successful'}