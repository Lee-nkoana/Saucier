from flask import request, jsonify
from backend.models.users import get_user_by_username, get_user_by_email

def login_user():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "No data provided"
            }), 400
        
        

    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({ 
            "success": False,
            "message": "Login failed"
        }), 500

