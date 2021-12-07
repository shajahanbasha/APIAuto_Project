import requests
import json
import jsonpath
url = "https://reqres.in/api/users/2"

def test_modify_user():

    # Read Input file
    file = open("D:\\API automaton\\UpdatedUser.json", 'r')

    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    # make post request with json input body
    response = requests.put(url)
    res_code = response.status_code
    print(res_code)

    assert res_code == 200

    res_header = response.headers.get('Content-Length')
    print(res_header)

    #Parse response Content
    response_json = json.loads(response.text)
    update_li = jsonpath.jsonpath(response_json, 'updatedAt')
    print(update_li)