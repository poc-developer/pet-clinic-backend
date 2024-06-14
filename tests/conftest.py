
import pytest
from app.main import create_app
from app.models import db, Owner
from app.model_config import TestingConfig

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    flask_app.config.from_object(TestingConfig)
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client
            db.session.remove()

@pytest.fixture(scope='module')
def new_owner():
    owner = Owner(name='John De', address='123 Main St', city='Somewhere', telephone='1111112111')
    return owner
