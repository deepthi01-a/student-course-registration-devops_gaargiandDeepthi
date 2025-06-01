# # # # 📁 backend/app/config.py
# # import os
# # class Config:
# #     SECRET_KEY = os.environ.get('SECRET_KEY')
# #     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
# #     SQLALCHEMY_TRACK_MODIFICATIONS = False
# #     JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
# # # class Config:
# # #     SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:zx0cv0bn0m@localhost:5432/student_course_db'
# # #     SQLALCHEMY_TRACK_MODIFICATIONS = False
# # #     SECRET_KEY = 'your_secret_key'
# # #     JWT_SECRET_KEY = 'your_jwt_secret'
# import os

# class Config:

#     SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-jwt-secret")
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-jwt-secret")