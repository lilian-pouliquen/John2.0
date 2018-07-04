# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from time import sleep
from os import system
from Utile import *
from sys import exit

# position initiale du pion
PosX = 430
PosY = 50

info = Tk()
info.title("Insructions")

message = Label(info, text = """Déplacez-vous avec les flèches du clavier\nAppuyez sur "e" pour inspecter la case.""")
message.pack(padx=10, pady=10)

bouton_ok = Button(info, text = "OK", command = info.destroy)
bouton_ok.pack(pady=5, side = BOTTOM)

info.mainloop()

def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX,PosY
    touche = event.keysym

    # déplacement vers le haut
    if touche == 'Up':
        PosY -= 20
    # déplacement vers le bas
    if touche == 'Down':
        PosY += 20
    # déplacement vers la droite
    if touche == 'Right':
        PosX += 20
    # déplacement vers la gauche
    if touche == 'Left':
        PosX -= 20
    # on dessine le pion à sa nouvelle position
    Lac.coords(Pion,PosX -5, PosY -5, PosX +5, PosY +5)

    if touche == "e":
        #on définit la zone d'effet de l'appui sur "e" pour le papier
        if ((PosX,PosY) == (350, 50)):
            espace = Label(fond)
            espace.pack()

            bouton_ok = Button(espace, text = "OK", command = espace.destroy)
            bouton_ok.pack(padx=5, pady=5, side = RIGHT)

            message = Label(espace, text= "''Trouvez les 2 gemmes magiques,\nmontez sur le ponton,\njetez les gemmes magiques au coeur du lac.''")
            message.pack(padx=10, pady=10)



        #on définit la zone d'effet de l'appui sur "e" pour le ponton
        if ((PosX,PosY) == (90,150) or (PosX,PosY) == (110,150) or (PosX,PosY) == (130,150)) :
            if Verif_Succes("gemme_Rouge = True\n") and Verif_Succes("gemme_Bleue = True\n"):
                cache = open("Ne_pas_ouvrir\cache_deplacer.dat", "a")
                cache.write("succes_Lac = True\n")
                cache.close()
                fond.destroy()
            else:
                showinfo("Info", "### Vous ne pouvez rien faire pour l'instant ###")


        #on définit la zone d'effet de l'appui sur "e" pour le coffre

        if (((PosX,PosY) == (390,270)) or  ((PosX,PosY) == (410,270))) :
            if Verif_Succes("gemme_Rouge = True\n"):
                showinfo("Info", "### Il n'y a plus rien ici ###")

            else:
                # Indication dans le cache que la gemme rouge a été trouvée
                cache = open("Ne_pas_ouvrir\cache_deplacer.dat", "a")
                cache.write("gemme_Rouge = True\n")
                cache.close()

                #puis on affiche ce que le joueur a obtenu
                gemme = Frame(fond,borderwidth=2)
                gemme.pack(padx=10,pady=10)

                #création du bouton "OK"
                bouton_ok = Button(gemme, text = "OK", command = gemme.destroy)
                bouton_ok.pack(pady=5, side = RIGHT)

                # Création d'un message
                Label1 = Label(gemme, text = 'Vous obtenez une étrange gemme', fg = 'red')
                Label1.pack(side = BOTTOM)

                #chargement de l'image nécéssaire
                photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Gemme Rouge.gif")
                #création d'une zone graphique
                Largeur = 125
                Hauteur = 178
                obtenu = Canvas(gemme, width = Largeur, height = Hauteur)
                obtenu.create_image(0,0,anchor=NW, image = photo)
                obtenu.pack()

                gemme.mainloop()

        #on définit la zone d'effet de l'appui sur "e" pour le trou
        if ((PosX,PosY) == (70,270)) :
            if Verif_Succes("gemme_Bleue = True\n"):
                showinfo("Info", "### Il n'y a plus rien ici ###")
            else:
                # Indication dans le cache que la gemme rouge a été trouvée
                cache = open("Ne_pas_ouvrir\cache_deplacer.dat", "a")
                cache.write("gemme_Bleue = True\n")
                cache.close()

                #puis on affiche ce que le joueur a obtenu
                gemme = Label(fond)

                #création du bouton "OK"
                bouton_ok = Button(gemme, text = "OK", command = gemme.destroy)
                bouton_ok.pack(pady=5, side = RIGHT)

                # Création d'un message
                label = Label(gemme, text = 'Vous obtenez une étrange gemme', fg = 'blue')
                # Positionnement du widget avec la méthode pack()
                label.pack(side = BOTTOM)
                #chargement de l'image nécéssaire
                photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Gemme Bleue.gif")

                #création d'une zone graphique
                Largeur = 125
                Hauteur = 178
                obtenu = Canvas(gemme, width = Largeur, height = Hauteur)
                obtenu.create_image(0,0,anchor=NW, image = photo)
                obtenu.pack()

                gemme.pack()
                gemme.mainloop()


