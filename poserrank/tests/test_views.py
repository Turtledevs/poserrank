from ..tests.fixtures import client

def test_index(client):
	rv = client.get('/')
	assert b'PoserRank' in rv.data