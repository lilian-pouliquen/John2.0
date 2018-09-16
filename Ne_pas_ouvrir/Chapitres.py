# -*- coding: utf-8 -*-

#on importe les bibliothèques et modules dont nous allons avoir besoin
from tkinter import *
from tkinter.messagebox import *
from random import choice
from os import system
from Ne_pas_ouvrir.Utile import *
from sys import exit

def Chapitre1(prenom):
    """
    Lance le chapitre 1 de l'histoire du jeu.
    """
    #On lance un monologue
    print("Nous voici dans le Chapitre 1 ! TINTINTIN !\n")
    print("Quoi ?! Je fais des chapitres moi maintenant ??")
    print("Enfin ! Là n'est pas la question !\n")
    print("Bienvenue dans mon univers, je suis John 2.0 !")
    print("Je ne suis, certes, qu'une machine, mais Lilian m'a quand même doté de sensibilité !")
    print("Disons donc que ce chapitre n'est qu'une présentation de mon monde !")
    print("Alors,", prenom+",", "laissez moi vous présenter cet univers :\n")
    print("Ici, tout peut arriver : Des licornes trottant sur les arcs-en-ciel, jusqu'aux choses les plus sombres...")
    print("Bien entendu je préfère le coin des licornes !\n")
    print("Bref ! Ici, la curiosité est votre meilleure alliée ! Dixit mon cher John, premier du nom... (Le pauvre... Perdu dans les limbes de la corruption...")
    print("Donc voilà, vous pouvez vous attendre à tout et n'importe quoi ! Un mot de passe peut vous passer sous le nez d'un coup !")
    print("Et je suis sûr que vous ne vous atendiez pas à trouver un texte dans le dossier où je suis rangé !")
    print("A bientôt ! Je vous attends au chapitre 2,", prenom, "!")
    print("_______________________________________________________________________________")
    
    #puis on crée un fichier texte dans le dossier de John 2.0
    texte = open("La surprise.txt", "w")
    
    texte.write("Haha ! Je vous avais dit que vous ne vous y attendiez pas !\n\
Alors voilà, cadeau ! C'est le mot de passe du chapitre 2 !\n\n               licorne")
    
    texte.close()
    

def Chapitre2():
    """
    Lance le chapitre deux de l'histoire.
    """    
    print("Bien, je vois que vous aussi vous aimez les licornes mmh ?")
    print("Enfin ! Vous voici dans mon monde. Mais ici, tout n'est pas rose.")
    print("Comme je vous l'ai déjà dit, mon prédécesseur s'est fait avoir par la corruption.")
    print("Voici donc la raison de votre présence ! Vous allez m'aider à vaincre cette corruption !")    
    print("_______________________________________________________________________________")
    print()
    
    #ıon demande à l'utilisateur s'il est d'accord, on attends un "oui" ou autre chose
    daccord = input("Etes-vous vous avec moi ? ")

    if daccord.lower() == "oui":
        print("Très bien, alors allons-y !")
        
    else :
        print("De toute façon vous n'avez pas le choix ! C'est mon univers ici !")
        
    print()
    print()
    
    print("Bon ! Alors voici mon idée :")
    print("J'ai entendu parlé de ces trois codes que devait trouver mon prédécesseur, alors nous devons trouver ces codes ! En revanche ils doivent être protégés...")
    print("Il va donc falloir les trouver, PUIS y accéder...")
    print("Je compte donc sur vous pour le faire, parce que moi je ne peux que vous guider...")
    print()
    print("Alors... par où commencer ? Ah je sais ! J'ai une amie qui vit au coin des licornes...")
    print("Elle devrait pouvoir nous aider !")
    print("Tenez, voici le prochain mot de passe : ")
    print()
    print("licornia town")
    print("_______________________________________________________________________________")


def Chapitre3(prenom):
    """
    lance le chapitre 3
    """
    
    print("Nous y voilà ! Licornia Town, le coin des Licornes !" )    
    print()
    print("Je vais vous présenter à Lili, une de mes amies. Elle devrait être en mesure de vous aider.")
    print("Je vous laisse donc faire connaissance...")
    print("\n")
    print("### John 2.0 s'est éclipsé ###\n")
    print("_______________________________________________________________________________")
    
    system("pause")
    
    #on crée une fenêtre graphique dans laquelle 
    #on affichera l'image de Lili (sans ses couleurs)
    canvas("Lili", "Licorne.gif", 1178, 775)

    print("Lili : Bonjour ! Je suis Lili, enchantée !")
    print("John 2.0 m'a parlé de votre projet. Vous souhaitez donc trouver ces codes de légende ?")
    print("Je devrai pouvoir vous aider. Seulement, j'ai perdu mes couleurs, comme vous pouvez le constater...")
    print("Je vais donc aussi avoir besoin de vous,", prenom, " ! Il faut que vous m'aidiez à retrouver mes couleurs, je serai alors en mesure de vous aider.")
    print("C'est la corruption qui me les a prises... Et je ne pourrais pas me confronter à elle, tandis que vous, vous pouvez vous y confronter ! Vous n'êtes pas de ce monde, alors vous pouvez faire face à la corruption !\n")
    print("Je vais vous mener vers le lieu où mes couleurs ont été corrompues. Il ne vous restera qu'à les sauver !")
    print("Je vous laisse vous préparer, on partira lorsque vous serez prêt(e).")
    print("\nVoici le mot de passe du chapitre 4 : colors")
    print("_______________________________________________________________________________")


