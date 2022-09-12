import requests

endpoint = "http://127.0.0.1:8000/api/products/4/delete"

get_response = requests.delete(endpoint)  # HTTP Request

print(get_response.json())
