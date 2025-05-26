import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=payload)

print("POST Status Code:", response.status_code)
print("POST Response Body:", response.json())
print(response.json()["title"])

updated_data = {
    "id": 1,
    "title": "updated title",
    "body": "updated body",
    "userId": 1
}

response = requests.put(url, json=updated_data)

print("PUT Status Code:", response.status_code)
print("PUT Response Body:", response.json())


# Make the GET request
response = requests.get(url)

# Extract and print response code and body
print("Status Code:", response.status_code)
print("Response Body:", response.json())  # Use response.text if not JSON

response = requests.delete(url)

print("DELETE Status Code:", response.status_code)
print("DELETE Response Body:", response.text)  # Usually empty

