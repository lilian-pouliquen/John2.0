# -*- coding: utf-8 -*-

from tkinter import *
from random import choice


def verif_Nombre(nombre):
    ok = False
    
    while (not(ok)):
        try:
            nombre = int(nombre)
        except:
            nombre = input("\nCe n'est pas un nombre, veuillez saisir à nouveau : ")
        
        else:
            ok = True
        
    return nombre


def canvas(titre, fichier, largeur, hauteur):
    
    nom = Tk()
    nom.title(titre)

    #chargement de l'image nécéssaire
    photo = PhotoImage(file="Ne_pas_ouvrir/"+fichier)
        
    #création d'une zone graphique
    
    Canevas = Canvas(nom, width = largeur, height = hauteur)
    Canevas.create_image(0,0,anchor=NW, image = photo)
    Canevas.pack()
        
    nom.mainloop()


def epreuve_Corruption():
    nb_cle = 0

    #on fait ensuite une boucle qui tournera
    #tant que l'utilisateur n'aura pas 3 clés
    while (nb_cle != 3):    
        #on choisi un nombreau hasar dans la liste que l'on a créé
        nombre = choice(range(1, 101))
        
        #on crée une boucle for, afin de déduire
        #le nombre d'essais restants
        for I in range(1, 8):
            #on demande à l'utiliateur son estimation
            estimation = input("Quelle est votre estimation ? ")
            estimation = verif_Nombre(estimation)
            #puis on teste la valeur de l'estimation, afin de voir
            #si elle correspond au nombre à trouver
            if estimation == nombre:
               print("Correct, c'était bien", nombre)
               print("Accès au " + str(nb_cle+2) + "ème nombre.\n")
               break
            #si l'estimation est supérieure au nombre,
            #on indique à l'utilisateur que le nombre est plus petit
            if estimation > nombre:
                print("Le nombre est plus petit")
                print()
            #sinon on indique qu'il est plus grand
            else:
                print("Le nombre est plus grand")
                print()

        #si l'utilisateur n'a pas trouvé le nombre au bout
        #de 7 essais, alors il a perdu
        if estimation != nombre :
            print("Vous n'avez plus d'essais...")
            break
        #sinon on passe au nombre suivant
        else :
            nb_cle += 1
    
    return nb_cle
    
def Lux():
    nom = Toplevel()
    nom.title("Lux")

    #chargement de l'image nécéssaire
    photo = PhotoImage(file="Ne_pas_ouvrir/Lux5.gif")
        
    #création d'une zone graphique
    
    Canevas = Canvas(nom, width = 890, height = 552)
    Canevas.create_image(0,0,anchor=NW, image = photo)
    Canevas.pack()
        
    nom.mainloop()


def creation_Fichiers_Chap5():
    #on crée un fichier texte contenant le deuxième chiffre.
    chiffre_2 = open("La lumière de la pénombre.txt", "w")
    
    #on écrit dans ce fichier.
    chiffre_2.write("Vous cherchez bien à ce que je vois...\nTrès bien ! Alors laissez moi temps avant de vous donner ce vous cherchez !\
\nJ'ai une idée, parlons un peu de Lux, la gardienne !\n\nC'est un poisson très spécial, en plus de ne pouvoir être vue que de profil, \
\npeu importe l'angle avec lequel vous la regardez, elle est facile à représenter et elle est lumineuse ! D'où son nom d'ailleurs...\
\nElle est de plus utilisé dans d'autres endroits de cet univers afin de représenter une personne spéciale... \nEnfin ! Cela devrait être assez\
à propos de cette chère petite Lux !\n\nVoici ce que vous recherchez : 8")
    
    #puis on ferme le fichier
    chiffre_2.close()
    
    #on crée ensuite un fichier image (très petite) où se trouve le troisième chiffre.
    zoom = open("Zoom.bmp", "w")
    
    #on écrit dans ce fichier afin de créer une image.
    zoom.write("P1\n28 15\n")
    zoom.write("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n\
0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n\
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n\
0 0 0 0 1 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n\
0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n\
0 0 1 0 0 0 0 0 1 0 0 0 1 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0\n\
0 1 1 1 1 1 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0\n\
0 0 0 0 0 0 0 0 1 1 1 1 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0\n\
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 1 1 0 1 1 0 0 0\n\
0 1 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 1 0 1 0 1 0 0 0\n\
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0\n\
0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0\n\
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0\n\
0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n\
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
    
    #on ferme le fichier.
    zoom.close()


def creation_Fichier_A_Decoder():
    #on crée un fichier texte contenant la phrase à décoder.
    fichier = open("./module/Texte_a_decoder.txt", "w")
    
    #on écrit dans ce fichier.
    fichier.write("t'swkqsxo aeo tovvi k oxmybo yelvso vo myno no vk zybdo wwr ? lyx, doxoj : kxdsdowzvs\n\n< 10 >")
    
    #puis on ferme le fichier
    fichier.close()
    
    
def Verif_Succes(succes):
    """
    Vérifie si un passage a été fait correctement dans deplacer.py
    Renvoie Vrai si le succes est présent dans le cache
    """
    cache = open("Ne_pas_ouvrir/cache_deplacer.dat", "r")
    clefs = cache.readlines()
    cache.close()
    flag = False
    i = 0
    
    while not(flag) and i < len(clefs):
        if clefs[i] == succes:
            flag = True
        else:
            i += 1
    
    return flag
    
    

def Clear_Cache():
    cache = open("Ne_pas_ouvrir/cache_deplacer.dat", "w")
    cache.write("")
    cache.close()
    
    
def Attaque_Corruption():
    """
    Choix de l'attaque utilisée par la Corruption dans le combat du chapitre 7
    """
    choix = choice(range(1,5))
    
    if choix == 1:
        return 100
    elif choix == 2:
        return 50
    elif choix == 3:
        return 30
    else :
        return 15
    
    
def Verif_Vie(vie):
    """
    Si la vie donnée en paramètre est négative, on la ramène à 0
    """
    if vie < 0:
        vie = 0
    
    return vie

def Verifs_Fin_De_Tour(vie1, vie2, label1, label2):
    """
    Effectue les vérifications de fin de tour du combat
    """
    vie1 = Verif_Vie(vie1)
    vie2 = Verif_Vie(vie2)
    label1.config(text=vie1)
    label2.config(text=vie2)
