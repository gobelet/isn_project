from random import randint 

def initialisation(taille) : 
    lVoisins = [] 

    etatsCases = [[" " for _ in range (taille)] for _ in range (taille)] #permet de connaitre l'etat de chaque case : 'blanche' : " ", 'voisin' : "v", ou qui fait deja partie du laby : "." 
    etatsCases[0][0] = "." 

    mursVerticaux = [[1 for _ in range (taille)] for _ in range (taille)] 
    mursHorizontaux = [[1 for _ in range (taille)] for _ in range (taille)] 
    
    return lVoisins, etatsCases, mursVerticaux, mursHorizontaux 
                                    
def trouverVoisins(etatsCases, taille, caseX, caseY) : #quand une nouvelle case est ajoutée, cette fonction aujoute à la liste de voisins les voisins de cette case 
    global lVoisins

    if caseX+1 < taille and etatsCases[caseY][caseX + 1] == " " : 
        etatsCases[caseY][caseX + 1] = "v" 
        lVoisins.append([caseY, caseX + 1])

    if caseX-1 >= 0 and etatsCases[caseY][caseX - 1] == " " :
        etatsCases[caseY][caseX - 1] = "v"
        lVoisins.append([caseY, caseX - 1])

    if caseY+1 < taille and etatsCases[caseY + 1][caseX] == " " :
        etatsCases[caseY + 1][caseX] = "v"
        lVoisins.append([caseY + 1, caseX])

    if caseY-1 >= 0 and etatsCases[caseY - 1][caseX] == " " :
        etatsCases[caseY - 1][caseX] = "v"
        lVoisins.append([caseY - 1, caseX])

def voisinHasard() : #choisi au hasard une case 'voisin' qu'on va ajouter au laby
    global lVoisins

    voisin = randint(0, len(lVoisins)-1)
    y, x = lVoisins[voisin][0], lVoisins[voisin][1]
    del lVoisins[voisin]
    return y, x

def nbCheminVoisin(etatsCases, y, x) :
    totalVoisins = 0
    lTotalVoisins = []
    global taille

    if x < taille - 1 and etatsCases[y][x + 1] == "." :
        totalVoisins += 1
        lTotalVoisins.append([y, x + 1])
    if x > 0 and etatsCases[y][x - 1] == "." :
        totalVoisins += 1
        lTotalVoisins.append([y, x - 1])
    if y < taille - 1 and etatsCases[y + 1][x] == "." :
        totalVoisins += 1
        lTotalVoisins.append([y + 1, x])
    if y > 0 and etatsCases[y - 1][x] == "." :
        totalVoisins += 1
        lTotalVoisins.append([y - 1, x])

    return totalVoisins, lTotalVoisins

def chemin(y, x, lTotalVoisins, totalVoisins) : #choisi un voisin appartenant à chemin à "voisin" et retourne la direction à prendre pour aller de "v" à "." et donc construire le chemin
    if totalVoisins > 1 :
        nb = randint(0, totalVoisins-1)
    else :
        nb = 0
    if lTotalVoisins[nb][0] == y + 1 :
        direction = "S"
    elif lTotalVoisins[nb][0] == y - 1 :
        direction = "N"
    elif lTotalVoisins[nb][1] == x + 1 :
        direction = "E"
    elif lTotalVoisins[nb][1] == x - 1 :
        direction = "O"
    
    return direction

def enleverMur(direction, y, x) :
    global mursV
    global mursH
    
    if direction == "S" :
        mursH[y][x] = 0
    elif direction == "N" :
        mursH[y-1][x] = 0
    elif direction == "E" :
        mursV[y][x] = 0
    elif direction == "O" :
        mursV[y][x-1] = 0

def generer(taille, etatsCases) :
    global lVoisins
    global mursH
    global mursV
    trouverVoisins(etatsCases, taille, 0, 0)
    while len(lVoisins) != 0 :
        y, x = voisinHasard()
        etatsCases[y][x] = "."
        totVois, lTotVois = nbCheminVoisin(etatsCases, y, x)
        direction = chemin(y, x, lTotVois, totVois)
        enleverMur(direction, y, x)
        trouverVoisins(etatsCases, taille, x, y)

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

def fabriqueLaby(niveau):
	global taille
	global cote
	global lVoisins, etatsCases, mursV, mursH
	taille = niveauChoisi(niveau)
	cote = 600//taille
	lVoisins, etatsCases, mursV, mursH = initialisation(taille)
	etatsCases = generer(taille, etatsCases)
	return taille, cote, mursH, mursV

"""
partir de la case en haut à gauche
trouver ses voisins
prendre un voisin au pif
boum il devient chemin --> il faut enlever un mur
on reactualise les voisins
(si 2 cases du chemin adjacentes à 'voisin' : on en end une au îf, et du coup le chemin se fait entre ces deux cases)
"""
