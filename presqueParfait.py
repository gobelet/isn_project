from tkinter import *
from generer_laby import *
import time

# -----------------------Initialisation----------------------- #
fenetre = Tk()
page = 1
currentPage = 0
attraper = 0


def base():  # Interface Base
    global canvas
    canvas = Canvas(fenetre, width=640, height=640, background="LightSkyBlue1")


def presentation():
    global bloc
    bloc = canvas.create_rectangle(20, 20, 620, 620, fill="White")


# -----------------------Fonctions Dessin----------------------- #


def dessinCarteHaut(mursH):
    for i in range(taille):
        for j in range(taille):
            if mursH[i][j] == 1:
                refTopx = j * 50 + 20
                refTopy = (i+1) * 50 + 20
                murTop = canvas.create_rectangle(refTopx, refTopy,
                                                 refTopx+50, refTopy+1,
                                                 fill="Grey")
    murTop = canvas.create_rectangle(20, 20, 620, 20, fill="Grey")


def dessinCarteGauche(mursV):
    for i in range(taille):
        for j in range(taille):
            if mursV[i][j] == 1:
                refLeftx = (j + 1) * 50 + 20
                refLefty = i * 50 + 20
                murLeft = canvas.create_rectangle(refLeftx, refLefty,
                                                  refLeftx+1, refLefty+50,
                                                  fill="Grey")
    murLeft = canvas.create_rectangle(20, 20, 20, 620, fill="Grey")


# -----------------------Fonctions Evenementiels----------------------- #


def clavier(event):
    global page
    page = 2
    pageManagement(page)


def clickRegles(event):
    global page
    page = 6
    pageManagement(page)

def clickNiveaux(event):
    global page
    page = 7
    pageManagement(page)

def clickContinuer(event):
    global page
    page = 3
    pageManagement(page)

def clickUnpause(event):
    global page
    pausedPage

def pausedPage():
    global page


def deleteCanvas():
    canvas.delete(*canvas.find_all())


def move(event):
    global pos
    global page
    global attraper
    press = event.keysym
    de = 0
    if press == "space":
        page = 4
        pausedPage = thirdPage()
        pageManagement(page)
    elif press == "Up":
        de = 1
    elif press == "Down":
        de = 2
    elif press == "Left":
        de = 3
    elif press == "Right":
        de = 4
    avancer, direction = avance(pos, de)
    if avancer:
        pos = (pos[0]+direction[0], pos[1]+direction[1])
        canvas.coords(perso, pos[0], pos[1], pos[0]+40, pos[1]+40)   


# -----------------------Collisions----------------------- #


def avance(pos, de):
    x = (pos[0] - 25) // 50
    y = (pos[1] - 25) // 50
    avancer = True

    if de == 0 :
        return False, 0
    elif de == 1:
        direction = (0, -50)
        if y == 0 or mursH[y-1][x] == 1:
            avancer = False
    elif de == 2:
        direction = (0, 50)
        if y == taille-1 or mursH[y][x] == 1:
            avancer = False
    elif de == 3:
        direction = (-50, 0)
        if x == 0 or mursV[y][x-1] == 1:
            avancer = False
    elif de == 4:
        direction = (50, 0)
        if x == taille-1 or mursV[y][x] == 1:
            avancer = False

    return avancer, direction


def collisionPersonnage(pos, posNmi):
    global posCentreX
    global posCentreY
    posCentreX = pos[0] + 20
    posCentreY = pos[1] + 20
    posNmiCentreX = posNmi[0] + 20
    posNmiCentreY = posNmi[1] + 20
    separationX = abs(posCentreX-posNmiCentreX)
    separationY = abs(posCentreY-posNmiCentreY)
    if separationX < 20 and separationY < 20:
        return True
    
    


def collisionClef(posCentreX, posCentreY, posClef):
    posClefCentreX = posClef[0] + 20
    posClefCentreY = posClef[1] + 10
    separationX = abs(posCentreX-posClefCentreX)
    separationY = abs(posCentreY-posClefCentreY)
    if separationX < 25 and separationY < 15:
        return True
    


def collisionDoor(posCentreX, posCentreY, posDoor):
    posDoorCentreX = posDoor[0] + 13
    posDoorCentreY = posDoor[1] + 20
    separationX = abs(posCentreX-posDoorCentreX)
    separationY = abs(posCentreY-posDoorCentreY)
    if separationX < 13 and separationY < 20:
        return True


# -----------------------Ennemis----------------------- #


def ennemis():
    global posNmi
    de = randint(1, 4)
    distance = randint(1, 3)
    avancer, direction = avance(posNmi, de)
    if avancer:
        posNmi = (posNmi[0] + direction[0], posNmi[1] + direction[1])
        canvas.coords(Nmi, posNmi[0], posNmi[1], posNmi[0]+40, posNmi[1]+40)

    # PERDRE
    if collisionPersonnage(pos, posNmi):
        page = 8
        pageManagement(page)
    canvas.after(500, ennemis)

def gagner():
    global attraper
    if collisionClef(posCentreX, posCentreY, posClef) == True:
        attraper = 1
        canvas.delete(clef)
    if attraper == 1:
        if collisionDoor(posCentreX, posCentreY, posDoor) == True:
            page = 5
            pageManagement(page)
    canvas.after(15, gagner)


# -----------------------Pages----------------------- #


