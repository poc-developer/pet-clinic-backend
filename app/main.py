"""
This module serve as the entry point for the Flask application.
It sets up the Flask app, initializes logging, configure the database, and registers the routes.
"""
from flask import Flask
from app.routes import bp
from app.models import db
from app.model_config import Config
from app.logging_config import setup_logging


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
    app.register_blueprint(bp)

    return app

if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(port=8081, debug=True)