# Création de la fenêtre principale
fond = Tk()
fond.title("Lac Céleste")

#chargement de l'image nécéssaire
photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Fond Lac.gif")

#création d'une zone graphique
Largeur = 480
Hauteur = 320
Lac = Canvas(fond, width = Largeur, height = Hauteur)
Lac.create_image(0,0,anchor=NW, image = photo)
Lac.pack()

Pion = Lac.create_oval(PosX-5,PosY-5,PosX+5,PosY+5,width=2,outline='black',fill="red")
Lac.focus_set()
Lac.bind('<Key>',Clavier)
Lac.pack(padx =5, pady =5)

#création d'un bouton Quitter
Button(fond, text ='Quitter', command = fond.destroy).pack(side=LEFT,padx=5,pady=5)

fond.mainloop()

if not(Verif_Succes("succes_Lac = True\n")):
    Clear_Cache()
    exit()

######################################## Message ##############################
message = Tk()
message.title("")
message.geometry("250x100")

label = Label(message, text = "### Vous montez sur le ponton et \njetez les deux gemmes à l'eau ###")
label.pack(pady=15)

Button(message, text ='Suite -->', command = message.destroy).pack(side=BOTTOM, pady=5)

message.mainloop()

############################## Lac 1 ##########################################

# Création de la fenêtre principale
fond = Tk()
fond.title("Lac Céleste")

#chargement de l'image nécéssaire
photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Fond Lac.gif")

#création d'une zone graphique
Largeur = 480
Hauteur = 320
Lac = Canvas(fond, width = Largeur, height = Hauteur)
Lac.create_image(0,0,anchor=NW, image = photo)
Lac.pack()

#on attends une seconde avant de passer à la fenêtre suivante
fond.update()
sleep(1)

fond.destroy()
fond.mainloop()

############################ Lac 2 ############################################

# Création de la fenêtre principale
fond = Tk()
fond.title("Lac Céleste")

#chargement de l'image nécéssaire
photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Lac2.gif")

#création d'une zone graphique
Largeur = 480
Hauteur = 320
Lac = Canvas(fond, width = Largeur, height = Hauteur)
Lac.create_image(0,0,anchor=NW, image = photo)
Lac.pack()

#on attends une seconde avant de passer à la fenêtre suivante
fond.update()
sleep(1)

fond.destroy()
fond.mainloop()

########################### Lac 3 #############################################

# Création de la fenêtre principale
fond = Tk()
fond.title("Lac Céleste")

#chargement de l'image nécéssaire
photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Lac3.gif")

#création d'une zone graphique
Largeur = 480
Hauteur = 320
Lac = Canvas(fond, width = Largeur, height = Hauteur)
Lac.create_image(0,0,anchor=NW, image = photo)
Lac.pack()

#on attends une seconde avant de passer à la fenêtre suivante
fond.update()
sleep(1)

fond.destroy()
fond.mainloop()

########################### Lac 4 #############################################

