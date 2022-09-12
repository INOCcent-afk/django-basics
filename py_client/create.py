import requests


endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "title",
}

get_response = requests.post(endpoint, json=data)  # HTTP Request

print(get_response.json())
