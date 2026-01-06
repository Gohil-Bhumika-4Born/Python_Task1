from flask import Blueprint
from ..controllers import auth_controller

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

auth_bp.add_url_rule(
    "/login", view_func=auth_controller.show_login, methods=["GET"], endpoint="login"
)
auth_bp.add_url_rule(
    "/login", view_func=auth_controller.login_action, methods=["POST"], endpoint="login_post"
)

auth_bp.add_url_rule(
    "/register", view_func=auth_controller.show_register, methods=["GET"], endpoint="register"
)
auth_bp.add_url_rule(
    "/register", view_func=auth_controller.register_action, methods=["POST"], endpoint="register_post"
)

auth_bp.add_url_rule(
    "/logout", view_func=auth_controller.logout_action, endpoint="logout"
)