# Création de la fenêtre principale
fond = Tk()
fond.title("Lac Céleste")

#chargement de l'image nécéssaire
photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Lac4.gif")

#création d'une zone graphique
Largeur = 480
Hauteur = 320
Lac = Canvas(fond, width = Largeur, height = Hauteur)
Lac.create_image(0,0,anchor=NW, image = photo)
Lac.pack()

#on attends une seconde avant de passer à la fenêtre suivante
fond.update()
sleep(1)

fond.destroy()
fond.mainloop()

########################### Lac 5 #############################################

# Création de la fenêtre principale
fond = Tk()
fond.title("Lac Céleste")

#chargement de l'image nécéssaire
photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Lac5.gif")

#création d'une zone graphique
Largeur = 480
Hauteur = 320
Lac = Canvas(fond, width = Largeur, height = Hauteur)
Lac.create_image(0,0,anchor=NW, image = photo)
Lac.pack()

#on attends une seconde avant de passer à la fenêtre suivante
fond.update()
sleep(1)

# Création d'un widget Button (bouton Quitter)
Button(fond, text ='Suite -->', command = fond.destroy).pack(side=RIGHT,padx=5,pady=5)
fond.mainloop()

############################## Nouveaux messages ##############################
message = Tk()
message.title("")

label = Label(message, text = "### Un temple est sorti du lac,\nVous vous jetez à l'eau et rejoignez ce dernier. ###")
label.pack(padx=10, pady=10)

bouton_suite = Button(message, text = "Suite -->", command = message.destroy)
bouton_suite.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################

message = Tk()
message.title("")

label = Label(message, text = "### Vous montez sur la plateforme, \net remarquez que deux gemmes sont incrustées dans la porte. ###")
label.pack(padx=10, pady=10)

bouton_suite = Button(message, text = "Suite -->", command = message.destroy)
bouton_suite.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################

message = Tk()
message.title("")

label = Label(message, text = "### Vous les saisissez, et la lourde porte de pierre blanche commence à s'ouvrir lentement.\nVous entrez à l'intérieur du temple. ###")
label.pack(padx=10, pady=10)

bouton_suite = Button(message, text = "Suite -->", command = message.destroy)
bouton_suite.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################

message = Tk()
message.title("Instructions")

label = Label(message, text = "### Utilisez la souris pour déplacer les objets :\n_ Clic gauche pour déplacer la gemme rouge\n_ Clic droit pour déplacer la gemme bleue ###")
label.pack(padx=10, pady=10)

bouton_suite = Button(message, text = "Suite -->", command = message.destroy)
bouton_suite.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################

message = Tk()
message.title("Instructions")

label = Label(message, text = "### Une fois les deux gemmes en place, cliquez sur le piédestal au centre. \n\nAttention, il faut être précis ! ###")
label.pack(padx=10, pady=10)

bouton_ok = Button(message, text = "OK", command = message.destroy)
bouton_ok.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################
###############################################################################

def Clic(event):
    """ Gestion de l'événement Clic gauche """
    global DETECTION_CLIC_SUR_OBJET

    # position du pointeur de la souris
    X = event.x
    Y = event.y

    # coordonnées de l'objet
    [xmin,ymin,xmax,ymax] = Canevas.coords(Gemme_r)

    if xmin<=X<=xmax and ymin<=Y<=ymax: DETECTION_CLIC_SUR_OBJET = True
    else: DETECTION_CLIC_SUR_OBJET = False

    if (((Canevas.coords(Gemme_b) == [385.0, 184.0, 405.0, 200.0]) or (Canevas.coords(Gemme_b) == [385.0, 183.0, 405.0, 199.0])) and ((Canevas.coords(Gemme_r) == [74.0, 184.0, 94.0, 200.0]) or (Canevas.coords(Gemme_r) == [74.0, 183.0, 94.0, 199.0]))) :
        cache = open("Ne_pas_ouvrir\cache_deplacer.dat", "a")
        cache.write("succes_Temple = True\n")
        cache.close()
        sleep(0.5)
        Mafenetre.destroy()

