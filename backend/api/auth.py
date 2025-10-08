from flask import Blueprint
from backend.models.users import create_user, get_user_by_email
from backend.api.register import register_user  
from backend.api.login import login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    return register_user()

@auth_bp.route("/login", methods=["POST"])
def login():
    return login_user()