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
        
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({
                "success": False,
                "message": "Username and/ or password can not be empty."
            }), 400
        
        user = get_user_by_username(username)

        if user is None:
            return jsonify({
                "success": False,
                "message": "User does not exist"
            }), 406
        
        if user.password != password:
            return jsonify({
                "success": False,
                "message": "Incorrect password"
            }), 400
        
        return jsonify({
            "success": True,
            "message": "Login successful",
            "data": {
                "user_id": user.id,
                "username": user.username,
                "email": user.email
            }
        }), 200

    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({ 
            "success": False,
            "message": "Login failed"
        }), 500