def Clic2(event):
    """ Gestion de l'événement Clic droit """
    global DETECTION_CLIC_SUR_OBJET

    # position du pointeur de la souris
    X = event.x
    Y = event.y

    # coordonnées de l'objet
    [xminb,yminb,xmaxb,ymaxb] = Canevas.coords(Gemme_b)

    if xminb<=X<=xmaxb and yminb<=Y<=ymaxb: DETECTION_CLIC_SUR_OBJET = True
    else: DETECTION_CLIC_SUR_OBJET = False

    if (((Canevas.coords(Gemme_b) == [385.0, 184.0, 405.0, 200.0]) or (Canevas.coords(Gemme_b) == [385.0, 183.0, 405.0, 199.0])) and ((Canevas.coords(Gemme_r) == [74.0, 184.0, 94.0, 200.0]) or (Canevas.coords(Gemme_r) == [74.0, 183.0, 94.0, 199.0]))) :
        cache = open("Ne_pas_ouvrir\cache_deplacer.dat", "a")
        cache.write("succes_Temple = True\n")
        cache.close()
        sleep(0.5)
        Mafenetre.destroy()

def Drag(event):
    """ Gestion de l'événement bouton gauche enfoncé """
    X = event.x
    Y = event.y

    if DETECTION_CLIC_SUR_OBJET == True:
        # limite de l'objet dans la zone graphique
        if X<0: X=0
        if X>Largeur: X=Largeur
        if Y<0: Y=0
        if Y>Hauteur: Y=Hauteur
        # mise à jour de la position de l'objet (drag)
        Canevas.coords(Gemme_r,X-longueur_rect,Y-largeur_rect,X+longueur_rect,Y+largeur_rect)


def Drag2(event):
    """ Gestion de l'événement bouton droit enfoncé """
    X = event.x
    Y = event.y

    if DETECTION_CLIC_SUR_OBJET == True:
        # limite de l'objet dans la zone graphique
        if X<0: X=0
        if X>Largeur: X=Largeur
        if Y<0: Y=0
        if Y>Hauteur: Y=Hauteur
        # mise à jour de la position de l'objet (drag)
        Canevas.coords(Gemme_b,X-longueur_rect,Y-largeur_rect,X+longueur_rect,Y+largeur_rect)


DETECTION_CLIC_SUR_OBJET = False

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Temple")

photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Temple.gif")

# Création d'un widget Canvas
Largeur = 480
Hauteur = 320

longueur_rect = 10
largeur_rect = 8

Canevas = Canvas(Mafenetre,width=Largeur,height=Hauteur,bg ='white')
Canevas.create_image(0,0,anchor=NW, image = photo)

#on définit la position initiale des 2 gemmes
x = 285
x2=200
y = 300
r = 10

# Création d'un objet graphique
Gemme_r = Canevas.create_oval(x-r, y-8, x+r, y+8, outline='yellow', fill='red')
Gemme_b = Canevas.create_oval(x2-r, y-8, x2+r, y+8, outline='yellow', fill='blue')

# La méthode bind() permet de lier un événement avec une fonction
Canevas.bind('<Button-1>',Clic) # évévement clic gauche (press)
Canevas.bind('<B1-Motion>',Drag) # événement bouton gauche enfoncé (hold down)

Canevas.bind('<Button-3>',Clic2)
Canevas.bind('<B3-Motion>',Drag2)

Canevas.focus_set()
Canevas.pack(padx=10,pady=10)

Mafenetre.mainloop()

if not(Verif_Succes("succes_Temple = True\n")):
    Clear_Cache()
    exit()

###############################################################################

message = Tk()
message.title("")

label = Label(message, text = "### La salle se met à trembler... \nPuis, un faisceau lumineux apparaît, éclairant le piédestal au centre.\nUn cristal apparaît alors sur ce dernier. ###")
label.pack(padx=10, pady=10)

