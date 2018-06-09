# -*- coding: utf-8 -*-
from tkinter import *
from random import *

def canvas(titre, fichier, largeur, hauteur):
    
    nom = Tk()
    nom.title(titre)

    #chargement de l'image nécéssaire
    photo = PhotoImage(file="Ne_pas_ouvrir\\"+fichier)
        
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

            estimation = input("Quelle est votre estimation ? ")#on demande à l'utiliateur son estimation
            estimation = int(estimation)#que l'on traduit en entier
    
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
    zoom = open("Zoom.pbm", "w")
    
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