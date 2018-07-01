# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from os import system

def decodage(texte_a_decoder, code):
    """
    decode le texte texte avec le codage dans lequel
    il a été traduit.
    texte est une chaine de caractères
    code est un entier.
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    texte_decode = ""

    #on parcourt chaque caractère du texte, afin de le traduire.
    for caractere in texte_a_decoder:
        if caractere not in alphabet:
            #si c'est une ponctuation, on ne le traduit pas.
            texte_decode += caractere
        
        #pour chaque lettre de l'alphabet, on cherche si le caractère y correspond.
        for numero in range(0, len(alphabet)):
            if alphabet[numero] == caractere:
                
                #si oui alors on traduit le caractère avec code, de façon à retrouver la lettre d'origine.
                texte_decode += alphabet[(numero-code)%26]
     
    #on ouvre le fichier dans lequel on va écrire le texte décodé.
    nouveau_texte = open("Texte Décodé.txt", "w")
    nouveau_texte.write(texte_decode)

   
def verif():
    """
    vérifie si le mot de passe entré dans la boîte de message est correct.
    """
    if Motdepasse.get() == "univers":
        showinfo("", "Bravo !\nVoici l'accès au décodage...")
        #on ferme la fenêtre  
        mdp.destroy()
    
        print("Bien veuillez donc entrer le texte à déccoder :")
        texte = input().lower()
        
        print("Avec quel décodage ?")
        code = int(input())
        
        decodage(texte, code)
        
        print("Le fichier à été créé dans ''module''")
        system("pause")
        
        print("### VOus appelez Jelly ###\n")
        print("Jelly : Oh vous avez trouvé ? Quel est donc le mot de passe ?\n")
        trouve = input()
        
        sortir_boucle = 0
        
        while sortir_boucle != 1:
            if trouve == "antitempli" :
                print("\n### Vous donnez le mot de passe à Jelly ###")
                print("\n\nAh oui c'est vrai ! Merci, maintenant on peut entrer !")
                print("\n### Vous entrez dans le temple, l'intérieur est sombre, seul un piedestal est illuminé où flotte l'un des mots de passe dont vous avez besoin pour vaincre la corruption ###")
                print("### Le mot ''antitempli'' vient à vous, vous le saisissez puis il disparaît ###")
                print("\nJelly :\nNe vous inquiétez pas, ce code est lié à vous, vous pourrez l'invoquer en temps voulu.")
                print("Bon, j'imagine que j'ai accompli ma mission, alors permettez moi de vous racompagner...")
                print("\n### Jelly vous fait passer à trevers un portail qui vous ramène chez Lili ###")
                print("_______________________________________________________________________________")
                sortir_boucle = 1
            
            else :
                print("\n\nJelly :\nIl ne me semble pas que ce soit cela...")
    
    system("pause")
    print("\nLili :\nOh vous êtes revenu(e) ! J'imagine donc que vous avez réussi, parfait !")
    print("Pendant votre absence je me suis renseignée quant aux autres codes contre la corruption.")
    print("Le prochain se touve au lac céleste !")
    system("pause")
    print("Le mot de passe du chapitre 7 est donc : lac celeste")
    print("_______________________________________________________________________________")
        
    else :
        Motdepasse.set("")
        showerror("","Dommage, ce n'est pas cela !")
        

print("### Vous fouillez un peu les parages et trouvez l'outil dont parlait Jelly ###")
print("### Vous saisissez l'objet numerique et l'allumez")
print("Objet : Bonjour, vous venez d'allumer l'outil de décodage de la porte du temple.")
print("Le problème est que rien n'est trop simple :")
print("Je vous laisse chercher le mot de passe nécéssaire afin d'utiliser le décodage.")
print("Petit indice, il se trouve quelque part dans le dossier ''module'', après c'est à vous de trouver où.")
        

mdp = Tk()
mdp.title("# Mot de passe #")
mdp.geometry("400x100")

#Création d'un label(message dans la fenetre)
msg = Label(mdp, text = "Quel est votre mot de passe ?")
msg.pack(side = TOP, padx = 5, pady = 5)

# Création d'un champ de saisie
Motdepasse= StringVar()
Champ = Entry(mdp, textvariable= Motdepasse, show='*', bg ='white', fg='black')
Champ.focus_set()
Champ.pack( padx = 5, pady = 5)

# Création d'un bouton Valider
Bouton = Button(mdp, text ='Valider', command = verif)
Bouton.pack(side = BOTTOM, padx = 5, pady = 5)


mdp.mainloop() 