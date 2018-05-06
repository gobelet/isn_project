from tkinter import *
from generer_laby import *
import generer_laby

# -----------------------Initialisation----------------------- #


fenetre = Tk()
page = 1


# Base de l'interface
def base():
    global canvas
    canvas = Canvas(fenetre, width=640, height=640, background="LightSkyBlue1")
    presentation()
    pageManagement(page)
    canvas.mainloop()


# Crée le fond blanc de l'interface
def presentation():
    fond = canvas.create_rectangle(20, 20, 620, 620, fill="White")


# -----------------------Pages----------------------- #


# Permet de changer de page
def pageManagement(page):
    deleteCanvas()
    presentation()

    if page == 1:
        pageUne()
    if page == 2:
        pageDeux()
    if page == 3:
        pageTrois()
    if page == 4:
        pageQuatre()
    if page == 5:
        pageCinq()
    if page == 6:
        pageSix()
    if page == 7:
        pageSept()
    if page == 8:
        pageHuit()


# Page de présentation
def pageUne():
    nomJeu = canvas.create_text(310, 250, text="Labyrinthe",
                                font="Arial 50 italic", fill="Grey")
    nosNoms = canvas.create_text(310, 330, text="Gwen & Mélo",
                                 font="Arial 30", fill="LightSkyBlue1")
    commande = canvas.create_text(310, 420,
                                  text="Appuyer sur 'Entrée' pour continuer ",
                                  font="Arial 16", fill="Grey")
    canvas.bind_all("<Return>", clavier)
    canvas.pack()


# Page permettant d'accéder aux règles et aux niveaux
def pageDeux():
    global attraper
    attraper = 0
    blocRegles = canvas.create_rectangle(230, 235, 400, 285,
                                         fill="DeepSkyBlue2")
    blocNiveaux = canvas.create_rectangle(230, 315, 400, 365,
                                          fill="DeepSkyBlue2")
    regles = canvas.create_text(310, 260, text="Règles",
                                font="Arial 20", fill="Grey")
    niveaux = canvas.create_text(310, 340, text="Niveaux",
                                 font="Arial 20", fill="Grey")

    canvas.tag_bind(blocRegles, "<ButtonPress-1>", clickRegles)
    canvas.tag_bind(regles, "<ButtonPress-1>", clickRegles)
    canvas.tag_bind(blocNiveaux, "<ButtonPress-1>", clickNiveaux)
    canvas.tag_bind(niveaux, "<ButtonPress-1>", clickNiveaux)

    canvas.pack()


# Règles
def pageTrois():
    header = canvas.create_text(320, 75, text="Règles",
                                font="system 70 bold", fill="Grey")

    but = canvas.create_text(100, 150, text="But du jeu:",
                             font="Arial 20 underline", fill="LightSkyBlue1")
    point1 = canvas.create_text(230, 190,
                                text="* Aller jusqu'à la porte en bas à \
droite.",
                                font="Arial 18", fill="LightGrey")
    point2 = canvas.create_text(263, 220,
                                text="* Récupérer la(-es) clé(s) pour \
ouvrir la porte",
                                font="Arial 18", fill="LightGrey")
    presentationPerso = canvas.create_text(297, 250,
                                           text="* Perso =          Ennemi =  \
        Clé =          Porte =",
                                           font="Arial 18", fill="LightGrey")

    perso = canvas.create_rectangle(130, 235, 160, 265, fill="DeepSkyBlue2")
    ennemi = canvas.create_rectangle(310, 235, 340, 265, fill="Red")
    clef = canvas.create_rectangle(440, 245, 480, 260, fill="Gold")
    porte = canvas.create_rectangle(580, 235, 605, 275, fill="Brown")

    comment = canvas.create_text(128, 290, text="Comment jouer:",
                                 font="Arial 20 underline",
                                 fill="LightSkyBlue1")
    point3 = canvas.create_text(255, 330,
                                text="* Se déplacer grâce aux flèches du \
 clavier ",
                                font="Arial 18", fill="LightGrey")
    autres = canvas.create_text(75, 370, text="Autres:",
                                font="Arial 20 underline",
                                fill="LightSkyBlue1")
    point4 = canvas.create_text(161, 410,
                                text="* Il faut éviter les ennemis",
                                font="Arial 18", fill="LightGrey")
    point5 = canvas.create_text(318, 440,
                                text="* À tout moment appuyer sur entrée \
pour recommencer",
                                font="Arial 18", fill="LightGrey")
    point6 = canvas.create_text(310, 500,
                                text="Choisir niveau pour commencer le \
 jeu !",
                                font="Arial 20", fill="Grey")
    blocNiveaux = canvas.create_rectangle(230, 540, 400, 590,
                                          fill="DeepSkyBlue2")
    niveaux = canvas.create_text(310, 565, text="Niveaux",
                                 font="Arial 20", fill="LightGrey")

    canvas.tag_bind(blocNiveaux, "<ButtonPress-1>", clickNiveaux)
    canvas.tag_bind(niveaux, "<ButtonPress-1>", clickNiveaux)
    canvas.pack()


