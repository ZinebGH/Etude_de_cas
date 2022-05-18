from WordPressAPI import *

"""
La fonction authentifie un utilisateur grâce à son pseudo (username) et son mot de passe (ppassword), de type string, donnés en paramètres
Elle renvoie True si la connexion c'est établie, sinon False.
"""


def authenticate(username, password):

    # On vérifie si les string donnés ne sont pas vide ou null, on renvoi False car l'authentification n'a pas aboutie.
    if (username or password) == ("" or " "):
        return False

    # Initialisation du client de type WordPressAPI avec en argument le pseudo et le mot de passe récupérer dans les paramètres de la fonction authenticate
    client = WordPressAPI(username, password)
    # On test la connexion du client
    client.connect()

    response = client.get(
        "https://etu2cas.wpcomstaging.com/wp-json/wp/v2/users/me")

    # On vérifie la valeur obtenue lors de l'appel de la fonction get par le client, si le client n'est pas connecté, elle vaut none et on renvoi False.
    if not response:
        return False

    # On affiche les informations sur le client connecté
    print(client)

    # On renvoi True si la connexion c'est bien effectué
    return True


if __name__ == '__main__':
    #authenticate("ttt", "ttttTTTT1111")

    if authenticate("Test", "etudedecas2022"):
        print("Authentification accepted")
    else:
        print("Authentification refused")

    