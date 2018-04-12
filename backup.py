from tkinter import *
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
#Cartes
murHaut=[[1] * 10,
       [1,1,1,0,0,1,1,1,0,1],
       [0,1,1,0,1,0,0,1,1,0],
       [0,0,0,1,1,1,1,1,1,0],
       [0,0,0,1,0,1,1,0,0,0],
       [0,1,1,0,1,1,0,0,0,0],
       [0] * 10,
       [0,0,0,1,0,0,1,1,0,0],
       [1] * 10]

murGauche=[[1] * 8,
         [0,0,1,1,0,1,1,0],
         [0,0,0,1,1,0,1,1],
         [0,1,1,0,0,1,1,0],
         [1,1,0,0,0,1,1,0],
         [0,0,0,0,0,0,1,1],
         [0,1,1,0,0,1,1,0],
         [0,0,0,0,1,1,0,0],
         [0,0,0,1,1,1,1,0],
         [0,0,1,0,1,1,1,1],
         [1] * 8]
#-----------------------------Fonctions Dessin--------------------------#
def dessinCarteHaut (murHaut):
    vertical = len(murHaut)
    horizontal = len(murHaut[0])
    for i in range (vertical):
         for j in range (horizontal):
            if murHaut[i][j] == 1:
                refTopx = j * 60 + 20
                refTopy = i * 60 + 20
                murTop = canvas.create_rectangle(refTopx , refTopy, refTopx + 60 , refTopy + 1, fill = 'Grey')

def dessinCarteGauche (murGauche):
    vertical = len(murGauche)
    horizontal = len(murGauche[0])
    for i in range (vertical):
        for j in range (horizontal):
            if murGauche[i][j] == 1:
                refLeftx = i * 60 + 20
                refLefty = j * 60 + 20
                murLeft = canvas.create_rectangle(refLeftx, refLefty, refLeftx + 1 , refLefty + 60, fill = 'Grey')

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
    
def deleteCanvas():
    canvas.delete(*canvas.find_all())
    
def move(event):
    global pos
    press = event.keysym
    if press == "Up":
        pos = (pos[0], pos[1] - 10)            
    elif press == "Down":
        pos = (pos[0], pos[1] + 10)
    elif press == "Right":
        pos = (pos[0] + 10, pos[1])
    elif press == "Left":
        pos = (pos[0] -10, pos[1])
    canvas.coords(perso, pos[0], pos[1], pos[0]+25, pos[1]+25)
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
        fouthPage()
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
    canvas.bind_all('<Return>', clavier)
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
    global murTop
    global murLeft
#Affichage du labyrinthe
    dessinCarteHaut(murHaut)
    dessinCarteGauche(murGauche)
#Mouvement et affichage du bloc
    global pos
    global perso
    pos = (20,20)
    perso = canvas.create_rectangle(20,20,45,45,fill="violet")
    canvas.focus_set()
    canvas.bind("<Key>", move)
    canvas.pack()
def fourthPage():
    blocPause = canvas.create_rectangle(280, 150, 450, 200, fill = 'DeepSkyBlue2')
    blocRecommencer = canvas.create_rectangle(280, 230, 450, 280, fill = 'DeepSkyBlue2')
    continuer = canvas.create_text(360, 175, text = "Continuer", font = "Arial 19", fill = "Grey")
    recommencer = canvas.create_text(364, 255 , text = "Recommencer", font = "Arial 19", fill = "Grey")
    canvas.pack()
def fifthPage():
    felictations = canvas.create_text(360, 150, text = "Felicitations ! ", font = "Arial 50 italic", fill = "DeepSkyBlue2")
    message = canvas.create_text(360, 250, text = "Vous Avez Gagné", font = "Arial 50 italic", fill = "Grey")        
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
    commencer = canvas.create_text(170, 355 , text = "Commencer", font = "Arial 20", fill = "LightGrey")
    canvas.tag_bind(blocCommencer,'<ButtonPress-1>', clickContinuer)
    canvas.tag_bind(commencer,'<ButtonPress-1>', clickContinuer)
    canvas.pack()

#---------------------------------------Boucle principale------------------------------#
def update():
    global currentPage
    if page != currentPage:
        pageManagement(page)
        currentPage = page
    canvas.after(15, update)



base()
update()
