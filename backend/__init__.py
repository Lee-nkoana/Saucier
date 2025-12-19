from flask import Flask, render_template, request, jsonify
import requests
import os
from flask_cors import CORS

def create_app():
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/static"
    )

    # Enable CORS
    CORS(app)

    HF_API_URL = "https://router.huggingface.co/models/google/flan-t5-base"
    HF_TOKEN = os.getenv("HF_baseToken")

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

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
    
    @app.route("/explore")
    def explore():
        return render_template("explore.html")
    
    @app.route("/chat", methods=["POST"])
    def chat():
        payload = request.get_json(silent=True)
        if not payload or "message" not in payload:
            return jsonify({"reply": "No message provided"}), 400

        user_message = payload["message"]

        response = requests.post(
            HF_API_URL,
            headers=headers,
            json={"inputs": user_message},
            timeout=30
        )

        # 🔎 Debug info
        print("HF status:", response.status_code)
        print("HF raw text:", response.text[:300])

        # ❌ Non-200 response
        if response.status_code != 200:
            return jsonify({
                "reply": f"HF error {response.status_code}"
            }), 500

        # ❌ Empty response body
        if not response.text.strip():
            return jsonify({
                "reply": "HF returned an empty response"
            }), 500

        # ❌ Not valid JSON
        try:
            hf_data = response.json()
        except Exception as e:
            return jsonify({
                "reply": "HF returned invalid JSON"
            }), 500

        # ❌ HF-level error
        if isinstance(hf_data, dict) and "error" in hf_data:
            return jsonify({
                "reply": hf_data["error"]
            }), 500

        # ✅ Normal response
        if isinstance(hf_data, list) and len(hf_data) > 0:
            ai_reply = hf_data[0].get("generated_text", "No response generated")
        else:
            ai_reply = "Unexpected HF response format"

        return jsonify({"reply": ai_reply})
    
    @app.route("/chat-ui")
    def chat_ui():
        return render_template("chat.html")

    return app



