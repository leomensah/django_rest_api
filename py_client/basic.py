import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, json={"query": "Hellow World"})
print(get_response.json())
print(get_response.status_code)