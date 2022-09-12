import requests


auth_endpoint = "http://127.0.0.1:8000/api/auth/"

auth_response = requests.post(
    auth_endpoint, json={"username": "admin", "password": "admin"})
print(auth_response.json())

endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.get(endpoint)  # HTTP Request

print(get_response.json())
