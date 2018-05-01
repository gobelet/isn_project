from tkinter import *
from generer_laby import *
import time

#-------------------------------Initialisation--------------------------------#
fenetre = Tk()
page = 1
currentPage = 0
#Interface Base
def base():
    global canvas
    canvas = Canvas(fenetre, width = 640, height = 640, background= 'LightSkyBlue1')
def presentation():
    global bloc
    bloc = canvas.create_rectangle(20, 20, 620, 620, fill = 'White')


#-----------------------------Fonctions Dessin--------------------------#
def dessinCarteHaut (mursH):
    for i in range (taille):
         for j in range (taille):
            if mursH[i][j] == 1:
                refTopx = j * 50 + 20
                refTopy = (i+1) * 50 + 20
                murTop = canvas.create_rectangle(refTopx , refTopy, refTopx + 50 , refTopy + 1, fill = 'Grey')
    murTop = canvas.create_rectangle(20, 20, 620, 20, fill = 'Grey')
def dessinCarteGauche (mursV) :
    for i in range (taille):
        for j in range (taille):
            if mursV[i][j] == 1:
                refLeftx = (j+1) * 50 + 20
                refLefty = i * 50 + 20
                murLeft = canvas.create_rectangle(refLeftx , refLefty, refLeftx + 1 , refLefty + 50, fill = 'Grey')
    murLeft = canvas.create_rectangle(20, 20, 20, 620, fill = 'Grey')
  
#-----------------------------Fonctions Evenementiels--------------------------#
def clavier(event):
    global page
    page = 2  
def clickRegles(event):
    global page
    page = 6
def clickNiveaux(event):
    global page
    page = 7
def clickContinuer(event):
    global page
    page = 3
def clickUnpause(event):
    global page
    pausedPage
def deleteCanvas():
    canvas.delete(*canvas.find_all())
def move(event):
    global pos
    global page
    press = event.keysym
    if press == "Up":
        pos = (pos[0], pos[1] - 10)
        if collisionMurs(pos) == True:
            pos = (pos[0], pos[1] + 10)
    elif press == "Down":
        pos = (pos[0], pos[1] + 10)
        if collisionMurs(pos) == True:
            pos = (pos[0], pos[1] - 10)
    elif press == "Right":
        pos = (pos[0] + 10, pos[1])
        if collisionMurs(pos) == True:
            pos = (pos[0] - 10, pos[1])
    elif press == "Left":
        pos = (pos[0] - 10, pos[1])
        if collisionMurs(pos) == True:
            pos = (pos[0] + 10, pos[1])
    elif press == "space":
        page = 4
        pausedPage = thirdPage()
    #collisionMurs(perso)
    canvas.coords(perso, pos[0], pos[1], pos[0]+40, pos[1]+40)

#----------------------------------Collisions---------------------------------#
def collisionMurs (pos):
    global overlap
    overlap = canvas.find_overlapping(pos[0], pos[1], pos[0] + 40, pos[1] + 40)
    if len(overlap) >= 3:
        print(overlap)
        return True
    else:
        return False
        
#-----------------------------Ennemis------------------------------------------#
def ennemis():
    global posNmi
    de = randint(1, 4)
    distance = randint(1, 3)
    x = (posNmi[0]-25)//50
    y = (posNmi[1]-25)//50
    avancer = True

    if de == 1:
        direction = (0, -50)
        if y == 0 or mursH[y-1][x] == 1:
            avancer = False
    if de == 2:
        direction = (0, 50)
        if y == taille-1 or mursH[y][x] == 1:
            avancer = False
    if de == 3:
        direction = (50, 0)
        if x == taille-1 or mursV[y][x] == 1:
            avancer = False
    if de == 4:
        direction = (-50, 0)
        if x == 0 or mursV[y][x-1] == 1:
            avancer = False

    if avancer:
        posNmi = (posNmi[0] + direction[0], posNmi[1] + direction[1])
        canvas.coords(Nmi, posNmi[0], posNmi[1], posNmi[0]+40, posNmi[1]+40)
    canvas.after(500, ennemis)

        

#-------------------------------------Pages-----------------------------------#
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
        
def firstPage():
    gameName = canvas.create_text(310, 250, text = "Labyrinthe", font = "Arial 50 italic", fill = "Grey")
    ourNames = canvas.create_text(310, 330 , text = "Gwen & Mélo", font = "Arial 30", fill = "LightSkyBlue1")
    commande = canvas.create_text(310, 420 , text = "Appuyer sur 'Entrée' pour continuer ", font = "Arial 16", fill = "Grey")
    canvas.bind_all("<Return>", clavier)
    canvas.pack()
def secondPage():
    blocRegles = canvas.create_rectangle(230, 235, 400, 285, fill = 'DeepSkyBlue2')
    blocNiveaux = canvas.create_rectangle(230, 315, 400, 365, fill = 'DeepSkyBlue2')
    regles = canvas.create_text(310, 260, text = "Règles", font = "Arial 20", fill = "Grey")
    niveaux = canvas.create_text(310, 340 , text = "Niveaux", font = "Arial 20", fill = "Grey")
    canvas.tag_bind(blocRegles,'<ButtonPress-1>', clickRegles)
    canvas.tag_bind(regles,'<ButtonPress-1>', clickRegles)
    canvas.tag_bind(blocNiveaux,'<ButtonPress-1>', clickNiveaux)
    canvas.tag_bind(niveaux,'<ButtonPress-1>', clickNiveaux)
    canvas.pack()