def Chapitre4(prenom):
    """
    lance le chapitre 4
    """
    
    print("Lili : Bien,", prenom+",", "nous y voici... C'est ici que sont mes couleurs... Vous pouvez y aller, je vous attends ici, je ne peux pas aller plus loin, ce serait trop risqué...")
    print("\n# Corruption # : Oh mais que vois-je ? Ne serait-ce pas un être humain ?")
    print("J'imagine que ce sont les couleurs que vous voulez... Eh bien bonne chance, Vous ne pourrez me vaicre qu'à l'aide de trois clés ! Haha !")
    print("Ces trois clés, vous ne les aurez qu'en devinant  trois nombres, compris entre 1 et 100, et choisis aléatoirement !")
    print("Bien entendu, vous n'avez que 7 chances pour chaque nombre, ce serait bien trop simple sinon hahaha !")
    print("Bonne chance, vous en aurez besoin !")
    print("_______________________________________________________________________________")
    print()
    
    system("pause")
    #on crée une variable comptant le nombre de clés obtenues par l'utilisateur
    nb_cle = epreuve_Corruption()
        
    #on vérifie que nb_cle soit bien égal à 3 afin de poursuivre l'histoire
    if nb_cle != 3:
        print("Oh comme c'est dommage... Vous avez échoué... HAHAHAHA !!")
        print("C'est donc la fin pour vous...\n")
        
        #si l'utilisateur a échoué, la partie est terminée
        print("### La corruption vous a repoussé(e) et s'est étendue à tout l'univers de John 2.0... C'est la fin... ###")
        exit()
    
    #sinon, l'histoire continue
    else:
        print("### Les clés réagissent et attaquent la Corruption... ###\n") 
        print("AAARGH !!! Vous avez réussi... Les voici vos couleurs !")
        print("Mais ne croyez pas m'avoir vaincue ! J'envahirai tout ce monde et le réduirai à néant !\n")
        print("### La Corruption disparait, laissant les couleurs de Lili revenir vers elle... Ainsi qu'un code : legendary ###\n")
        print("_______________________________________________________________________________")
        
        system("pause")
        #on crée ensuite la fenêtre graphique qui affichera Lili en couleur
        canvas("Lili", "Licorne color.gif", 1178, 775)
        
        print("Lili : Vous avez réussi ! mes couleurs sont de retour !! merci beaucoup !")
        print("Oh, mais... Ce code que la corruption a laissé... C'est un mot de passe légendaire, il vous mènera au premier code !")
        print("_______________________________________________________________________________")
              
        
def Chapitre5():
    """
    lance le chapitre 5 de l'histoire
    """
    print("### Vous vous approchez donc de cette lumière ###")
    print("??? : Oh ! Je vois que quelqu'un s'intéresse aux codes protégés ?")
    print("Dois-je en comprendre que la Corruption commence à sévir ?\n")
    print("Oh pardon, je ne me suis pas présentée ! Je suis Lux ! Gardienne du code qui se trouve ici !")
    print("_______________________________________________________________________________")
    
    system("pause")
    #on crée maintenant une autre fenêtre graphique affichant Lux
    canvas("Lux", "Lux.gif", 890, 552)
    
    print("Lux : J'imagine que vous voulez obtenir le code, mmh ?")
    print("Très bien, alors voici ce que vous devez faire :")
    print("Vous devez trouver 3 chiffres, qui vous permettrons d'atteindre le code protégé.")
    print("C'est tout ce que je peux vous dire... Bonne chance.")
    print("_______________________________________________________________________________")
    
    system("pause")
    #maintenant on crée une fenêtre graphique 
    #affichant Lux avec le premier chiffre recherché
    canvas("Lux", "Lux5.gif", 890, 552)
    
    creation_Fichiers_Chap5()
    
    chiffres = ""
    
    menu = Tk()
    menu.title("Choix")
    menu.geometry("200x75")
    
    revoir = Button(menu, text="Revoir Lux", command = Lux)
    reponse = Button(menu, text="Donner les chiffres à Lux", command = menu.destroy)

    revoir.pack(side = TOP, padx = 5, pady = 5)
    reponse.pack(side = BOTTOM, padx = 5, pady = 5)
    
    menu.mainloop()
    
    #on demande alors à l'utilisateur la bonne combinaison.
    chiffres = input("Dites-moi les trois chiffres dans l'ordre lorsque vous les aurez trouvés : ")
    
    #Tant que l'utilisateur ne donne pas la bonne réponse,
    #il réessaie
    while chiffres != "583":
        print("N'essayez pas de m'arnaquer... Je sais que ce n'est pas les bons chiffres, ou le bon ordre.")
        chiffres = input()

    print("Bravo, je vois que vous avez su trouver les chiffres !")
    print("Fort bien, je peux donc vous ouvrir le passage vers le code légendaire...")
    print("Dites moi lorsque vous serez prêt(e), je vous attendrai dans le chapitre 6, entrez donc les trois chiffres en mot de passe.")
    print("_______________________________________________________________________________")
  
      
