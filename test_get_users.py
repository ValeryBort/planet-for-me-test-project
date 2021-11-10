import requests


URL = 'https://reqres.in/api/users?page=2'
test_set = {'id', 'email', 'first_name', 'last_name', 'avatar'}


def test_get_users():
    get_users = requests.get(URL)
    assert get_users.status_code == 200
    fields = get_users.json()['data']
    for element in fields:
        keys = set(element.keys())
        assert test_set.issubset(keys)