bouton_ok = Button(message, text = "OK", command = message.destroy)
bouton_ok.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################

def Clic(event):
    """
    Gestion de l'événement Clic gauche
    """
    global DETECTION_CLIC_SUR_OBJET

    # position du pointeur de la souris
    X = event.x
    Y = event.y

    # coordonnées de l'objet
    [xmin,ymin,xmax,ymax] = fond.coords(objet)

    if xmin<=X<=xmax and ymin<=Y<=ymax: DETECTION_CLIC_SUR_OBJET = True
    if DETECTION_CLIC_SUR_OBJET == True:
        cristal.destroy()



DETECTION_CLIC_SUR_OBJET = False

cristal = Tk()
cristal.title("")

photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Temple cristal.gif")
fond = Canvas(cristal, width=480, height=320, bg="white")
fond.create_image(0, 0, anchor=NW, image = photo)

cote = 30
objet = fond.create_oval(242-cote, 145-cote, 242+cote, 145+cote)

fond.pack(padx=5, pady=5)

fond.bind('<Button-1>',Clic)

message = Label(cristal, text = "Saisissez le cristal.")
message.pack(padx=5, pady=5, side=BOTTOM)

cristal.mainloop()

###############################################################################

cristal = Tk()
cristal.title("")

photo = PhotoImage(file ="Ne_pas_ouvrir\img_lac_celeste\Cristal.gif")
obtenu = Canvas(cristal, width=288, height=339, bg = "white")
obtenu.create_image(0, 0, anchor=NW, image = photo)
obtenu.pack(padx=5, pady=5)

message = Label(cristal, text="Vous obtenez un grand cristal.\nA quoi peut-il servir ?", fg = "green")
message.pack(padx=5, pady=5)

bouton_suite = Button(cristal, text="Suite-->", comman = cristal.destroy)
bouton_suite.pack(padx=5, pady= 5, side = RIGHT)

cristal.mainloop()

###############################################################################
###############################################################################

message = Tk()
message.title("")

label = Label(message, text = "### Le cristal réagit de façon étrange... ###")
label.pack(padx=10, pady=10)

bouton_suite = Button(message, text = "Suite -->", command = message.destroy)
bouton_suite.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################

message = Tk()
message.title("")

label = Label(message, text = "### Le premier code légendaire apparaît alors et le cristal se met à briller...\nD'un coup, vous vous sentez mal à l'aise... ###")
label.pack(padx=10, pady=10)

bouton_suite = Button(message, text = "Suite -->", command = message.destroy)
bouton_suite.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################

message = Tk()
message.title("")

label = Label(message, text = "### Vous décidez donc de sortir du temple\net comprenez tout de suite la raison de votre mauvais sentiment. ###")
label.pack(padx=10, pady=10)

bouton_suite = Button(message, text = "Suite -->", command = message.destroy)
bouton_suite.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################

#ouverture d'une fenêtre graphique
# Création de la fenêtre de corruption
corruption = Tk()
corruption.title('')

#chargement de l'image nécéssaire
photo = PhotoImage(file="Ne_pas_ouvrir\img_lac_celeste\Fond Lac corruption.gif")

#création d'une zone graphique
Largeur = 480
Hauteur = 320
Canevas = Canvas(corruption, width = Largeur, height = Hauteur)
Canevas.create_image(0,0,anchor=NW, image = photo)
Canevas.pack()

bouton_suite = Button(corruption, text = "Suite -->", command = corruption.destroy)
bouton_suite.pack(pady=5, side = BOTTOM)

corruption.mainloop()

###############################################################################

message = Tk()
message.title("")

label = Label(message, text = "### Corruption se présente à vous, vous téléportant près de lui sur les bords du lac. ###")
label.pack(padx=10, pady=10)

bouton_suite = Button(message, text = "Suite -->", command = message.destroy)
bouton_suite.pack(pady=5, side = BOTTOM)

