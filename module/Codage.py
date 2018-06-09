# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from os import system

def codage(texte_a_coder, code):
    """
    code le texte texte avec un codage
    en +code
    texte est une chaine de caractères
    code est un entier.
    """
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    texte_code = ""
    
    #on parcourt chaque caractère du texte, afin de le traduire.
    for caractere in texte_a_coder:
        if ((caractere == ":") or (caractere =="(") or (caractere == ")") or (caractere == "'") or (caractere == " ") or (caractere == ",") or (caractere == ".") or (caractere == "!") or (caractere == "?") or (caractere == "-") or (caractere == "\n")):
            
            #si c'est une ponctuation, on ne le traduit pas.
            texte_code += caractere
        
        #pour chaque lettre de l'alphabet, on cherche si le caractère y correspond.
        for numero in range(0, len(alphabet)):
            if alphabet[numero] == caractere:
                
                #si oui, alors on écrit le caractère traduit en code dans le texte codé.
                texte_code += alphabet[(numero+code)%25]
        
    
    #on ouvre le fichier dans lequel on va écrire le texte traduit.
    nouveau_texte = open("Texte Codé.txt", "w")
    
    #on y écrit en quel code il a été traduit, puis on écrit le texte codé.
    nouveau_texte.write("Codé en "+str(code)+"\n\n")
    nouveau_texte.write(texte_code)






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
        if ((caractere == ":") or (caractere =="(") or (caractere == ")") or (caractere == "'") or (caractere == " ") or (caractere == ",") or (caractere == ".") or (caractere == "!") or (caractere == "?") or (caractere == "-") or (caractere == "\n")):
            
            #si c'est une ponctuation, on ne le traduit pas.
            texte_decode += caractere
        
        #pour chaque lettre de l'alphabet, on cherche si le caractère y correspond.
        for numero in range(0, len(alphabet)):
            if alphabet[numero] == caractere:
                
                #si oui alors on traduit le caractère avec code, de façon à retrouver la lettre d'origine.
                texte_decode += alphabet[(numero-code)%25]
     
    #on ouvre le fichier dans lequel on va écrire le texte décodé.
    nouveau_texte = open("Texte Décodé.txt", "w")
    nouveau_texte.write(texte_decode)

    
def verif():
    """
    vérifie si le mot de passe entré dans la boîte de message est correct.
    """
    if Motdepasse.get() == "univers":
        showinfo("", "Bien joué !\nVoici l'accès au décodage...")
        #on ferme la fenêtre  
        mdp.destroy()
    
        print("Bien veuillez donc entrer le texte à déccoder :")
        texte = input().lower()
        
        print("Avec quel décodage ?")
        code = int(input())
        
        decodage(texte, code)
        
        print("Le fichier à été créé dans ''module''")
        system("pause")
        
    else :
        Motdepasse.set("")
        showerror("","Dommage, ce n'est pas cela !")
        

print("Mmh, je vois que vous avez trouvé le bon programme...")
print("Seulement rien n'est trop simple, je vous laisse chercher le mot de passe\nnécéssaire afin d'utiliser le décodage...")
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
   
    
    
    
    
    
    
    
    
    

