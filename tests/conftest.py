"""This is a fixture models"""
import pytest
from run import create_app
from app.models.model import db, Owner
from app.configs.model_config import TestingConfig

@pytest.fixture(scope='module')
def test_client():
    """
    Sets up a Flask test client for the application configured for testing.

    - Configures the app for testying purpose and uses in-memory SQLite database.
    - Creates all database tables before the tests run.
    - Yields the test client for use in tests.
    - Remove the session after the tests are done.

    Returns:
        FlaskClient: Configured test client for the application.
    """
    flask_app = create_app()

    flask_app.config.from_object(TestingConfig)
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client
            db.session.remove()

@pytest.fixture(scope='module')
def new_owner():
    owner = Owner(name='John De', address='123 Main St', city='Somewhere', telephone='126543651423')
    return owner
