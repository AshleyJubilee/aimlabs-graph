import requests
import json
from pprint import pprint


username = 'ashjubilee'
url = "https://api.aimlab.gg/graphql"


graphql_query = """query GetProfile($username: String) {
        aimlabProfile(username: $username) {
            username
            id
        }
    }"""

variables = {
  "username": username,
  "user": {
                "id": ""
            }
}

data = {'query': graphql_query,
        "variables": variables}

headers = {
  'content-type': 'application/json'
}

response = requests.post(url=url, headers=headers, data=json.dumps(data))




pprint(response.json())
