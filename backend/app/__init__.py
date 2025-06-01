# # 📁 backend/app/__init__.py
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS
# from flask_jwt_extended import JWTManager
# from .config import Config

# # Initialize extensions
# db = SQLAlchemy()
# migrate = Migrate()
# jwt = JWTManager()

# def create_app():
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_object(Config)
#     app.config.from_pyfile('config.py', silent=True)

#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
#     CORS(app)

#     from .routes.auth_routes import auth_bp
#     from .routes.student_routes import student_bp
#     from .routes.admin_routes import admin_bp

#     app.register_blueprint(auth_bp, url_prefix='/api/auth')
#     app.register_blueprint(student_bp, url_prefix='/api/student')
#     app.register_blueprint(admin_bp, url_prefix='/api/admin')

#     return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object("app.config.Config")
    print("loaded DB URI: ", app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.student_routes import student_bp
    from app.routes.admin_routes import admin_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(student_bp, url_prefix="/student")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app
