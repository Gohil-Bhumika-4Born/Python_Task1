from flask import Flask
from .extensions import db, migrate, login_manager
from .config import Config
from .routes.auth_routes import auth_bp
from .models.user import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # redirect unauthorized users
    login_manager.login_view = "auth.login"

    # required user loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # register blueprints
    app.register_blueprint(auth_bp)

    return app
