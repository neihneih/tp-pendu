'''
Sujet : CS-DEV TP 2 : pendu (console) version 2
Auteur : Maxime Curral
Date de creation : 01/12/2020
'''


from random import randint


def choix_mot():
    # Retourne un mot au hasard du fichier mots.txt
    fichier = open('mots.txt','r')
    contenu = fichier.readline()
    liste_mots = contenu.split(' ')
    n = randint(0,len(liste_mots))
    mot = liste_mots[n-1]
    fichier.close
    return mot


def check_lettre(lettre,mot):
    # Retourne une liste contenant les indexs pour lesquels la lettre entrée par le joueur est dans le mot mystère.
    lettres_decouvertes = []
    i = 0
    for i in range(len(mot)):
        if lettre == mot[i]:
            lettres_decouvertes.append(i)
    return lettres_decouvertes


def affichage(mot,lettres_decouvertes):
    # Affiche le mot mystère avec des '_' à la place  des lettres non découvertes.
    affichage_masque = ""
    for i in range(len(mot)):
        if int(i) in lettres_decouvertes:
            affichage_masque += mot[i]
        else:
            affichage_masque += ' _ '
    return affichage_masque


def check_input(lettre):
    # Vérifie que la saisie est bien une seule lettre.
    if isinstance(lettre,str) and len(lettre) == 1 and lettre.isnumeric() == False:
        return True
    else:
        return False


def check_meilleur_score(score):
    # Interroge le fichier score pour comparer le score de la partie et le meilleur score réalisé, et le met à jour si besoin.
    fichier = open('score.txt','r')
    meilleur_score = fichier.readline()
    fichier.close
    if int(meilleur_score) < score:
        fichier = open('score.txt','w')
        fichier.write(str(score))
        fichier.close
        return score
    else:
        return meilleur_score


def jeu():
    #Lance le jeu du pendu.
    chances = 8
    mot_mystere = choix_mot()                                                               # Génération aléatoire du mot
    lettres_connues = []                                            
    lettres_saisies = []

    while chances > 0:                                                                      # Le jeu se poursuit tant qu'il reste des tentatives
        lettre = input('Tapez votre lettre :')                                              # Saisie de la lettre
    
        if check_input(lettre):                                                             # Vérification de la saisie
    
            while lettre in lettres_saisies:                                                # Vérification de si la lettre a déjà été saisie
                print("vous avez deja saisi la lettre")
                lettre = input('Tapez votre lettre :')
            lettres_saisies.append(lettre)                                                  # Ajout de la lettre pas encore saisie dans la liste de lettres déjà saisies 
    
            if check_lettre(str(lettre), str(mot_mystere)) == []:                           # Si la lettre saisie n'est pas dans le mot
                chances -= 1                                                                  # --> tentatives -1
    
            else:
                for val in check_lettre(str(lettre), str(mot_mystere)):                     # Si la lettre est dans le mot,
                    lettres_connues.append(val)                                             # Ajout de la lettre dans la liste à afficher

            print(affichage(mot_mystere,lettres_connues))
            print('Il vous reste encore ' + str(chances) + ' chances')
        
        else:
            print('***Saisie non valide***')

        if chances > 0 and len(lettres_connues) == len(mot_mystere):                        # Condtions de victoire
            print('Vous avez gagné, le mot était : ' + mot_mystere)                         
            score = chances                                                                 # Affichage du score et du meilleur score jusqu'à maintenant
            print('Votre score est : ' + str(score) + '\n' + 'Le meilleur score est : ' + str(check_meilleur_score(score)))            
            replay()

    if len(lettres_connues) != len(mot_mystere):                                            # Conditions de défaite
        print('Dommage, le mot était : ' + mot_mystere)
        replay()


def replay():
    # Demande au joueur s'il veut faire une autre partie.
    replay = input('Voulez-vous rejouer ? (o/n)')
    if replay == 'o':                                                                       # S'il veut rejouer, le jeu se relance.
        jeu()
    elif replay == 'n':                                                                     # Sinon, le programme s'arrête.
        exit()
    else:                                                                                   # Si la saisie est invalide, la fonction recommence.
        replay()