def Chapitre6():
    """
    lance le chapitre 6 de l'histoire
    """
    print("### Lux vous ouvre un passage mystérieux ###\n\nLux :\nAllez-y, je connais quelqu'un qui vous attends...")
    print("\n### Vous franchissez le portail de lumière, quelqu'un semble vous attendre de l'autre côté ###")
    print("_______________________________________________________________________________")
    
    system("pause")
    # Création de la fenêtre de l'image de Jelly
    canvas('Jelly', "jelly GIF.gif", 527, 586)
    
    print("\n\nJelly : \nAh ! Vous voilà, Lux m'a parlé de vous !")
    print("Bienvenue dans le premier temple, je suis Jelly, le gardien du code qui s'y cache !")
    print("Bon ! ne perdons pas de temps, entrons dans le temple, je vais vous amener au code.")
    system("pause")
    
    print("\n### Jelly vous emmène devant la porte massive d'une bâtisse antique magnifique,\navant de s'arrêter brusquement ###")
    system("pause")
    
    print("\nJelly : Mmh... Je ne me souviens plus du code pour entrer... ^^'")
    print("Je vais devoir vous soliciter, vous allez devoir traduire le message inscrit sur la porte...")
    print("Pour vous aider il me semble qu'il y a un outil de décodage de la porte quelque part...")
    print("_______________________________________________________________________________")
    system("pause")
    
    print("\n### Vous vous approchez de la porte et y lisez cette inscription : \n\nt'swkqsxo aeo tovvi k oxmybo yelvso vo myno no vk zybdo wwr ?\nlyx, doxoj :\nkxdsdowzvs\n\n< 10 >\n\n")
    print("\nJelly :\nPrévenez moi lorsque vous aurez trouvé...")

    # Création d'un fichier avec le message afin que l'utilisateur puisse le copier
    creation_Fichier_A_Decoder()
    
    # Exécution du fichier Decodage.py
    system("python Ne_pas_ouvrir\\Decodage.py")
        
def Chapitre7(prenom):
    """
    lance le chapitre 7 de l'histoire
    """
    print("### John 2.0 vous attendais au bord du lac ###\n")
    print("John 2.0 : Ah ! Vous voilà ! Lili m'a averti en ce qui concerne le second code...")
    print("Je ne sais absolument pas où il peut être... Il va falloir que vous cherchiez, je sens que la corruption n'est pas loin, Lili et moi ne pouvons donc pas vous aider "+ prenom + ".")
    print("Je vous souhaite bonne chance... \n### John 2.0 disparait ###")
    print("_______________________________________________________________________________")
    
    system("pause")
    
    system("python Ne_pas_ouvrir\\Deplacer.py")
    
def Chapitre8(prenom):
    """
    Lance le chapitre 8 de l'histoire
    """
    
    print("### Vous retournez chez Lili ###")
    print("Lili : Oh vous voilà, John 2.0 m'a avertie de votre venue. Qu'avez-vous trouvé ?")
    print("### Vous lui montrer le cristal ###")
    print()
    print("Oh je vois c'est un cristal des ancêtres, je sais d'où il vient mais pas à quoi il sert.")
    print("_______________________________________________________________________________")
    print()
    
    system("pause")
    
    print("Oh c'est une clef me dites-vous ? Parfait ! Alors dans ce cas nous devons aller au temple aérien.")
    print("Ce n'est pas trop loin d'ici, je vais vous y emmener. Il vou faudra être prudent, ce temple est très ancien,")
    print("il commence à tomber en ruine, les sols ne sont plus aussi solide et vous risquez de passer au travers.")
    print("Sachant que le temple est dans le ciel vous risquez de ne pas apprécier la chute.")
    print()
    print("### Lili vous emmene au temple aérien ###")
    print("_______________________________________________________________________________")
    
    system("pause")
    
    system("python Ne_pas_ouvrir\\Temple_aerien.py")