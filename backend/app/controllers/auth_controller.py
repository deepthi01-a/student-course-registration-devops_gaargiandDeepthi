# 📁 backend/app/controllers/auth_controller.py
# from ..models import User
# from .. import db
# from ..utils.auth_utils import generate_token

# def register_user(data):
#     if User.query.filter_by(email=data['email']).first():
#         return {'error': 'User already exists'}

#     user = User(name=data['name'], email=data['email'], is_admin=data.get('is_admin', False))
#     user.set_password(data['password'])
#     db.session.add(user)
#     db.session.commit()
#     return {'message': 'User registered successfully'}

# def login_user(data):
#     user = User.query.filter_by(email=data['email']).first()
#     if user and user.check_password(data['password']):
#         token = generate_token(user)
#         return {'token': token, 'is_admin': user.is_admin}
#     return {'error': 'Invalid credentials'}

# # 📁 backend/app/controllers/auth_controller.py
# from .. import db
# from ..utils.auth_utils import generate_token

# def register_user(data):
#     try:
#         # Print debug data
#         print("📦 Received data:", data)

#         if not data or not data.get('name') or not data.get('email') or not data.get('password'):
#             return {'error': 'Missing required fields'}, 400

#         if User.query.filter_by(email=data['email']).first():
#             return {'error': 'User already exists'}, 409  # Conflict

#         user = User(name=data['name'], email=data['email'], is_admin=data.get('is_admin', False))
#         user.set_password(data['password'])

#         db.session.add(user)
#         db.session.commit()

#         return {'message': 'User registered successfully'}, 201

#     except Exception as e:
#         print("❌ Registration Error:", e)
#         return {'error': 'Server error', 'details': str(e)}, 500
    
# def login_user(data):
#     user = User.query.filter_by(email=data['email']).first()
#     if user and user.check_password(data['password']):
#         token = generate_token(user)
#         return {'token': token, 'is_admin': user.is_admin}
#     return {'error': 'Invalid credentials'}

# 📁 backend/app/controllers/auth_controller.py

from .. import db
from ..models import User               # ✅ Add this import
from ..utils.auth_utils import generate_token

def register_user(data):
    try:
        print("📦 Received data:", data)

        if not data or not data.get('name') or not data.get('email') or not data.get('password'):
            return {'error': 'Missing required fields'}, 400

        if User.query.filter_by(email=data['email']).first():
            return {'error': 'User already exists'}, 409

        user = User(
            name=data['name'],
            email=data['email'],
            is_admin=data.get('is_admin', False)
        )
        user.set_password(data['password'])

        db.session.add(user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201

    except Exception as e:
        print("❌ Registration Error:", e)
        return {'error': 'Server error', 'details': str(e)}, 500


def login_user(data):
    try:
        print("🔐 Login attempt:", data)

        if not data or not data.get('email') or not data.get('password'):
            return {'error': 'Missing credentials'}, 400

        user = User.query.filter_by(email=data['email']).first()

        if user and user.check_password(data['password']):
            token = generate_token(user)
            return {'token': token, 'is_admin': user.is_admin}, 200

        return {'error': 'Invalid credentials'}, 401

    except Exception as e:
        print("❌ Login Error:", e)
        return {'error': 'Server error', 'details': str(e)}, 500