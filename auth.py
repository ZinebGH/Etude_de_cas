from WordPressAPI import *


def authentification(user, password):
    if (user or password) == ("" or " "):
        return False

    wpa = WordPressAPI(user, password)
    wpa.connect()

    response = wpa.get(
        "https://etu2cas.wpcomstaging.com//wp-json/jwt-auth/v1/token/validate")

    # response = wpa.get(
    #     "https://etu2cas.wpcomstaging.com/wp-json/wp/v2/users/me")

    if response != None:
        return True
    else:
        return False


if __name__ == '__main__':
    #authentification("ttt", "ttttTTTT1111")
    if authentification("Test", "etudedecas2022"):
        print("Authentification accepted")
    else:
        print("Authentification refused")
