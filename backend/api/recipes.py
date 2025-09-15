from flask import Blueprint, jsonify

recipes_bp = Blueprint("recipes", __name__)

@recipes_bp.route("/", methods=["GET"])
def get_recipes():
    return jsonify({"message": "Here are some recipes!"})