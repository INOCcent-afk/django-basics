import requests


endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={
                             "title": "Abc123", "content": "Hello world", "price": "33"})  # HTTP Request

print(get_response.json())