message.mainloop()

###############################################################################

print("Corruption :\nAlors comme ça on approche du deuxième code ? Bien essayé, mais ne crois pas que je vais te laisser faire ainsi !\n\
Et de toute manière tu ne sais que faire de ce cristal n'est-ce pas ? Haha !")
system("pause")
print("\nTu as de la chance, je suis joueur... Alors je vais te proposer quelque chose  :\n\
Si tu me bats, je te dirai quoi faire de ce cristal...\n")
system("pause")

choix = input("Alors, partant(e) ? ")

if choix.lower() == "oui" :
    print("Hahaha, très bien, c'est parti !\n")

else :
    print("Est-ce que je te donnais le choix ? Haha ! Non, pas du tout !!!\n")

print("_______________________________________________________________________________")

###############################################################################
###############################################################################
###############################################################################

info = Tk()
info.title("Insructions")

message = Label(info, text = "Déplacez le curseur avec les flèches du clavier.\n\
Appuyez sur 'Entrer' pour sélectionner.\n\
Chaque objet est à usage unique :\n\
    - Antitempli inflige des dégats\n\
    - Cristal brillant vous soigne et inflige des dégats", justify='left')
message.pack(padx=10, pady=10)

bouton_ok = Button(info, text = "OK", command = info.destroy)
bouton_ok.pack(pady=5, side = BOTTOM)

info.mainloop()

###############################################################################
vie_max_c = 300
vie_max_v = 150

utilise_Mot = False
utilise_Cristal = False

PosX = 38
PosY = 55

def Clavier(event):
    """
    Gestion de l'événement Appui sur une touche du clavier
    """
    global PosX, PosY, vie_max_c, vie_max_v, utilise_Mot, utilise_Cristal
    touche = event.keysym

    # déplacements verticaux selon la position du curseur
    if (PosX) == (160) or (PosX) == (520):
        if (PosX, PosY) == (160, 25):
            if touche == "Down":
                PosY += 60
            if touche == "Left":
                PosX = 38
                PosY = 55
            if touche == "Return":
                if utilise_Mot:
                    showinfo("", "Vous ne puvez plus utiliser cet objet")
                else:
                    vie_max_c -= 75
                    vie_max_v -= Attaque_Corruption()

                    Verifs_Fin_De_Tour(vie_max_c, vie_max_v, lbl_Vie_C, lbl_Vie_V)
                    utilise_Mot = True

        elif (PosX, PosY) == (160, 85):
            if touche == "Up":
                PosY -= 60
            if touche == "Left":
                PosX = 38
                PosY = 55
            if touche == "Return":
                if utilise_Cristal:
                    showinfo("", "Vous ne puvez plus utiliser cet objet")
                else:
                    vie_max_v += 175
                    vie_max_c -= 30
                    vie_max_v -= Attaque_Corruption()

                    Verifs_Fin_De_Tour(vie_max_c, vie_max_v, lbl_Vie_C, lbl_Vie_V)
                    utilise_Cristal = True

        elif (PosX, PosY) == (520, 20):
            if touche == "Down":
                PosY += 35
            if touche == "Left":
                PosX = 388
                PosY = 55
            if touche == "Return":
                vie_max_c -= 50
                vie_max_v -= Attaque_Corruption()

                Verifs_Fin_De_Tour(vie_max_c, vie_max_v, lbl_Vie_C, lbl_Vie_V)

        elif (PosX, PosY) == (520, 55):
            if touche == "Down":
                PosY += 35
            if touche == "Up":
                PosY -= 35
            if touche == "Left":
                PosX = 388
                PosY = 55
            if touche == "Return":
                vie_max_c -= 25
                vie_max_v -= Attaque_Corruption()

                Verifs_Fin_De_Tour(vie_max_c, vie_max_v, lbl_Vie_C, lbl_Vie_V)

        elif (PosX, PosY) == (520, 90):
            if touche == "Up":
                PosY -= 35
            if touche == "Left":
                PosX = 388
                PosY = 55
            if touche == "Return":
                vie_max_c -= 10
                vie_max_v -= Attaque_Corruption()

                Verifs_Fin_De_Tour(vie_max_c, vie_max_v, lbl_Vie_C, lbl_Vie_V)

    # déplacement vers la droite
    elif (PosX, PosY) == (38, 55):
        if touche == 'Right':
            PosX += 350
        if touche == "Return":
            if utilise_Cristal and utilise_Mot:
                showinfo("", "Vous ne puvez plus utiliser d'objets")
            else:
                PosX = 160
                PosY = 25

    # déplacement vers la gauche
    else:
        if touche == 'Left':
            PosX -= 350
        if touche == "Return":
            PosX = 520
            PosY = 20
    # on dessine le pion à sa nouvelle position
    second_ecran.coords(point1,PosX -6, PosY -6, PosX +6, PosY +6)

    # Actions si la vie d'un d'es deux est à zéro
    if vie_max_c <= 0:
        showinfo("", "Vous avez vaincu la Corruption !")
        sleep(0.5)
        combat.destroy()

        cache = open("Ne_pas_ouvrir\cache_deplacer.dat", "a")
        cache.write("succes_Combat = True\n")
        cache.close()

    elif vie_max_v <= 0:
        showinfo("", "La Corruption vous a battu(e)...\n\Vous vous faites expulser du monde de John2.0 laissant la Corruption s'en emparer\n\n Fin de partie.")
        sleep(0.5)
        combat.destroy()
        Clear_Cache()