# Choix des niveaux
def pageQuatre():
    global blocNiveau1
    global blocNiveau2
    global blocNiveau3
    global blocNiveau4

    choix = canvas.create_text(310, 120,
                               text="Choisir un niveau pour commencer le \
 jeu !",
                               font="Arial 20", fill="Grey")

    blocNiveau1 = canvas.create_rectangle(120, 200, 290, 250,
                                          fill="DeepSkyBlue2")
    afficher1 = canvas.create_text(205, 225, text="Niveau 1",
                                   font="Arial 20", fill="LightGrey")
    canvas.tag_bind(blocNiveau1, "<ButtonPress-1>", niveau1)
    canvas.tag_bind(afficher1, "<ButtonPress-1>", niveau1)

    blocNiveau2 = canvas.create_rectangle(340, 200, 510, 250,
                                          fill="DeepSkyBlue2")
    afficher2 = canvas.create_text(425, 225, text="Niveau 2",
                                   font="Arial 20", fill="LightGrey")
    canvas.tag_bind(blocNiveau2, "<ButtonPress-1>", niveau2)
    canvas.tag_bind(afficher2, "<ButtonPress-1>", niveau2)
    blocNiveau3 = canvas.create_rectangle(120, 280, 290, 330,
                                          fill="DeepSkyBlue2")
    afficher3 = canvas.create_text(205, 305, text="Niveau 3",
                                   font="Arial 20", fill="LightGrey")
    canvas.tag_bind(blocNiveau3, "<ButtonPress-1>", niveau3)
    canvas.tag_bind(afficher3, "<ButtonPress-1>", niveau3)
    blocNiveau4 = canvas.create_rectangle(340, 280, 510, 330,
                                          fill="DeepSkyBlue2")
    afficher4 = canvas.create_text(425, 305, text="Niveau 4",
                                   font="Arial 20", fill="LightGrey")
    canvas.tag_bind(blocNiveau4, "<ButtonPress-1>", niveau4)
    canvas.tag_bind(afficher4, "<ButtonPress-1>", niveau4)
    blocCommencer = canvas.create_rectangle(230, 540, 400, 590,
                                            fill="DeepSkyBlue2")
    commencer = canvas.create_text(315, 565, text="Commencer",
                                   font="Arial 20", fill="LightGrey")

    canvas.tag_bind(blocCommencer, "<ButtonPress-1>", clickContinuer)
    canvas.tag_bind(commencer, "<ButtonPress-1>", clickContinuer)
    canvas.pack()


# Page de pause; inutilisée ici
def pageCinq():
    blocContinuer = canvas.create_rectangle(230, 235, 400, 280,
                                            fill="DeepSkyBlue2")
    blocRecommencer = canvas.create_rectangle(230, 315, 400, 365,
                                              fill="DeepSkyBlue2")
    continuer = canvas.create_text(310, 260, text="Continuer",
                                   font="Arial 19", fill="Grey")
    recommencer = canvas.create_text(314, 340, text="Recommencer",
                                     font="Arial 19", fill="Grey")
    canvas.tag_bind(blocContinuer, "<ButtonPress-1>", clickContinuer)
    canvas.tag_bind(continuer, "<ButtonPress-1>", clickContinuer)
    canvas.tag_bind(blocRecommencer, "<ButtonPress-1>", clickNiveaux)
    canvas.tag_bind(recommencer, "<ButtonPress-1>", clickNiveaux)
    canvas.pack()


