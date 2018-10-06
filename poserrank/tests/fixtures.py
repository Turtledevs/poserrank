import os
import tempfile

import pytest
from .. import app_factory
from ..shared import db

@pytest.fixture
def client():
	app = app_factory(test=True)
	db_fd, app.config['DATABASE'] = tempfile.mkstemp()
	app.config['TESTING'] = True
	app.config['SECRET_KEY'] = 'testkey'
	client = app.test_client()

	with app.app_context():
		db.create_all()

	yield client

	os.close(db_fd)
	os.unlink(app.config['DATABASE'])