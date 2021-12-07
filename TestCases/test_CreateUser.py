import requests
import json
import jsonpath
url = "https://reqres.in/api/users"


def test_create_user():
    # Read Input file
    file = open("D:\\API automaton\\CreateUser.json", 'r')

    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    # make post request with json input body
    response = requests.post(url)
    res_code = response.status_code
    print(res_code)
    assert res_code == 201
    res_header = response.headers.get('Content-Length')
    print(res_header)

    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])