combat = Tk()
combat.title("")

photo = PhotoImage(file = "Ne_pas_ouvrir\img_lac_celeste\Combat.gif")
fond = Canvas(combat, width=647, height=367)
fond.create_image(0, 0, anchor=NW, image=photo)
fond.pack(padx=5, pady=5)

lbl_Vie_C = Label(fond,text = vie_max_c, font=("Fixedsys", 25), bg="white")
lbl_Vie_C.pack()

lbl_Vie_V = Label(fond,text = vie_max_v, font=("Comic Sans MS", 24), bg="white")
lbl_Vie_V.pack()

fond.create_window(170, 60, window = lbl_Vie_C)
fond.create_window(550, 333, window = lbl_Vie_V)

photo2 = PhotoImage(file = "Ne_pas_ouvrir\img_lac_celeste\Attaque Objet.gif")
second_ecran = Canvas(combat, width=651, height=112)
second_ecran.create_image(0, 0, anchor=NW, image = photo2)
second_ecran.pack()

point1 = second_ecran.create_oval(PosX-6, PosY-6, PosX+6, PosY+6, fill="black")
second_ecran.focus_set()
second_ecran.bind('<Key>',Clavier)
second_ecran.pack(padx=5, pady=5)

combat.mainloop()

# Actions suivant l'issue du combat
if not(Verif_Succes("succes_Combat = True\n")):
    Clear_Cache()
    exit()
else:
    Clear_Cache()
    print("Corruption : Argh... Tu m'as eu... Très bien... Chose promise, chose due...")
    print("Le cristal que tu possède sert de clef pour trouver le deuxième code légendaire...")
    print("C'est tout ce que je peux te dire...\n")
    print("### Corruption disparaît ###\n")
    system("pause")

    print("### John2.0 apparaît un peu essoufflé ###\n")
    print("John2.0 : Vous avez repoussé Corruption ? Parfait ! Nous allons pouvoir continuer !")
    print("Qu'avez-vous donc trouvé ?\n")
    print("### Vous expliquez à John2.0 ce que vous avez trouvé ###\n")
    system("pause")

    print("John2.0 : Mmh je vois. Il faut donc aller voir Lili, elle a peut-être quelques infos pour nous !\n")
    print("Le prochain mot de passe est 'le cristal', on se retrouve chez notre amie la licorne !\n")
    print("_______________________________________________________________________________")
    system("pause")
    