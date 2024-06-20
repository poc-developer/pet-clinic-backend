"""
This module serve as the entry point for the Flask application.
It sets up the Flask app, initializes logging, configure the database, and registers the routes.
"""
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes.owners_routes import owners_bp
from app.routes.pets_routes import pets_bp
from app.models.model import db
from app.configs.model_config import Config
from app.configs.logging_config import setup_logging

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application instances.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Initialize logging
    setup_logging(app)

    # Register blueprints
    app.register_blueprint(owners_bp)
    app.register_blueprint(pets_bp)

    # Swagger
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'pet-clinic': 'Access API'
        }
    )
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(port=8081, debug=True)
