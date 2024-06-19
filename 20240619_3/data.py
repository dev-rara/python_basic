import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
response_data = response.json()["results"]

question_data = []

for data in response_data:
    question_data.append(data)
