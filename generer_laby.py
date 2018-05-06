from random import randint


def initialisation(taille):
    lVoisins = []

# Permet de connaitre l'etat de chaque case : 'blanche' : " ", 'voisin' : "v",
# ou qui fait deja partie du labyrinthe : "."
    etatsCases = [[" " for _ in range(taille)] for _ in range(taille)]
    etatsCases[0][0] = "."

# Au début, toutes les cases sont entourées de murs. On en enlève au fur et à
# mesure
    mursVerticaux = [[1 for _ in range(taille)] for _ in range(taille)]
    mursHorizontaux = [[1 for _ in range(taille)] for _ in range(taille)]

    return lVoisins, etatsCases, mursVerticaux, mursHorizontaux


# Quand une nouvelle case est ajoutée au labyrinthe,
# cette fonction ajoute à la liste de voisins les voisins de cette case
def trouverVoisins(etatsCases, taille, caseX, caseY):
    global lVoisins

    if caseX+1 < taille and etatsCases[caseY][caseX + 1] == " ":
        etatsCases[caseY][caseX + 1] = "v"
        lVoisins.append([caseY, caseX + 1])

    if caseX-1 >= 0 and etatsCases[caseY][caseX - 1] == " ":
        etatsCases[caseY][caseX - 1] = "v"
        lVoisins.append([caseY, caseX - 1])

    if caseY+1 < taille and etatsCases[caseY + 1][caseX] == " ":
        etatsCases[caseY + 1][caseX] = "v"
        lVoisins.append([caseY + 1, caseX])

    if caseY-1 >= 0 and etatsCases[caseY - 1][caseX] == " ":
        etatsCases[caseY - 1][caseX] = "v"
        lVoisins.append([caseY - 1, caseX])


# Choisit au hasard une case 'voisin' et l'ajoute au labyrinthe
def voisinHasard():
    global lVoisins

    voisin = randint(0, len(lVoisins)-1)
    y, x = lVoisins[voisin][0], lVoisins[voisin][1]
    del lVoisins[voisin]
    return y, x


# Permet de trouver, à partir d'une case donnée, les cases voisines à cette
# dernière qui appartiennent déjà au labyrinthe
def nbCheminVoisin(etatsCases, y, x):
    totalVoisins = 0
    lTotalVoisins = []
    global taille

    if x < taille - 1 and etatsCases[y][x + 1] == ".":
        totalVoisins += 1
        lTotalVoisins.append([y, x + 1])
    if x > 0 and etatsCases[y][x - 1] == ".":
        totalVoisins += 1
        lTotalVoisins.append([y, x - 1])
    if y < taille - 1 and etatsCases[y + 1][x] == ".":
        totalVoisins += 1
        lTotalVoisins.append([y + 1, x])
    if y > 0 and etatsCases[y - 1][x] == ".":
        totalVoisins += 1
        lTotalVoisins.append([y - 1, x])

    return totalVoisins, lTotalVoisins


# Choisit une case appartenant déjà au labyrinthe et qui est voisine à la case
# sélectionnée et enlève le mur entre les deux
def Creerchemin(y, x, lTotalVoisins, totalVoisins):
    global mursV
    global mursH

    if totalVoisins > 1:
        nb = randint(0, totalVoisins-1)
    else:
        nb = 0
    if lTotalVoisins[nb][0] == y + 1:
        mursH[y][x] = 0
    elif lTotalVoisins[nb][0] == y - 1:
        mursH[y-1][x] = 0
    elif lTotalVoisins[nb][1] == x + 1:
        mursV[y][x] = 0
    elif lTotalVoisins[nb][1] == x - 1:
        mursV[y][x-1] = 0


# Fonction principale qui génère le labyrinthe
def generer(taille, etatsCases):
    global lVoisins
    global mursH
    global mursV
    trouverVoisins(etatsCases, taille, 0, 0)
    while len(lVoisins) != 0:
        y, x = voisinHasard()
        etatsCases[y][x] = "."
        totVois, lTotVois = nbCheminVoisin(etatsCases, y, x)
        Creerchemin(y, x, lTotVois, totVois)
        trouverVoisins(etatsCases, taille, x, y)


# Choisit la taille du labyrinthe en fonction du niveau sélectionné par
# l'utilisateur
def niveauChoisi(niveau):
    if niveau == 1:
        taille = 15
    if niveau == 2:
        taille = 20
    if niveau == 3:
        taille = 25
    if niveau == 4:
        taille = 30
    return taille


# Fait tourner les fonctions et retourne les données nécessaires pour le jeu
def fabriqueLaby(niveau):
    global taille, cote
    global lVoisins, etatsCases, mursV, mursH

    taille = niveauChoisi(niveau)
    cote = 600//taille
    lVoisins, etatsCases, mursV, mursH = initialisation(taille)
    etatsCases = generer(taille, etatsCases)
    return taille, cote, mursH, mursV
