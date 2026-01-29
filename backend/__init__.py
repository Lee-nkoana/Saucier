from flask import Flask, render_template, request, jsonify, redirect, session, url_for
import requests
import os
from flask_cors import CORS

def create_app():
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/static"
    )

    app.secret_key = "dev-secret-key"
    app.config.update(
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=False,
        SESSION_COOKIE_PATH="/"
    )

    # Enable CORS
    CORS(app, supports_credentials=True)

    OLLAMA_URL = "http://localhost:11434/api/chat"
    MODEL = "mistral"

    # Import and register blueprints
    from backend.api import register_blueprints
    register_blueprints(app)

    @app.route("/")
    def home():
        return render_template("index.html")
    
    @app.route("/login")
    def login():
        return render_template("login.html")
    
    @app.route("/register")
    def register():
        return render_template("register.html")
    
    @app.route("/profile")
    def profile():
        return render_template("profile.html")
    
    @app.route("/explore")
    def explore():
        print("SESSION CONTENTS:", dict(session))
        if "user_id" not in session:
            return redirect(url_for("login"))
        return render_template("explore.html")
    
    @app.route("/chat", methods=["POST"])
    def chat():
        user_message = request.json.get("message")

        payload = {
            "model": MODEL,
            "messages": [
                {"role": "user", "content": user_message}
            ],
            "stream": False
        }

        try:
            response = requests.post(OLLAMA_URL, json=payload)
            response.raise_for_status()

            data = response.json()
            reply = data["message"]["content"]

            return jsonify({"reply": reply})

        except Exception as e:
            print("Ollama error:", e)
            return jsonify({"reply": "Error talking to Ollama"}), 500

        
    @app.route("/chat-ui")
    def chat_ui():
        return render_template("chat.html")

    return app
