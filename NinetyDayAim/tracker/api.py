import requests
import json

url = "https://api.aimlab.gg/graphql"

def usernameQuery(username):
    graphql_query = """query GetProfile($username: String) {
            aimlabProfile(username: $username) {
                username
                id
            }
        }"""
    
    variables = {"username": username, "user": {"id": ""}}

    data = {'query': graphql_query,
        "variables": variables}
    
    headers = {'content-type': 'application/json'}

    response = requests.post(url=url, headers=headers, data=json.dumps(data))


    if response.json()['data']['aimlabProfile'] == None: 
       return None
    else: 
       return response.json()['data']['aimlabProfile']





