from WordPressAPI import *


def authentification(user, password):
    if (user or password) == ("" or " "):
        return False

    wpa = WordPressAPI(user, password)
    wpa.connect()

    if print(wpa.get()) != None:
        return True
    else:
        return False


if __name__ == '__main__':
   print(" ")
