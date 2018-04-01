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
#-----------------------------Fonctions Evenementiels--------------------------#
def clavier(event):
    global page
    page = 2
    
def clickRegles(event):
    global page
    page = 3
    
def clickNiveaux(event):
    global page
    page = 7
    
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
def sixthPage():
    canvas.pack()
def seventhPage():
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
