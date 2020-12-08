from  tkinter import *
import random
from random import randint
from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas, Entry


def choix_mot():
    # Retourne un mot au hasard du fichier mots.txt
    fichier = open('mots.txt','r+')
    contenu = fichier.readline()
    liste_mots = contenu.split(' ')
    n = randint(0,len(liste_mots))
    mot = liste_mots[n-1]
    fichier.close
    return mot


def affichage_mot(Mot,lettres_trouvees):
    # Affiche le mot mystère avec des '_' à la place  des lettres non découvertes.
    valRen = ""
    for i, L in enumerate(Mot): 
        if i==0 or L in lettres_trouvees:    
            valRen+=L
        else:                                   
            valRen+=" _ "
    cache.set(valRen)
    return valRen


def affichlettres_fausses(lettres_fausses):
    # Affiche les lettres fausses
    valRen=""
    for i in lettres_fausses:
        valRen+=i
        valRen+=" "
    List.set("Lettres fausses : "+valRen)
    return valRen


def check_lettre():
    # check si la lettre saisie par le joueur est dans le mot
    global lettres_trouvees,lettres_fausses,Mot,chance
    
    l=Lettre.get()
    Lettre.set('')

    if isinstance(l,str) and len(l) == 1 and l.isnumeric() == False:
        if l in lettres_trouvees or l in lettres_fausses:                   # si la lettre a déja été donnée
            info.set("Lettre déjà saisies")
        elif l in Mot:                                                      # si la lettre est dans le mot
            lettres_trouvees.append(l)                                      
            affichage_mot(Mot,lettres_trouvees)                             # mis à jour du mot
            info.set("Bien vu!")
        else :
            chance-=1                                               # -1 chance
            lettres_fausses.append(l)                                       
            affichage_Bonhomme()
            cpt.set("Nombre de coups restants: "+str(chance))
            info.set("Raté! Attention!")
            affichlettres_fausses(lettres_fausses)   
    else:
        # info.set("Saisie incorrecte")
        info.set("")


def gagne(Mot,lettres_trouvees):
    # fonction qui vérifie la condition de victoire
    i=0
    for l in Mot:
        if l in lettres_trouvees:
            i+=1
    if i==len(Mot): 
        return True

def affichage_Bonhomme():
    # affiche l'état du bonhomme selon les chances restantes
    global chance
    if chance==7:
        item = Canevas.create_image(150,150,image=image1)
    if chance==6:
        item = Canevas.create_image(150,150,image=image2)
    if chance==5:
        item = Canevas.create_image(150,150,image=image3)
    if chance==4:
        item = Canevas.create_image(150,150,image=image4)
    if chance==3:
        item = Canevas.create_image(150,150,image=image5)
    if chance==2:
        item = Canevas.create_image(150,150,image=image6)
    if chance==1:
        item = Canevas.create_image(150,150,image=image7)
    if chance==0:
        item = Canevas.create_image(150,150,image=image8)      

    
def jeu():
    # fonction principale qui gère le jeu
    global Mot,lettres_trouvees,lettres_fausseslettres_fausses,chance

    affichage_mot(Mot,lettres_trouvees)                                 # affichage du mot avec les lettres trouvées

    if chance>0:                                                        # tant que le joueur n'a pas épuisé ses chances
        check_lettre()

        if gagne(Mot,lettres_trouvees)==True:                           # si condition de gagne réalisée
            info.set("Félicitations !")

    if chance==0 and gagne(Mot,lettres_trouvees)!=True :                # si le nombre de chance épuisé
        info.set("Perdu ! Il a disparu ...")


def Rejouer():
    # fonction qui permet de relancer la fonction principale
    global Mot,lettres_trouvees,lettres_fausses,chance

    Mot=choix_mot() 
    lettres_trouvees=[Mot[0]]                                          
    lettres_fausses=[]
    chance = 8                                                          
    jeu()

    return Mot,lettres_trouvees,lettres_fausses,chance


Mot=choix_mot()
lettres_trouvees=[Mot[0]]                                               # réinitialistation des listes et du nombre de chances
lettres_fausses=[]
chance = 8 


#============================================================================================================


# création de la fenêtre principale
root=Tk()
root.title('PENDU TKINTER')
root.geometry('900x1200')

# definition des images
image1=PhotoImage(master=root, file='bonhomme8.gif')
image2=PhotoImage(master=root, file='bonhomme7.gif')
image3=PhotoImage(master=root, file='bonhomme6.gif')
image4=PhotoImage(master=root, file='bonhomme5.gif')
image5=PhotoImage(master=root, file='bonhomme4.gif')
image6=PhotoImage(master=root, file='bonhomme3.gif')
image7=PhotoImage(master=root, file='bonhomme2.gif')
image8=PhotoImage(master=root, file='bonhomme1.gif')

Largeur=300
Hauteur=300
Canevas=Canvas(root, height= Hauteur, width=Largeur)
item = Canevas.create_image(150,150,image=image1)

Lettre=StringVar()
BoutonEntry=Entry(root,textvariable=Lettre)

BoutonSaisir=Button(root,text='Saisir',command = jeu)
BoutonRejouer=Button(root,text='Rejouer',command=Rejouer)
BoutonQuitter=Button(root,text='Quitter',command=root.destroy)

cache=StringVar()
cache.set(affichage_mot(Mot,lettres_trouvees))
LabelMotRech=Label(root,textvariable=cache)

cpt=StringVar()
cpt.set("Nombre de coups restants: "+str(chance))
label_cpt=Label(root,textvariable=cpt)

List=StringVar()
Labellettres_fausses=Label(root,textvariable=List)

info=StringVar()
console=Label(root, textvariable=info)

# === mise en page ===

label_cpt.grid(row=7,column=2)
LabelMotRech.grid(row=2)
BoutonEntry.grid(row=3)
BoutonSaisir.grid(row=4)
BoutonRejouer.grid(row=5)
BoutonQuitter.grid(row=6)
Labellettres_fausses.grid(row=7)
Canevas.grid(row=1,column=2,rowspan=6)
console.grid(row=8, column=2)

Rejouer()

Mot=Rejouer()[0]
lettres_trouvees=Rejouer()[1]
lettres_fausses=Rejouer()[2]
chance=Rejouer()[3]

root.mainloop()