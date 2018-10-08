def is_redirect(response_code):
	return 300 <= response_code < 400

def is_ok(response_code):
	return 200 <= response_code < 300