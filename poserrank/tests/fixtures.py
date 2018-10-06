import os
import tempfile

import pytest
from .. import app_factory
from ..shared import db

@pytest.fixture
def client():
	app = app_factory(test=True)
	client = app.test_client()

	with app.app_context():
		db.create_all()

	yield client