def thirdPage():
#Affichage du labyrinthe
    dessinCarteHaut(mursH)
    dessinCarteGauche(mursV)
#Mouvement et affichage du bloc
    global perso
    global Nmi
    global posNmi
    global pos
    posNmi = (525, 425)
    Nmi = canvas.create_rectangle(525, 425, 565, 465, fill = 'Red')
    coordAleax = randint(0, 11)
    coordAleay = randint(0, 11)
    coordClefx = (coordAleax * 50) + 23
    coordClefy = (coordAleay * 50) + 23
    clef = canvas.create_rectangle(coordClefx , coordClefy , coordClefx + 40, coordClefy + 20, fill = 'Gold')
    door = canvas.create_rectangle(580, 575, 605, 615, fill = 'Brown')
    pos = (25, 25)
    perso = canvas.create_rectangle(25, 25, 65, 65, fill = 'DeepSkyBlue2')
    ennemis()
    canvas.focus_set()
    canvas.bind_all("<Key>", move)
    canvas.pack()
def fourthPage():
    blocContinuer = canvas.create_rectangle(230, 235, 400, 280, fill = 'DeepSkyBlue2')
    blocRecommencer = canvas.create_rectangle(230, 315, 400, 365, fill = 'DeepSkyBlue2')
    continuer = canvas.create_text(310, 260, text = "Continuer", font = "Arial 19", fill = "Grey")
    recommencer = canvas.create_text(314, 340 , text = "Recommencer", font = "Arial 19", fill = "Grey")
    canvas.tag_bind(blocContinuer,'<ButtonPress-1>', clickContinuer)
    canvas.tag_bind(continuer,'<ButtonPress-1>', clickContinuer)
    canvas.tag_bind(blocRecommencer,'<ButtonPress-1>', clickNiveaux)
    canvas.tag_bind(recommencer,'<ButtonPress-1>', clickNiveaux)
    canvas.pack()
def fifthPage():
    felicitations = canvas.create_text(320, 250, text = "Felicitations ! ", font = "Arial 50 italic", fill = "DeepSkyBlue2")
    message = canvas.create_text(320, 400, text = "Vous Avez Gagné", font = "Arial 50 italic", fill = "Grey")        
    canvas.pack()
def sixthPage():#Règles
    header = canvas.create_text(300, 100, text = "Règles", font = "system 70 bold", fill = "Grey")
    but = canvas.create_text(100, 150, text = "But du jeu:", font = "Arial 20 underline", fill = "LightSkyBlue1")
    firstPoint = canvas.create_text(320, 190, text = "* Partir de la case en haut à droite et arriver à la case " , font = "Arial 18", fill = "LightGrey")
    endFirstPoint = canvas.create_text(137, 220, text = "en bas à gauche.", font = "Arial 18", fill = "LightGrey")
    secondPoint = canvas.create_text(263, 250, text = "* Récupérer des clés pour ouvrir les portes.", font = "Arial 18", fill = "LightGrey")
    comment = canvas.create_text(128, 290, text = "Comment jouer:", font = "Arial 20 underline", fill = "LightSkyBlue1")
    thirdPoint = canvas.create_text(290, 330, text = "* Utiliser les flèches du clavier pour se déplacer. " , font = "Arial 18", fill = "LightGrey")
    contraintes = canvas.create_text(107, 370, text = "Contraintes:", font = "Arial 20 underline", fill = "LightSkyBlue1")
    fourthPoint = canvas.create_text(305, 410, text = "* Eviter les ennemis, les toucher fait perdre une vie." , font = "Arial 18", fill = "LightGrey")
    fifthPoint = canvas.create_text(127, 440, text = "* Vous avez 3 vies." , font = "Arial 18", fill = "LightGrey")
    finalPoint = canvas.create_text(310, 500, text = "Choisir niveau pour commencer le jeu !", font = "Arial 20", fill = "Grey")
    blocNiveaux = canvas.create_rectangle(230, 540, 400, 590, fill = 'DeepSkyBlue2')
    niveaux = canvas.create_text(310, 565 , text = "Niveaux", font = "Arial 20", fill = "LightGrey")
    canvas.tag_bind(blocNiveaux,'<ButtonPress-1>', clickNiveaux)
    canvas.tag_bind(niveaux,'<ButtonPress-1>', clickNiveaux)
    canvas.pack()
    
def seventhPage():#chx niveaux
    blocNiveaux1 = canvas.create_rectangle(230, 540, 400, 590, fill = 'DeepSkyBlue2')
    niveaux1 = canvas.create_text(310, 565 , text = "Niveau 1", font = "Arial 20", fill = "LightGrey")
    blocCommencer = canvas.create_rectangle(230, 540, 400, 590, fill = 'DeepSkyBlue2')
    commencer = canvas.create_text(315, 565 , text = "Commencer", font = "Arial 20", fill = "LightGrey")
    canvas.tag_bind(blocCommencer,'<ButtonPress-1>', clickContinuer)
    canvas.tag_bind(commencer,'<ButtonPress-1>', clickContinuer)
    canvas.pack()

#---------------------------------------Boucle principale------------------------------#
def update():
    global currentPage
    if page != currentPage:
        pageManagement(page)
        currentPage = page
    canvas.after(20, update)




base()
update()
canvas.mainloop()


