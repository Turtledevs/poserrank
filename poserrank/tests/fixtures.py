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


@pytest.fixture
def auth_client(client):
	"""a logged-in client"""
	new_user_response = client.post('/users/new', data=dict(username='testusername',
															full_name='Test User',
															email='testuser@mail.com',
															password='Testpass123'))
	login_response = client.post('/login', data=dict(username='testusername',
													 password='Testpass123'))

	yield client
