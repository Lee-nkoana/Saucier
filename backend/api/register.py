from flask import request, jsonify
from backend.models.users import create_user, get_user_by_email

def register_user():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "messsage": "No data provided"
            }), 400
        
        username = data.get("username")
        email =  data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        existing_user = get_user_by_email(email)

        if not username or not email or not password or not confirm_password:
            return jsonify({
                "success": False,
                "message": "Fields can not be empty"
            }), 400
        
        if password != confirm_password:
            return jsonify({
                "success": False,
                "message": "Password and confirm password should match"
            }), 400
        
        if existing_user:
            return jsonify({
                "success": False,
                "message": "Email is already registered to a different account"
            }), 409
        
        newuser = create_user(username, email, password)
        if newuser is None:
            return jsonify({
                "success": False,
                "message": "Failed to create account"
            }), 500
        
        return jsonify({
            "success": True,
            "message": "Account created successfully",
            "data": {
                "user_id": newuser.id,
                "username": newuser.username,
                "email": newuser.email
            }
        }), 200
    
    except Exception as e:
        print(f"Registration error: {e}")
        return jsonify({ 
            "success": False,
            "message": "Registration failed"
        }), 500
