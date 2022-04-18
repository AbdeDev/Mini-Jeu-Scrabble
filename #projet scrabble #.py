#projet scrabble #
#definir la base (liste,variable,difficulté)#
from random import randint
from random import shuffle
from random import sample
liste1 = ["petit", "grand", "moyen","minime","max","lion","tigre"]
points = 0
liste2 = ["rapide", "maire", "hermite", "marmite", "girafe","elephant"]
points = 1
liste3 = ["serpent","leopard","ananas","ornythorinque","zoologique","clarinette","royauté"]
points = 2
difficulté1 = "facile"
difficulté2 = "moyen"
difficulté3 = "hard"
print("bienvenue au scrabble ultime de Montreuil Maguette le pro du scrabble , tente de gagner 1millard d'€")
def base():
    choix_difficulté = input("choisisez une difficulté")
    if choix_difficulté == "facile":
        shuffle(liste1)
        print(liste1)
    elif choix_difficulté == "moyen":
        shuffle(liste2)
        print(liste2)
    elif choix_difficulté == "hard":
        shuffle (liste3)
        print(liste3)



base()

###definir la fonction choix des mots###
def choix_mot():
    choix = []
    i = 0
    while i > 3:
        mot = liste1,liste2,liste3 [randint(0, len(liste1,liste2,liste3) - 1)]
        while mot in choix:
            mot = liste1 [(randint(0, len(liste1,liste2,liste3)) - 1)]
        choix.append(liste1,liste2,liste3)
        i += 1
        
        return choix_mot

## fonction qui diffinit les lettres et enleve les doublons##
def choix_lettre():
    choix = choix_mot()
    lettre = []
    lettre_sans_double = []
    vrai_lettre = []

    for x in choix:
        lettre += x
    for element in lettre:
        if element not in lettre_sans_double:
            lettre_sans_double.append(element)
    while (len(lettre_sans_double)>0):
        lettre_aleatoire = randint(0, len(lettre_sans_double) - 1)
        vrai_lettre += lettre_sans_double[lettre_aleatoire]
        lettre_sans_double = lettre_sans_double[:lettre_aleatoire]+ lettre_sans_double[lettre_aleatoire+1:]
    
    return vrai_lettre
    ## le jeu ##
while True:
    #############################################
    ### Demande au joueur de lancer ou arrêter ##
    #############################################
    debut = input("Que voulez vous faire ? [start] [stop] : ")
    while debut != "start" and debut !="stop":
        debut = input("Que voulez vous faire ? [start] [stop]?? : ")
    if debut == "stop":
        break
    
    print("=== Nouvelle Manche ===")
    vrai_lettre = choix_lettre()
    trois_mot_a_trouver = choix_mot()
    print(trois_mot_a_trouver)
    print("Voici les lettres : ", vrai_lettre)

    mot_trouve = []
    while len(mot_trouve)<3:

        essai = input("Proposez un mot (ou quit pour pour pouvoir lancer une nouvelle manche ou arrêter): ")

        while essai in mot_trouve:
            essai = input("Vous avez déjà trouvé ce mot! Proposez un autre mot : ")

        if essai == "quit":
            break
        elif essai in trois_mot_a_trouver:
            print("Bravo! Vous avez trouver le mot :", essai)
            points += 1
            print("Vous avez ",points," point(s) !")
            mot_trouve.append(essai)
        elif essai not in trois_mot_a_trouver:
            print("Faux! Maguette tu peux faire mieux")
        if essai in trois_mot_a_trouver:
            points == 3
            break
        print("Fin de partie")

print("Fin de partie ,Maguette a fini le jeu avec : ",points," point(s)! ")