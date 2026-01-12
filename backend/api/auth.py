from flask import Blueprint
from backend.models.users import create_user, get_user_by_email
from backend.api.register import register_user  
from backend.api.login import login_user
from backend.api.posts import *

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    return register_user()

@auth_bp.route("/login", methods=["POST"])
def login():
    return login_user()

@auth_bp.route("/posts", methods=["POST"])
def post():
    return create_post()

@auth_bp.route("/posts/<username>", methods=["GET"])
def user_posts(username):
    return get_user_posts(username)

@auth_bp.route("/posts/all", methods=["GET"])
def all_posts():
    return get_all_existing_posts()