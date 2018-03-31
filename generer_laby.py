from random import randint

lVoisins = [[0, 1][1, 0]]

def initialiser(taille) :
    etatsCases = [[[" "] for _ in range (taille)] for _ in range (taille)] #permet de connaitre l'etat de chaque case : 'blanche' : " ", 'voisin' : "v", ou qui fait deja partie du laby : "."
    etatsCases[0][0] = "."
    etatsCases[0][1], etatsCases[1][0] = "v", "v"

def trouverVoisins(etatsCases, caseX, caseY) :
    global lVoisins
    if etatsCases[caseY][caseX + 1] == " " :
        etatsCases[caseY][caseX + 1] = "v"
        lVoisins.append([caseY, caseX + 1])

    if etatsCases[caseY][caseX - 1] == " " :
        etatsCases[caseY][caseX - 1] = "v"
        lVoisins.append([caseY, caseX - 1])

    if etatsCases[caseY + 1][caseX] == " " :
        etatsCases[caseY + 1][caseX] = "v"
        lVoisins.append([caseY + 1, caseX])
    
    if etatsCases[caseY][caseX + 1] == " " :
        etatsCases[caseY][caseX + 1] = "v"
        lVoisins.append([caseY, caseX + 1])

def voisinHasard(lVoisins) :
    voisin = randint(0, len(lVoisins)-1)
    return lVoisins[voisin][0], lVoisins[voisin][1]

def generer(taille) :


while len(lVoisins) != 0 :
partir de la case en haut à gauche
trouver ses voisins
prendre un voisin au pif
boum il devient chemin --> il faut enlever un mur
on réactualise les voisins
(si une case voisin est adjacente à 2 ou plus cases du chemin/laby : on en prend une au pif, et du coup le chemin se fait entre ces 2 cases)
quand y a plus de cases voisin ou de case qui fait pas partie du chemin : c est fini!!!

