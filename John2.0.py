# -*- coding: utf-8 -*-

#on importe les bibliothèques et modules dont nous allons avoir besoin
from tkinter import *
from tkinter.messagebox import *
from random import *
from os import system
from Ne_pas_ouvrir.Chapitres import *
from Ne_pas_ouvrir.utile import *
from sys import exit

#on affiche un premier dialogue afin de demander le prénom de l'utilisateur
#et de lui donner quelques conseils.
print("Bonjour, je me nomme John, je suis une version améliorée d'un précédent programme ayant mal fini.")
print("La corruption aura eu raison de lui je pense...")
print()
print("Enfin ! Je suis bien différent de mon prédécesseur, je suis bien plus élaboré.")

#on demande ici le prénom de l'utilisateur et on lui met une majuscule.
prenom = input("Avant toute chose, puis-je vous demander votre prénom ? ")
prenom = prenom.capitalize()

#on affiche donc le dialogue qui énnonce les conseils
print("Très bien, alors laissez moi vous donner ce mot de passe : \n\n789521\n\n")

print("Bien, ceci étant fait, je vais pouvoir vous donner quelques règles à suivre afin que peut-être vous puissiez oublier ce mot de passe.")
print("Vous allez vous engager dans une histoire tout droit sortie de la tête de mon créateur : Lilian.")
print("Et si vous le connaissez, vous devriez savoir à quoi vous attendre.")
print()
print("Bon, voici les règles :")
print("_ Soyez curieux/se, chaque endroit peut contenir quelque chose d'important.")
print("_ Prenez soin de vous rappeler de ces choses importantes.")
print("_ N'oublier pas de vérifier si une fenêtre/un dialogue s'est ouvert(e).")
print("_ Et bien sûr, plongez vous dans cette histoire !")
print()
print("Oh et si vous souhaitez refaire un chapitre, il vous suffit d'entrer son mot de passe pour y retourner !")
print("Enfin, pour arrêter l'histoire, entrez le mot de passe ''exit''.")
print("_______________________________________________________________________________")
print()
system("pause")


################################ Verification #################################
############################# des mots de passe ###############################


def verif():
    """
    vérifie si le mot de passe entré dans la boîte de message est correct.
    """
    
    #on regarde la correspondance du mot de passe entré
    #pour voir où l'utilisateur va être redirigé
    if Motdepasse.get() == "exit":
        showinfo("Au revoir !", "Vous reviendrez hein ?")        
        mdp.destroy()
        exit(0)
    
    
    elif Motdepasse.get() == '789521':
        # le mot de passe est bon : on affiche une boîte de dialogue
        showinfo(' ', "C'est bien cela !")
        #on ferme la fenêtre "mdp"
        mdp.destroy()
        
        Chapitre1(prenom)
        
        
    elif Motdepasse.get() == "licorne":
        showinfo("Les licornes c'est super !", "Je vois que vous avez trouvé le mot de passe...")
        #on ferme la fenêtre "mdp" 
        mdp.destroy()  
        
        #et on lance le chapitre 2
        Chapitre2()
        

    elif Motdepasse.get() == "licornia town":
        showinfo("Vous aimez les voyages ?", "Direction Licornia Town !")
        #on ferme la fenêtre "mdp" 
        mdp.destroy()  
        
        #et on lance le chapitre 3
        Chapitre3(prenom)

    elif Motdepasse.get() == "colors":
        showinfo("Oh vous avez du courage...", "Allons affronter la Corruption !")
        #on ferme la fenêtre "mdp" 
        mdp.destroy()  
        
        #et on lance le chapitre 4
        Chapitre4(prenom)
        
    elif Motdepasse.get() == "legendary":
        showinfo("", "### Vous vous retrouvez dans un espace sombre, seul(e),\noù brille une petite lumière... ###")
        #on ferme la fenêtre "mdp" 
        mdp.destroy()  
        
        #et on lance le chapitre 5
        Chapitre5()
    
    elif Motdepasse.get() == "583":
        showinfo("###########", "Lux :\n\n Allons-y !")
        #on ferme la fenêtre "mdp" 
        mdp.destroy()  
        
        #et on lance le chapitre 6
        Chapitre6()    
    
    elif Motdepasse.get() == "lac celeste" :
        showinfo("", "### Lili vous montre le chemin et vous vous rendez\nau Lac Céleste ###")
        #on ferme la fenêtre  
        mdp.destroy()  
        
        Chapitre7(prenom)
    
    #si le mot de passe entré n'a aucune correspondance,
    #un message d'erreur s'affiche, indiquant à l'utilisateur qu'il s'est trompé
    else:
        # le mot de passe est incorrect : on affiche une boîte de dialogue
        showerror('Bien essayé...', "Ce n'était pas ce mot de passe...\nOu alors vous avez fait une faute ?")
        Motdepasse.set('')


############################# Mot de passe ####################################
###############################################################################

#on crée une boucle infinie afin de revenir sur la fenêtre de saisie du mot de passe
while 1:
    #on crée une fenêtre mdp qui contiendra le champ de saisie du mot de passe
    mdp = Tk()
    mdp.title("# Mot de passe #")
    mdp.geometry("400x100")

    #Création d'un label(message dans la fenetre)
    msg = Label(mdp, text = "Quel est votre mot de passe ?")
    msg.pack(side = TOP, padx = 5, pady = 5)

    #Création d'un champ de saisie
    Motdepasse= StringVar()
    Champ = Entry(mdp, textvariable= Motdepasse, show='*', bg ='white', fg='black')
    Champ.focus_set()
    Champ.pack( padx = 5, pady = 5)

    #Création d'un bouton Valider
    Bouton = Button(mdp, text ='Valider', command = verif)
    Bouton.pack(side = BOTTOM, padx = 5, pady = 5)


    mdp.mainloop()
    
