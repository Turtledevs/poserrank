from poserrank.tests.fixtures import client
from poserrank.tests.assert_tools import is_redirect

def test_index(client):
	rv = client.get('/')
	assert b'PoserRank' in rv.data


def test_login(client):
	new_user_response = client.post('/users/new', data=dict(username='testusername',
															full_name='Test User',
															email='testuser@mail.com',
															password='Testpass123'))
	assert is_redirect(new_user_response.status_code)
	login_response = client.post('/login', data=dict(username='testusername',
													 password='Testpass123'))
	assert is_redirect(login_response.status_code)