import json
import requests
from requests.auth import HTTPBasicAuth


class WordPressAPI:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.API = "https://webeniz.wpcomstaging.com/2022/05/16/hello-world/"

    def connect(self):
        response = requests.request(
            'POST', self.API, auth=HTTPBasicAuth(self.user, self.password))
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
            return response.json()
        elif response.status_code == 404:
            print("Unable to reach URL.")
            return None
        else:
            print(f"There is a {response.status_code} error with your request")
            return None
