import json
import requests


class WordPressAPI:
    def __init__(self, user, password, API):
        self.user = user
        self.password = password
        self.API = API

    def connect(self):
        response = requests.request('POST', self.API)
        if response.status_code == 200:
            print("Succesful connection with API.")
            data = response.json()
        elif response.status_code == 404:
            print("Unable to reach URL.")
        else:
            print(f"There is a {response.status_code} error with your request")

    def get(self, endpoint):
        response = requests.get(endpoint)
        if response.status_code == 200:
            print("Succesful connection with API")
            print(response.json())
        elif response.status_code == 404:
            print("Unable to reach URL.")
        else:
            print(f"There is a {response.status_code} error with your request")
