'''
Sujet : CS-DEV TP 2 : pendu (console) version 1
Auteur : Maxime Curral
Date de creation : 01/12/2020
'''

from random import randint

def choix_mot():
    #retourne un mot au hasard dans mots.txt
    fichier = open('mots.txt','r')
    contenu = fichier.readline()

    liste_mots = contenu.split(' ')
    n = randint(0,len(liste_mots))
    mot = liste_mots[n-1]
    return mot

def check_lettre(lettre,mot):
    #retourne une liste contenant les indexs pour lesquels la
    # lettre entrée par le joueur est dans le mot mystère.
    lettres_decouvertes = []
    i = 0
    for i in range(len(mot)):
        if lettre == mot[i]:
            lettres_decouvertes.append(i)
    return lettres_decouvertes

def affichage(mot,lettres_decouvertes):
    #affiche le mot mystère avec des '_' à la place 
    # des lettres non découvertes.
    affichage_masque=""
    for i in range(len(mot)):
        if int(i) in lettres_decouvertes:
            affichage_masque += mot[i]
        else:
            affichage_masque += ' _ '
    return affichage_masque

def check_input(lettre):
    if isinstance(lettre,str) and len(lettre) == 1 and lettre.isnumeric() == False:
        return True
    else:
        return False

def jeu():
    #Lance le jeu du pendu.
    chances = 8
    mot_mystere = choix_mot()
    lettres_connues = []
    print(mot_mystere)
    while chances > 0:
        lettre = input('Tapez votre lettre :')
        if check_input(lettre):
            if check_lettre(str(lettre), str(mot_mystere)) == []:
                chances-=1
            else:
                for val in check_lettre(str(lettre), str(mot_mystere)):
                    lettres_connues.append(val)
            print(affichage(mot_mystere,lettres_connues))
            print('Il vous reste encore ' + str(chances) + ' chances')
        else:
            print('***Saisie non valide***')
        if chances > 0 and len(lettres_connues) == len(mot_mystere):
            print('Vous avez gagné, le mot était : ' + mot_mystere)
            break
    if len(lettres_connues) != len(mot_mystere):
        print('Dommage, le mot était : ' + mot_mystere)
