"""
Un générateur de moot de passe sécurisé
"""

import random
import string


def need_upper(answer):
    """ 
    Vérifie si le user veux utiliser des lettres majuscules

    Args:
        answer (char): la reponse de l'utilisateur sur son choix d'utiliser des lettres majuscules

    Return:
        choice : le choix si on inclus ou pas des majuscules
    """
    choice = False
    if answer == 'y':
        choice = True
    return choice

def need_digits(answer):
    """ 
    Vérifie si le user veux utiliser des chiffres

    Args:
        answer (char): la reponse de l'utilisateur sur son choix d'utiliser des chiffres

    Return:
        choice : le choix si on inclus ou pas des chiffres
    """
    choice = False
    if answer == 'y':
        choice = True
    return choice

def need_symbols(answer):
    """ 
    Vérifie si le user veux utiliser des symboles

    Args:
        answer (char): la reponse de l'utilisateur sur son choix d'utiliser des symboles

    Return:
        choice : le choix si on inclus des symboles
    """
    choice = False
    if answer == 'y':
        choice = True
    return choice

def password_generator(length, include_uppercase, include_digits, include_symbols):
    """
    Génère un mot de passe aléatoire.

    Args:
        length (int): La longueur du mot de passe.
        include_digits (bool): Inclure les lettres majuscules.
        include_digits (bool): Inclure des chiffres.
        include_symbols (bool): Inclure des symboles.

    Returns:
        chaine: Le mot de passe généré.
    """
    chaine = string.ascii_lowercase
    rst = ""

    if include_uppercase:
        chaine += string.ascii_uppercase

    if include_digits:
        chaine += string.digits

    if include_symbols != "":
        chaine += string.punctuation 

    for i in range(length):
        rst += random.choice(chaine)

    print(chaine)
        
    return rst

def input_user():
    """
    Récupère l'entrée utilisateur et recupère la valeur si elle correspond

    """
    haveToControl = ['y', 'n']
    choice = False
    while True:
        user_input = input("\t : ")

        if user_input not in haveToControl:
            print("Vous devez entrer 'y' ou 'n', veuillez réessayer !!")
            continue
        break

    if user_input == 'y':
        choice = True

    return choice

if __name__ == '__main__':
    print("Welcome motherFucker ! \n")
    print("Busy about choosing a password, i'm your man.\n")

    print("************************")

    print("Quelle longueur pour le mot de passe ??")
    lenght = int(input("\t : "))

    print("Voulez-vous inclure des majuscules ??")
    include_uppercase = input_user()

    print("Voulez-vous inclure des chiffres ??")
    include_digits = input_user()

    print("Voulez vous inclure des caractères spéciaux ??")
    include_symbols = input_user()


    password = password_generator(lenght, include_uppercase, include_digits, include_symbols)

    print(f"Votre mot de passe est : {password}")
    

    print("************************")