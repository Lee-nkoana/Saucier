from flask import Flask
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

    return app
