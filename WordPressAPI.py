from typing import Dict
import requests

"""
Classe WordPressAPI modélise un client référencé par son pseudo ainsi que son mot de passe dans la ressource WordPress de l'url donné.
Le client tente de se connecter et lance une requête get sur une ressource WordPress endpoint.
"""


class WordPressAPI:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.API = "https://etu2cas.wpcomstaging.com"
        self.token = None  # if None client not connected

    """
    Permet d'avoir les informations concernant le client connecté avec l'url indiquée dans 
    la requête POST en réutilisant le token stocké si la rêquete est valide.
    """

    def _get__user_informations(self):

        # Requête POST qui renvoi une reponse avec les information du client connecté.
        response = requests.post(
            self.API + "/wp-json/wp/v2/users/me", headers={'Authorization': 'Bearer {}'.format(self.token)}, verify=False)

        # Si la requête est valide, on sauvegarde les informations grâce aux ressources "first_name", "last_name" et "email", sinon on affiche l'erreur.
        if response.status_code == 200:
            rep_json = response.json()
            self.first_name = rep_json["first_name"]
            self.last_name = rep_json["last_name"]
            self.email = rep_json["email"]

        elif response.status_code == 404:
            print("Unable to reach URL.")
        else:
            print(
                f"There is a {response.status_code} error with your request {response.json()}")

    """
    Connecte l'utilisateur donné en argument avec username et password. Sauvegarde le token renvoyer par la requête qui est valide et appel la fonction privée
    _get__user_informations pour avoir la suite des informations qui nous interesse. Sinon on affiche l'erreur.
    """

    def connect(self):

        # Requête POST qui tente une connexion à l'API avec le pseudo et mot de passe du client que l'on veut authentifié pour récupérer son jeton sur la ressource token.
        response = requests.post(
            self.API + "/wp-json/jwt-auth/v1/token", data={'username': self.user, 'password': self.password})

        # Si la requête est valide on sauvegarde la ressource token et on appel la fonction privée _get_user_informations, sinon on affiche l'erreur.
        if response.status_code == 200:
            rep_json = response.json()
            self.token = rep_json["token"]
            self._get__user_informations()
        elif response.status_code == 404:
            print("Unable to reach URL.")
        else:
            print(
                f"There is a {response.status_code} error with your request {response.json()}")

    """
    Permet de lancer une reqûete GET sur l'url, venant de WordPress, endpoint donné en paramètre. 
    On réutilise le token sauvegardé pour que l'on ai une requête authentifiée.
    La fonction retourne la reponse de la requête sous format JSON si la requête est valide.
    Si le token a expiré (en ayant obtenu le code 403, ainsi que le message "Expired token"), 
    on relance une connexion du compte client pour avoir un token à jour valide et on rappel 
    la fonction get(endpoint) avec le meme endpoint. Sinon on affiche l'erreur et on renvoi none.
    """

    def get(self, endpoint):
        # Modification du header en utilisant le token récupéré dans la fonction connect() du client pour avoir une requête authentifiée.
        headers = {'Authorization': 'Bearer {}'.format(self.token)}

        # Requête GET sur la ressource endpoint, avec le header moidifié qui prend le token sauvegardé.
        response = requests.get(endpoint, headers=headers, verify=False)

        # Si la requête est valide on renvoi la reponse sous format JSON. Si le token expire on le remet à jour, sinon on affiche l'erreur et on renvoi none.
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403 and response.json()["message"] == "Expired token":
            self.connect()
            self.get(endpoint)
        elif response.status_code == 404:
            print("Unable to reach URL.")
            return None
        else:
            print(
                f"There is a {response.status_code} error with your request {response.json()}")
            return None

    """
    Permet de gérer l'affichage de l'objet en indiquant son prénom, nom et adresse email.
    """

    def __str__(self):
        if self.token:
            return f"Is connected as {self.first_name} {self.last_name}, {self.email}"
        return "Not connected yet"
