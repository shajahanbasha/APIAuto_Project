import requests

url = "https://reqres.in/api/users/2"

def test_delete_user():

    response = requests.delete(url)
    res_code = response.status_code
    print(res_code)

    assert res_code == 204
