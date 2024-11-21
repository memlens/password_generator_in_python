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


def subchain_generator(lenght, chaine):
    subChain = ""
    """
    Crée une chaine aléatoire

    Args:
        lenght (int): la longueur de la chaine du mot de passe
        chaine (str): la chaine a modifier

    Return:
        chaine: la sous-chaine
    """
    for i in range(lenght):
        subChain += random.choice(chaine)

    return subChain

def melange_chaine(chaine):
    """
    Modifie l'ordre de la chaine

    Args:
        chaine (str): la chaine à modifier

    Return:
        chaine (str): la chaine modifiée
    """
    liste_chaine = list(chaine)

    random.shuffle(liste_chaine)

    chaine = ''.join(liste_chaine)

    return chaine

def password_generator(lenght, include_uppercase, include_digits, include_symbols):
    """
    Génère un mot de passe aléatoire.

    Args:
        lenght (int): La longueur du mot de passe.
        include_digits (bool): Inclure les lettres majuscules.
        include_digits (bool): Inclure des chiffres.
        include_symbols (bool): Inclure des symboles.

    Returns:
        chaine: Le mot de passe généré.
    """
    chaine1 = string.ascii_lowercase
    chaine2 = string.ascii_uppercase
    chaine3 = string.digits
    chaine4 = string.punctuation
    subLenght = lenght
    rst = ""
    temp1 = ""
    temp2 = ""
    temp3 = ""
    temp4 = ""

    if include_uppercase:
        temp1 = subchain_generator(lenght//4, chaine2)
        subLenght -= lenght//4

    if include_digits:
        temp2 = subchain_generator(lenght//4, chaine3)
        subLenght -= lenght//4

    if include_symbols:
        temp3 = subchain_generator(lenght//4, chaine4)
        subLenght -= lenght//4

    temp4 = subchain_generator(subLenght, chaine1)

    rst = temp1 + temp2 + temp3 + temp4

    rst = melange_chaine(rst)
        
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

    lenght = 0
    while lenght < 8 :
        print("Quelle longueur pour le mot de passe ?? (minimum 8)")
        lenght = int(input("\t : "))

        if lenght < 8 :
            print("Vous devez entrer une valeure supérieur à 8")
            continue
        

    print("Voulez-vous inclure des majuscules ??")
    include_uppercase = input_user()

    print("Voulez-vous inclure des chiffres ??")
    include_digits = input_user()

    print("Voulez vous inclure des caractères spéciaux ??")
    include_symbols = input_user()


    password = password_generator(lenght, include_uppercase, include_digits, include_symbols)

    print(f"Votre mot de passe est : {password}")
    

    print("************************")
