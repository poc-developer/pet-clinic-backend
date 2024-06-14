"""This module is for unit testing purpose."""

def test_get_owners_success(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/v1/owners' endpoint is required (GET)
    THEN check that the response is valid and contains owner data 
    """
    response = test_client.get('/v1/owners')
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert len(data['data']) > 0

def test_get_owners_with_last_name(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/v1/owners' endpoint is required (GET) with the lastName query parameter
    THEN check that the response is valid and contains the filtered owner data
    """
    response = test_client.get('/v1/owners', query_string= {'lastName': 'De'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert len(data['data']) > 0

def test_create_owner_success(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/v1/owners/new' endpoint is required (POST) with valid data
    THEN check that a new owner is created successfully and a location header is presented
    """
    response = test_client.post('/v1/owners/new', json={
        'firstName': 'Jane',
        'lastName': 'Doe',
        'address': '345 Main St',
        'city': 'Anywhere',
        'telephone': '4444445555'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert 'data' in data
    assert data['data']['name'] == 'Jane Doe'
    assert 'Location' in response.headers

def test_create_owner_duplicate_telephone(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/v1/owners/new' endpoint is required (POST) with a duplicate telephone number
    THEN check that the response indicates a bad request with a suitable error message
    """
    response = test_client.post('/v1/owners/new', json={
        'firstName': 'Anne',
        'lastName': 'Doe',
        'address': '345 Main St',
        'city': 'Anywhere',
        'telephone': '3333333333'
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == 400
    assert data['error']['message'] == 'Telephone number has already exists!'

def test_create_owner_invalid_data(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/v1/owners/new' endpoint is required (POST) with valid data
    THEN check that a new owner is created successfully and a location header is presented
    """
    response = test_client.post('/v1/owners/new', json={'first_name': 'Jane'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == 400
    assert data['error']['message'] == "Invalid request data"
