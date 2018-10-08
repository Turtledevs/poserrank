from poserrank.tests.fixtures import client, auth_client
from poserrank.tests.assert_tools import is_redirect, is_ok

def test_new_group(auth_client):
	new_group_response = auth_client.post('/groups/new', data=dict(name='testgroup',
																   description='test description'))
	assert is_redirect(new_group_response.status_code)
	group_response = auth_client.get('/groups/1')
	assert is_ok(group_response.status_code)
