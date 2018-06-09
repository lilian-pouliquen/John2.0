# -*- coding: utf-8 -*-
#on importe les bibliothèques et modules dont nous allons avoir besoin
from tkinter import *
from tkinter.messagebox import *
from random import *
from os import system
from Ne_pas_ouvrir.utile import *

def Chapitre1(prenom):
    """
    Lance le chapitre 1 de l'histoire du jeu.
    """
    #On lance un monologue
    print("Quoi ?! Je fais des chapitres moi maintenant ??")
    print("Enfin ! Là n'est pas la question ! Nous voici dans le Chapitre 1 ! TINTINTIN ! (D'accord j'arrête...)\n")
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
    lili = Tk()
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
    epreuve_Corruption()
        
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
        lili = Tk()
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
    Lux = Tk()
    canvas("Lux", "Lux.gif", 890, 552)
    
    print("Lux : J'imagine que vous voulez obtenir le code, mmh ?")
    print("Très bien, alors voici ce que vous devez faire :")
    print("Vous devez trouver 3 chiffres, qui vous permettrons d'atteindre le code protégé.")
    print("C'est tout ce que je peux vous dire... Bonne chance.")
    print("_______________________________________________________________________________")
    
    system("pause")
    #maintenant on crée une fenêtre graphique 
    #affichant Lux avec le premier chiffre recherché
    Lux_5 = Tk()    
    canvas("Lux", "Lux 5.gif", 890, 552)
    
    creation_Fichiers_Chap5()
    
    #on crée une boucle infinie afin de redemender les chiffres jusqu'à ce que
    #l'utilisateur entre la bonne réponse.
    while 1 :
        #on demande alors à l'utilisateur la bonne combinaison.
        chiffres = input("Dites-moi les trois chiffres dans l'ordre lorsque vous les aurez trouvés : ")
    
        if chiffres == "583":
            print("Bravo, je vois que vous avez su trouver les chiffres !")
            print("Fort bien, je peux donc vous ouvrir le passage vers le code légendaire...")
            print("Dites moi lorsque vous serez prêt(e), je vous attendrai dans le chapitre 6, entrez donc les trois chiffres en mot de passe.")
            print("_______________________________________________________________________________")
            break
        
        else : 
            print("N'essayez pas de m'arnaquer... Je sais que ce n'est pas les bons chiffres, ou le bon ordre.")

            
def Chapitre6():
    """
    lance le chapitre 6 de l'histoire
    """
    print("### Lux vous ouvre un passage mystérieux ###\n\nLux :\nAllez-y, je connais quelqu'un qui vous attends...")
    print("\n### Vous franchissez le portail de lumière, quelqu'un semble vous attendre de l'autre côté ###")
    print("_______________________________________________________________________________")
    
    system("pause")
    # Création de la fenêtre de l'image de Jelly
    Jelly = Tk()
    canvas('Jelly', "jelly GIF.gif", 527, 586)
    
    print("\n\nJelly : \nAh ! Vous voilà, Lux m'a parlé de vous !")
    print("Bienvenue dans le premier temple, je suis Jelly, le gardien du code qui s'y cache !")
    print("Bon ! ne perdons pas de temps, entrons dans le temple, je vais vous amener au code.")
    system("pause")
    
    print("\n### Jelly vous emmène devant la porte massive d'une bâtisse antique magnifique,\navant de s'arrêter brusquement ###")
    system("pause")
    
    print("\nJelly : Mmh... Je ne me souviens plus du code pour entrer... ^^'")
    print("Je vais devoir vous soliciter, vous allez devoir traduire le message inscrit sur la porte...")
    print("Pour vous aider il me semble qu'il y a un dossier ''module'', peut-être pourriez vous y faire un tour ?")
    print("_______________________________________________________________________________")
    system("pause")
    
    #on crée un fichier afin que l'utilisateur puisse copier l'inscription.
    inscription = open("Inscription.txt", "w")
    inscription.write("t'swkqsxo bfo tovvj k oxmyco yflvso vo myno no vk ayceo wwr ? lyx eoxok : kxeseowavs")
    inscription.close()
    
    print("\n### Vous vous approchez de la porte et y lisez cette inscription : \n\nt'swkqsxo bfo tovvj k oxmyco yflvso vo myno no vk ayceo wwr ?\nlyx eoxok :\nkxeseowavs\n\n< 10 >\n\n(Vous pouvez copier cette phrase dans le dossier ''John 2.0'')")
    print("\nJelly :\nPrévenez moi lorsque vous aurez trouvé...")
    
    #on crée une variable qui permet de sortir de la boucle while
    sortir_boucle = 0
    
    #tant que l'on entrera pas le bon mot de passe, la boucle tournera
    while sortir_boucle != 1:
        #on demande à l'utilisateur d'entrer le mot de passe de la traduction
        trouve = input("(Entrez le mot de passe de la traduction ici)\n")
    
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
            sortir_boucle = 0
    
    system("pause")
    print("\nLili :\nOh vous êtes revenu(e) ! J'imagine donc que vous avez réussi, parfait !")
    print("Pendant votre absence je me suis renseignée quant aux autres codes contre la corruption.")
    print("Le prochain se touve au lac céleste !")
    system("pause")
    print("Le mot de passe du chapitre 7 est donc : lac celeste")
    print("_______________________________________________________________________________")

    
    
    
    
    
    
    
    
    
def Chapitre7():
    """
    lance le chapitre 7 de l'histoire
    """        
    print("### John 2.0 vous attendais au bord du lac ###\n")
    print("John 2.0 : Ah ! Vous voilà ! Lili m'a averti en ce qui concerne le second code...")
    print("Je ne sais absolument pas où il peut être... Il va falloir que vous cherchiez, je sens que la corruption n'est pas loin, Lili et moi ne pouvons donc pas vous aider "+ prenom + ".")
    print("Je vous souhaite bonne chance... \n### John 2.0 disparait ###")
    print("_______________________________________________________________________________")
    
    system("pause")
    
    info = Tk()
    info.title("Insructions")
    
    message = Label(info, text = "Rendez-vous dans le dossier ''Module''.\nIl y a un programme nommé Lac Céleste qui vous attend.\nIl vous faudra passer par ce dernier, pour continuer...")
    message.pack(padx=10, pady=10)
    
    bouton_ok = Button(info, text = "OK", command = info.destroy)
    bouton_ok.pack(pady=5, side = BOTTOM)
    
    info.mainloop()
