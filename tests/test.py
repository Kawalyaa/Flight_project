import json
import pytest
from app import app
from app.routes_or_views import create_aflight
# from app.routes_or_views import all_flights

# Fixture for test client:


@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass
# databases and resourses have to be freed at the end. But so far we don't have anything
    request.addfinalizer(teardown)
    return test_client


def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='/application/json')


def json_of_respons(response):
        """Decode json from response"""
        return json.loads(response.data.decode('utf8'))

# The simplest test for GET endpoint:


def test_all_flights(client):
    response = client.get('/all_flights')
    assert b'my_flight' in response.data


def test_get_oneFlight(client):
    """Testing the get one endpoint"""
    response = client.get('/get_oneFlight/<int:id>')
    assert json_of_respons(response) == {'error': 'Not found'}


def test_create_create_aflight(client):
    response = post_json(client, '/create_aflight', {'key': 'value'})
    assert json_of_respons(response) == [{'error': 'Bad request'}, 400]


def test_update_flight(client):
    response = post_json(client, '/update_flight/<int:ask_flightId>', {'key': 'value'})
    assert json_of_respons(response) == {'error': 'Not found'}


def test_delete_flight(client):
    response = post_json(client, '/remove_aflight/<int:flightId>', {'key': 'value'})
    assert json_of_respons(response) == {'error': 'Not found'}
