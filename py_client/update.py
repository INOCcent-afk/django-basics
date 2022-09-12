import requests


endpoint = "http://127.0.0.1:8000/api/products/4/update"

data = {
    "title": "updated"
}

get_response = requests.put(endpoint, json=data)  # HTTP Request

print(get_response.json())