# Jeu en lui-même
def pageSix():
    # Affichage du labyrinthe
    dessineMursH(mursH)
    dessineMursV(mursV)

    # Mouvement et affichage du bloc
    global perso
    global Nmis
    global clefs
    global posPerso
    global posNmi
    global posClef
    global posPorte

    posPerso = (25, 25)
    perso = canvas.create_rectangle(25, 25, cote+15, cote+15,
                                    fill="DeepSkyBlue2")

    Nmis = []
    posNmi = []
    for n in range(niveau):
        NmiAlea = (randint(taille*n//niveau+2, taille*(n+1)//niveau-1),
                   randint(0, taille-1))
        posNmi.append([NmiAlea[0]*cote+25, NmiAlea[1]*cote+25])
        Nmis.append(canvas.create_rectangle(posNmi[n][0], posNmi[n][1],
                                            posNmi[n][0]+cote-10,
                                            posNmi[n][1]+cote-10,
                                            fill="Red"))
        ennemis(n)

    posClef = []
    clefs = []
    for n in range(niveau):
        clefAlea = (randint(0, taille-1),
                    randint(taille*n//niveau+2, taille*(n+1)//niveau-1))
        posClef.append([clefAlea[0]*cote+25, clefAlea[1]*cote+25])
        clefs.append(canvas.create_rectangle(posClef[n][0], posClef[n][1],
                                             posClef[n][0] + cote-10,
                                             posClef[n][1] + cote//3,
                                             fill="Gold"))

    posPorte = ((taille-1)*cote+30, (taille-1)*cote+24)
    porte = canvas.create_rectangle(posPorte[0], posPorte[1],
                                    posPorte[0]+cote//2, posPorte[1]+4*cote//5,
                                    fill="Brown")

    canvas.focus_set()
    canvas.bind_all("<Key>", move)
    canvas.pack()


# Page de fin en cas de victoire
def pageSept():
    felicitations = canvas.create_text(320, 250, text="Félicitations ! ",
                                       font="Arial 50 italic",
                                       fill="DeepSkyBlue2")
    message = canvas.create_text(320, 400, text="Vous Avez Gagné",
                                 font="Arial 50 italic", fill="Grey")
    commande = canvas.create_text(310, 580,
                                  text="Appuyer sur 'Entrée' pour recommencer",
                                  font="Arial 20", fill="Cyan2")
    canvas.pack()


# Page de fin en cas de défaite
def pageHuit():
    perdu = canvas.create_text(310, 310, text="PERDU !",
                               font="Arial 80", fill="LightGrey")
    commande = canvas.create_text(310, 580,
                                  text="Appuyer sur 'Entrée' pour recommencer",
                                  font="Arial 20", fill="Cyan2")


# -----------------------Fonctions Dessin----------------------- #


# Affiche les murs horizontaux
def dessineMursH(mursH):
    for i in range(taille):
        for j in range(taille):
            if mursH[i][j] == 1:
                x = j * cote + 20
                y = (i+1) * cote + 20
                mur = canvas.create_rectangle(x, y, x+cote, y+1, fill="Grey")
    bord = canvas.create_rectangle(20, 20, 620, 20, fill="Grey")


# Affiche les murs verticaux
def dessineMursV(mursV):
    for i in range(taille):
        for j in range(taille):
            if mursV[i][j] == 1:
                x = (j + 1) * cote + 20
                y = i * cote + 20
                mur = canvas.create_rectangle(x, y, x+1, y+cote, fill="Grey")
    bord = canvas.create_rectangle(20, 20, 20, 620, fill="Grey")


# -----------------------Fonctions Evenementiels----------------------- #


# Les fonctions suivantes appellent pageMangament() pour changer de page
def clavier(event):
    pageManagement(2)


def clickRegles(event):
    pageManagement(3)


def clickNiveaux(event):
    pageManagement(4)


def clickContinuer(event):
    pageManagement(6)


# Cette fonction efface tout ce qu'il y a sur la page avant de changer de page
def deleteCanvas():
    canvas.delete(*canvas.find_all())


# Les focntions suivantes sont liées au choix du niveau
def auNiveau(n):
    global niveau, taille, cote, mursH, mursV
    niveau = n
    taille, cote, mursH, mursV = fabriqueLaby(n)


def niveau1(event):
    canvas.itemconfig(blocNiveau1, fill='cyan2')
    canvas.itemconfig(blocNiveau2, fill='DeepSkyBlue2')
    canvas.itemconfig(blocNiveau3, fill='DeepSkyBlue2')
    canvas.itemconfig(blocNiveau4, fill='DeepSkyBlue2')
    auNiveau(1)


def niveau2(event):
    canvas.itemconfig(blocNiveau1, fill='DeepSkyBlue2')
    canvas.itemconfig(blocNiveau2, fill='cyan2')
    canvas.itemconfig(blocNiveau3, fill='DeepSkyBlue2')
    canvas.itemconfig(blocNiveau4, fill='DeepSkyBlue2')
    auNiveau(2)


def niveau3(event):
    canvas.itemconfig(blocNiveau1, fill='DeepSkyBlue2')
    canvas.itemconfig(blocNiveau2, fill='DeepSkyBlue2')
    canvas.itemconfig(blocNiveau3, fill='cyan2')
    canvas.itemconfig(blocNiveau4, fill='DeepSkyBlue2')
    auNiveau(3)


def niveau4(event):
    canvas.itemconfig(blocNiveau1, fill='DeepSkyBlue2')
    canvas.itemconfig(blocNiveau2, fill='DeepSkyBlue2')
    canvas.itemconfig(blocNiveau3, fill='DeepSkyBlue2')
    canvas.itemconfig(blocNiveau4, fill='cyan2')
    auNiveau(4)


# -----------------------Personnages----------------------- #


# Gère les mouvements du personnage
def move(event):
    global posPerso
    global posNmi
    global attraper
    press = event.keysym
    de = 0

    if press == "space":
        pausedPage = pageCinq()
        pageManagement(6)
    elif press == "Up":
        de = 1
    elif press == "Down":
        de = 2
    elif press == "Left":
        de = 3
    elif press == "Right":
        de = 4

    avancer, direction = collisionMurs(posPerso, de)

    if avancer:
        posPerso = (posPerso[0]+direction[0], posPerso[1]+direction[1])
        canvas.coords(perso, posPerso[0], posPerso[1],
                      posPerso[0]+cote-10, posPerso[1]+cote-10)
        for n in range(niveau):
            perdre(posNmi[n], posPerso)
        for n in range(niveau):
            gagner(posPerso, posClef[n], clefs[n], taille)


# Gère les défaites (= collision entre ennemi et personnage)
def perdre(posNmi, pos):
    if collisionObjet(pos, posNmi):
        pageManagement(8)


# Gère les victoires (= personnage arrivé en bas à droite du labyrinthe)
def gagner(pos, posClef, clef, taille):
    global attraper

    if collisionObjet(pos, posClef):
        attraper += 1
        canvas.delete(clef)

    if attraper == niveau:
        if collisionObjet(pos, ((taille-1)*cote+25, (taille-1)*cote+25)):
            pageManagement(7)


# -----------------------Ennemis----------------------- #


# Gère les mouvements du(des) ennemi(s)
def ennemis(n):
    global posNmi
    global posPerso
    de = randint(1, 4)
    avancer, direction = collisionMurs(posNmi[n], de)

    if avancer:
        posNmi[n] = (posNmi[n][0] + direction[0], posNmi[n][1] + direction[1])
        canvas.coords(Nmis[n], posNmi[n][0], posNmi[n][1],
                      posNmi[n][0]+cote-10, posNmi[n][1]+cote-10)
        perdre(posNmi[n], posPerso)

    canvas.after(500, ennemis, n)


# -----------------------Collisions----------------------- #


# Détecte les collisions entre les murs et le personnage
def collisionMurs(pos, de):
    x = (pos[0] - 25) // cote
    y = (pos[1] - 25) // cote
    avancer = True

    if de == 0:
        return False, 0
    elif de == 1:
        direction = (0, -cote)
        if y == 0 or mursH[y-1][x] == 1:
            avancer = False
    elif de == 2:
        direction = (0, cote)
        if y == taille-1 or mursH[y][x] == 1:
            avancer = False
    elif de == 3:
        direction = (-cote, 0)
        if x == 0 or mursV[y][x-1] == 1:
            avancer = False
    elif de == 4:
        direction = (cote, 0)
        if x == taille-1 or mursV[y][x] == 1:
            avancer = False
    return avancer, direction


# Détecte les collisions entre le personnage et un autre objet
def collisionObjet(posPerso, posObjet):
    persoX = (posPerso[0] - 25) // cote
    persoY = (posPerso[1] - 25) // cote
    objetX = (posObjet[0] - 25) // cote
    objetY = (posObjet[1] - 25) // cote

    if persoX == objetX and persoY == objetY:
        return True


# ----------------------Boucle principale----------------------- #
base()