def pageManagement(page):
    deleteCanvas()
    presentation()
    if page == 1:
        firstPage()
    if page == 2:
        secondPage()
    if page == 3:
        thirdPage()
    if page == 4:
        fourthPage()
    if page == 5:
        fifthPage()
    if page == 6:
        sixthPage()
    if page == 7:
        seventhPage()
    if page == 8:
        eighthPage()


def firstPage():
    gameName = canvas.create_text(310, 250, text="Labyrinthe",
                                  font="Arial 50 italic", fill="Grey")
    ourNames = canvas.create_text(310, 330, text="Gwen & Mélo",
                                  font="Arial 30", fill="LightSkyBlue1")
    commande = canvas.create_text(310, 420,
                                  text="Appuyer sur 'Entrée' pour continuer ",
                                  font="Arial 16", fill="Grey")
    canvas.bind_all("<Return>", clavier)
    canvas.pack()


def secondPage():
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


def thirdPage():
    # Affichage du labyrinthe
    dessinCarteHaut(mursH)
    dessinCarteGauche(mursV)

    # Mouvement et affichage du bloc
    global page
    global perso
    global Nmi
    global posNmi
    global posClef
    global posDoor
    global pos
    global clef
    posNmi = (525, 425)
    Nmi = canvas.create_rectangle(525, 425, 565, 465, fill="Red")
    coordAleax = randint(0, 11)
    coordAleay = randint(0, 11)
    coordClefx = (coordAleax * 50) + 23
    coordClefy = (coordAleay * 50) + 23
    posClef = (coordClefx, coordClefy)
    clef = canvas.create_rectangle(coordClefx, coordClefy,
                                   coordClefx + 40, coordClefy + 20,
                                   fill="Gold")
    posDoor = (580, 575)
    door = canvas.create_rectangle(580, 575, 606, 615, fill="Brown")
    pos = (25, 25)
    perso = canvas.create_rectangle(25, 25, 65, 65, fill="DeepSkyBlue2")
    ennemis()
    gagner()
    canvas.focus_set()
    canvas.bind_all("<Key>", move)
    canvas.pack()


def fourthPage():
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


def fifthPage():
    felicitations = canvas.create_text(320, 250, text="Félicitations ! ",
                                       font="Arial 50 italic",
                                       fill="DeepSkyBlue2")
    message = canvas.create_text(320, 400, text="Vous Avez Gagné",
                                 font="Arial 50 italic", fill="Grey")
    canvas.pack()


def sixthPage():  # Règles
    header = canvas.create_text(300, 100, text="Règles",
                                font="system 70 bold", fill="Grey")
    but = canvas.create_text(100, 150, text="But du jeu:",
                             font="Arial 20 underline", fill="LightSkyBlue1")
    firstPoint = canvas.create_text(320, 190,
                                    text="* Partir de la case en haut à droite \
                                    et arriver à la case",
                                    font="Arial 18", fill="LightGrey")
    endFirstPoint = canvas.create_text(137, 220, text="en bas à gauche.",
                                       font="Arial 18", fill="LightGrey")
    secondPoint = canvas.create_text(263, 250,
                                     text="* Récupérer des clés pour ouvrir \
                                     les portes.",
                                     font="Arial 18", fill="LightGrey")
    comment = canvas.create_text(128, 290, text="Comment jouer:",
                                 font="Arial 20 underline",
                                 fill="LightSkyBlue1")
    thirdPoint = canvas.create_text(290, 330,
                                    text="* Utiliser les flèches du clavier \
                                    pour se déplacer. ",
                                    font="Arial 18", fill="LightGrey")
    contraintes = canvas.create_text(107, 370, text="Contraintes:",
                                     font="Arial 20 underline",
                                     fill="LightSkyBlue1")
    fourthPoint = canvas.create_text(305, 410,
                                     text="* Eviter les ennemis, les toucher \
                                     fait perdre une vie.",
                                     font="Arial 18", fill="LightGrey")
    fifthPoint = canvas.create_text(127, 440, text="* Vous avez 3 vies.",
                                    font="Arial 18", fill="LightGrey")
    finalPoint = canvas.create_text(310, 500,
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


def seventhPage():  # choix niveaux
    blocNiveaux1 = canvas.create_rectangle(230, 540, 400, 590,
                                           fill="DeepSkyBlue2")
    niveaux1 = canvas.create_text(310, 565, text="Niveau 1",
                                  font="Arial 20", fill="LightGrey")
    blocCommencer = canvas.create_rectangle(230, 540, 400, 590,
                                            fill="DeepSkyBlue2")
    commencer = canvas.create_text(315, 565, text="Commencer",
                                   font="Arial 20", fill="LightGrey")
    canvas.tag_bind(blocCommencer, "<ButtonPress-1>", clickContinuer)
    canvas.tag_bind(commencer, "<ButtonPress-1>", clickContinuer)
    canvas.pack()


def eighthPage():
    niveaux1 = canvas.create_text(310, 565, text="PERDU !",
                                  font="Arial 80", fill="LightGrey")


# ----------------------Boucle principale----------------------- #

"""
def update():
    global currentPage
    if page != currentPage:
        pageManagement(page)
        currentPage = page
    canvas.after(20, update)
"""

base()
pageManagement(page)
"""update()"""
fenetre.mainloop()
