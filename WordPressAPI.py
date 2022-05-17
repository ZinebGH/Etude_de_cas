import requests


class WordPressAPI:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.API = "https://etu2cas.wpcomstaging.com"
        self.token = None

    def connect(self):
        response = requests.post(
            self.API + "/wp-json/jwt-auth/v1/token", data={'username': self.user, 'password': self.password})
        if response.status_code == 200:
            print("Succesful connection with API.")
            self.token = response.json()["token"]
            print(self.token)
        elif response.status_code == 404:
            print("Unable to reach URL.")
        else:
            print(
                f"There is a {response.status_code} error with your request {response.json()}")

    def get(self, endpoint):
        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        print(self.token)
        response = requests.get(endpoint, headers=headers, verify=False)

        if response.status_code == 200:
            print("Succesful connection with API")
            return response.json()
        elif response.status_code == 403:
            self.connect()
            self.get(endpoint)
        elif response.status_code == 404:
            print("Unable to reach URL.")
            return None
        else:
            print(
                f"There is a {response.status_code} error with your request {response.json()}")
            return None
