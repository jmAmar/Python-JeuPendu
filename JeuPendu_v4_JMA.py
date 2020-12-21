#!python3.9
#coding: utf-8

#module: Listes_v7
#date: 13/12/2020
#author: jmAmar


print("\n\t**** Jeu du Pendu ****\n")

def lancer() :
    # initialiation et exécution du jeu
    initialiser()
    print("\n... à vous de jouer ... \n")
    executer()


def initialiser() :

    import random

    # themes
    global animaux_savane
    animaux_savane = ["girafe", "elephant", "crocodile", "mangouste", "leopard", "serval", "phacochere", "gnou", "gazelle", "guepard"]
    global poissons_mer
    poissons_mer = ["hareng", "turbot", "sardine", "morue", "esturgeon", "anguille", "brochet", "baudroie", "hyppocampe", "rascasse"]
    global fleurs
    fleurs = ["jonquille", "geranium", "marguerite", "petunia", "orchidee", "edelweiss", "hibiscus", "camelia", "azalee", "coquelicot"]

    theme = selectionner()
    global mot    # mot à deviner
    mot = random.choice(theme).upper()
    # longueur du mot à deviner
    n = len(mot)

    global echafaud  # séquence scripturale de pendaison
    echafaud = ["potence", "corde", "tete", "corps", "brasGauche", "brasDroit", "jambeGauche", "jambeDroite", "! pendu !"]
    global pendu     # séquence de pendaison en fonction de la longeur du mot à deviner
    pendu = echafaud[-n:]

    # ajoute des éléments de présentation à chaque élément de la liste pendu
    # v1
    """
    i = 0
    while(i < len(pendu)) :
        pendu[i] = (">>" + pendu[i] + " ")
        i += 1
    """
    # v2
    """
    for s in pendu :
        i = pendu.index(s)
        s = ">>" + s + " "
        pendu[i] = s
    """
    # v3
    pendu = [(">>" + s + " ")  for s in pendu]

    # initialisation de la séquence de saisie du joueur en underscores
    global saisie
    saisie = []
    i = 0
    while(i < n) :
        saisie.append("_")
        i += 1

    global pendaison    # séquence des erreurs = séquence dynamique scripturale de pendaison
    pendaison = []



def selectionner() :  # sélection du thème du mot à deviner

    themes1 = {"A":animaux_savane, "P":poissons_mer, "F":fleurs}
    themes2 = {"A":"animaux de la savane", "P":"poissons de mer", "F":"fleurs"}

    print("** sélection du thème **")
    print("  animaux de la savanne\t:  A")
    print("  poissons de mer\t:  P")
    print("  fleurs\t\t:  F")
    print("  quitter\t\t:  Q")
    choix = input("\n\tchoix du thème\t? ").upper()
    print("\tchoix du thème\t:", choix)

    if(choix == "Q") :
        print("\t\t\t" + "quitter")
        import sys
        sys.exit()
    else :
        if(choix in themes1) :
            print("\t\t\t" + themes2[choix])
            return(themes1[choix])
        else :
            print("\t\t\t! choix invalide !")
            lancer()


# définition de la fonction de jeu
def jouer(x) :
    # x = index du dernier élément de la séquence de pendaison (pendu)

    lettre = input("lettre (sans accent)\t? ").upper()    # conversion en majuscule de la lettre saisie
    print("lettre\t:", lettre)

    if(lettre in mot):
        # si la lettre saisie figure dans le mot à deviner,
        # alors le programme récupère l'index de celle-ci dans le mot
        # puis la place dans la séquence de saisie
        # lettres en doublon dans le mot sont traitées
        i = 0
        for l in mot :
            if(lettre == l) :
                saisie[i] = lettre
            i += 1
        return("OK")
    else :
        # si la lettre saisie ne figure pas dans le mot à deviner,
        # alors la séquence dynamique de pendaison est complétée
        pendaison.append(pendu[x])
        return("NO")


def executer() :
    # initialisation des variables d'exécution
    i = 0   # index de la séquence de saisie
    j = 0   # index de la séquence de pendaison
    n = 0   # compteur de saisies du joueur
    r = ""  # résultat de la fonction jouer()
    resultat =  ""  # séquence de résultat

    # exécution du jeu
    while(n < (len(echafaud) + len(mot))) :
        n += 1  # incrémente le compteur de saisies du joueur
        r = jouer(j)
        if(r == "OK") :
            resultat = ""
            # insert des blancs entre les lettres de la séquence de saisies valides
            for s in saisie :
                resultat += (s + " ")
            print("résultat : ", resultat, "\n")
            # ré-affecte la séquence de résultat
            resultat = "".join(saisie)  # convertit la liste contenant la séquence de saisies valide en string
            if(resultat == mot) :
                print("\t!! gagné !!")
                break
        if(r == "NO") :
            resultat = "".join(pendaison)    # convertit la liste contenant la séquence de pendaison en string
            print("résultat :", resultat, "\n")
            j += 1  # incrémente l'index de la séquence de pendaison
            if(pendaison[-1] == pendu[-1]) :
                print("\t!! perdu !!")
                print("le mot à deviner était : ", mot)
                break

# lancement du programme
lancer()

print("\n///\n")
