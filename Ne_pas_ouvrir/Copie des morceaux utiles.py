# -*- coding: utf-8 -*-

#vérification des mots de passe
elif Motdepasse.get() == "":
        showinfo("", "")
        #on ferme la fenêtre  
        mdp.destroy()  
        
        Chapitre___()
        

#ouverture d'une fenêtre graphique
# Création de la fenêtre de ___
___ = Tk()
___.title('___')

#chargement de l'image nécéssaire
photo = PhotoImage(file="Ne pas ouvrir (spoil)\___.gif")
    
#création d'une zone graphique
Largeur = ___
Hauteur = ___
Canevas = Canvas(___, width = Largeur, height = Hauteur)
Canevas.create_image(0,0,anchor=NW, image = photo)
Canevas.pack()
    
___.mainloop()



#messages
message = Tk()
message.title("")

label = Label(message, text = "###  ###")
label.pack(padx=10, pady=10)

bouton_ok = Button(message, text = "OK", command = message.destroy)
bouton_ok.pack(pady=5, side = BOTTOM)

message.mainloop()