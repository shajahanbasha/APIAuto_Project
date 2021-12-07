import json

import requests
import json
import jsonpath

def test_fetch_user():

    # API Url
    url="https://reqres.in/api/users?page=2"

    # Send Get request
    response = requests.get(url)
    print(response)
    res_code = response.status_code

    # getting response code
    print(res_code)
    assert res_code == 200

    # Display Response content
    print(response.content)

    # Fetch header of the response
    print(response.headers)

    # loading the data in json format
    json_response = json.loads(response.text)
    print(json_response)

    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(pages[0])
    assert pages[0] == 2