from flask import Flask, render_template
from flask_cors import CORS

def create_app():
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/static"
    )

    # Enable CORS
    CORS(app)

    # Import and register blueprints
    from backend.api import register_blueprints
    register_blueprints(app)

    @app.route("/")
    def home():
        return render_template("index.html")
    
    @app.route("/login")
    def login():
        return render_template("login.html")

    return app



