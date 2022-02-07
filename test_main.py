import main 

def test_validate_url():
	assert main.valid_url('url.com')==False
	assert main.valid_url('something.com')==False
	assert main.valid_url('http://www.google.com')==True

def test_check_url():
	assert main.check_url('http://www.googlee.com')==False
	assert main.check_url('http://www.google.com')==True