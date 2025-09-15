# Import blueprints from the other API files
from .recipes import recipes_bp
# from .auth import auth_bp

# Function to register all blueprints with the app
def register_blueprints(app):
    app.register_blueprint(recipes_bp, url_prefix="/api/recipes")
    # app.register_blueprint(auth_bp, url_prefix="/api/auth")
    # app.register_blueprint(mealprep_bp, url_prefix="/api/mealprep")