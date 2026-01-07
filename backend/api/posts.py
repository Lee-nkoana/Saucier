from flask import request, jsonify
from backend.models.posts import create_new_post, get_post_by_id, get_post_by_author

def create_post():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "messsage": "No data provided"
            }), 400
        
        title = data.get("title")
        recipe =  data.get("recipe")
        author = data.get("author")

        if not title or not recipe or not author:
            return jsonify({
                "success": False,
                "message": "Fields can not be empty"
            }), 400
        
        newPost = create_new_post(title, author, recipe)

        if newPost is None:
            return jsonify({
                "success": False,
                "message": "Failed to create new post"
            }), 500
        
        return jsonify({
            "success": True,
            "message": "Account created successfully",
            "data": {
                "post_id": newPost.post_id,
                "post_title": newPost.title,
                "post_author": newPost.author,
                "recipe": newPost.recipe
            }
        }), 200
    
    except Exception as e:
        print(f"Registration error: {e}")
        return jsonify({ 
            "success": False,
            "message": "Failed to create post"
        }), 500

def get_user_posts(username):
    try:
        posts = get_post_by_author(username)

        return jsonify({
            "success": True,
            "data": [
                {
                    "post_id": post.post_id,
                    "title": post.title,
                    "recipe": post.recipe
                } for post in posts
            ]
        }), 200
    
    except Exception as e:
        print(f"Get posts error: {e}")
        return jsonify({
            "success": False,
            "message": "Failed to fetch posts"
        }), 500