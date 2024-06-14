"""
This module contains the configuration settings for the Flask application. 
It defines a Config class which holds the configuration variables for the application, 
particularly for SQLAlchemy.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration class with settings for SQLAlchemy.

    Attributes:
        SQLALCHEMY_DATABASE_URI: The database URI for SQLAlchemy.
        SQLALCHEMY_TRACK_MODIFICATIONS: 
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///"memory:'
    TESTING = True