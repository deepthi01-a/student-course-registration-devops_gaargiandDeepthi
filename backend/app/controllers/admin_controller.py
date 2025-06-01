# 📁 backend/app/controllers/admin_controller.py
from ..models import Course
from .. import db

def create_course(data):
    course = Course(title=data['title'], description=data['description'])
    db.session.add(course)
    db.session.commit()
    return {'message': 'Course created successfully'}
