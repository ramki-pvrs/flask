"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from ddtrace import patch_all

db = SQLAlchemy()
login_manager = LoginManager()
thisSession = Session()
patch_all()

def create_app():
    """Create Flask Application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')
    
    # Blueprints assets related
    assets = Environment()  # Create an assets environment
    assets.init_app(app)  # Initialize Flask-Assets

    # Initialize Plugins
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    thisSession.init_app(app)

    with app.app_context():
        # any python files or logic in your app which are not Blueprints 
        from .assets import compile_static_assets

        # Import blueprint parts of our application
        from .blueprints.home import home
        from .blueprints.auth import auth
        from .blueprints.userprofile import userprofile
        #from .blueprints.todo import todo


        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(userprofile.userprofile_bp)
        #app.register_blueprint(todo.todo_bp)

        # Create static asset bundles
        compile_static_assets(assets)

        # Create Database Models
        db.create_all() # Create sql tables for our data models

        return app
