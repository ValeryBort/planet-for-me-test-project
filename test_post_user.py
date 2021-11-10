import requests

URL = 'https://reqres.in/api/users'
NAME = 'morpheus'
JOB = 'leader'

def test_post_user():
    post_user_response = requests.post(URL, data={'name': NAME, 'job': JOB})
    assert post_user_response.status_code == 201
    user_data = post_user_response.json()
    assert NAME == user_data['name']
    assert JOB == user_data['job']
