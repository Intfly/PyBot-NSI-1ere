from tkinter import *
import tkinter.font as font
import webbrowser

fen = Tk()
fen.geometry("750x500")
fen.title("PyBot")


frame_p = Frame(fen)
frame_p.pack(side="top", expand=True, fill="both")

can = Canvas(frame_p,bg="white", height=500, width=750)
can.place(x=-2,y=-2)

#variables utiles dans le code
olhelper = 0
next_helper = 0
home_hlp = 0
apos='"'


def menu_home():
    global home_hlp
    if home_hlp !=0:  
        for widgets in frame_p.winfo_children():
           if widgets.winfo_class() != 'Canvas':
              widgets.destroy()
    can.delete(ALL)
    button_home_act_t = Button(frame_p,image = button_home_img_resized,width= 180,height=40,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",highlightbackground="white",text = 'tutoriel',compound="center",font=Font_button,command=tuto_1)
    button_home_act_n = Button(frame_p,image = button_home_img_resized,width= 180,height=40,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",highlightbackground="white",text = 'nouveau',compound="center",font=Font_button,command=nouveau_1)
    button_home_act_n.place(x=460,y=270)
    button_home_act_t.place(x=460,y=150)
    can.create_image(-40,0,image=linear_gradent_home)
    can.create_text(70,100,fill="white",text="PyBot",font=Font_PyBot)
    can.create_text(160,135,fill="white",text="Créez votre propre bot discord",font=Font_desc)
    home_hlp = 1

#fonction du bouton suivant
def interface_suivante():
    global vect
    if next_helper == 1:
        tuto_2()
    elif next_helper == 2:
        tuto_3()
    elif next_helper == 3:
        tuto_4()
    elif next_helper == 5:
        tok=ent_tok.get()
        ide=ent_id.get()
        vect=[tok,ide]
        nouveau_2()
        return vect

def ftn_commande(cmd):
    if cmd == 1:
        print(5)
    elif cmd ==2:
        print(2)
#premier menu en cliquant sur "tutoriel" 
def tuto_1():
    global olhelper
    global next_helper
    olhelper,next_helper = 1,1
    can.delete(ALL)
    for widgets in frame_p.winfo_children():
        if widgets.winfo_class() != 'Canvas':
            widgets.destroy()
    can.create_image(0,0,image=linear_gradient_1)
    can.create_image(10,10,image=img_bck_white)
    can.create_text(150,50,fill="#7256B2",text="prérequis",font=Font_titre_gros)
    can.create_text(300,165,fill="white",text="-ouvrez le portail de développeur discord:\n\n\n-connectez-vous",font=Font_desc)
    button_link= Button(frame_p,image = button_open_link,width= 150,height=25,relief=FLAT,bg="#6f60c0",fg="white",activeforeground="white",borderwidth=0,activebackground="#6f60bf",highlightbackground="white",text = 'cliquez ici',compound="center",font=Font_button,command=open_link)
    button_link.place(x=150,y=150)
    button_next = Button(frame_p,image = button_next_img_resized,width= 150,height=25,relief=FLAT,bg="#7159b5",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#7159b5",highlightbackground="#7159b5",text = 'suivant',compound="center",font=Font_button,command=interface_suivante)
    button_next.place(x=575,y=450)
    can.create_image(250,340, image=DDPconnexion_resized)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#6f60c0",fg="white",activeforeground="white",borderwidth=0,activebackground="#6f62c3",highlightbackground="white",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)

def tuto_2():
    global next_helper
    next_helper = 2
    can.delete(ALL)
    for widgets in frame_p.winfo_children():
        if widgets.winfo_class() != 'Canvas':
            widgets.destroy()
    can.create_image(0,0,image=linear_gradient_1)
    can.create_image(10,10,image=img_bck_white)
    can.create_text(150,50,fill="#7256B2",text="prérequis",font=Font_titre_gros)
    can.create_text(300,165,fill="white",text="-créez une nouvelle application grâce au bouton en haut à droite",font=Font_desc)
    can.create_image(120,210, image=new_app)
    can.create_text(120,260,fill="white",text="vous y trouverez",font=Font_desc)
    can.create_text(273,260,fill="#ff7583",text="l'ID de l'application",font=Font_desc)
    can.create_text(443,260,fill="white",text="(vous sera demandé)",font=Font_desc)
    button_next = Button(frame_p,image = button_next_img_resized,width= 150,height=25,relief=FLAT,bg="#7159b5",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#7159b5",highlightbackground="#7159b5",text = 'suivant',compound="center",font=Font_button,command=interface_suivante)
    button_next.place(x=575,y=450)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#6f60c0",fg="white",activeforeground="white",borderwidth=0,activebackground="#6f62c3",highlightbackground="white",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)

def tuto_3():
    global next_helper
    next_helper = 3
    can.delete(ALL)
    for widgets in frame_p.winfo_children():
        if widgets.winfo_class() != 'Canvas':
            widgets.destroy()
    can.create_image(0,0,image=linear_gradient_1)
    can.create_image(10,10,image=img_bck_white)
    can.create_text(150,50,fill="#7256B2",text="prérequis",font=Font_titre_gros)
    can.create_text(225,175,fill="white",text=f"-dans l'onglet {apos}Bot{apos} du menu à gauche\n\n       ajoutez un nouveau Bot",font=Font_desc)
    can.create_image(150,250, image=new_bot)
    can.create_text(180,300,fill="white",text=f"vous y trouverez le ",font=Font_desc)
    can.create_text(320,300,fill="#ff7583",text=f"TOKEN du bot",font=Font_desc)
    can.create_text(475,300,fill="white",text="(vous sera demandé)",font=Font_desc)
    button_next = Button(frame_p,image = button_next_img_resized,width= 150,height=25,relief=FLAT,bg="#7159b5",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#7159b5",highlightbackground="#7159b5",text = 'suivant',compound="center",font=Font_button,command=interface_suivante)
    button_next.place(x=575,y=450)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#6f60c0",fg="white",activeforeground="white",borderwidth=0,activebackground="#6f62c3",highlightbackground="white",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)

def tuto_4():
    can.delete(ALL)
    for widgets in frame_p.winfo_children():
        if widgets.winfo_class() != 'Canvas':
            widgets.destroy()
    can.create_image(0,0,image=linear_gradient_1)
    can.create_image(10,10,image=img_bck_white)
    can.create_text(150,50,fill="#7256B2",text="installation",font=Font_titre_gros)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#7259b6",fg="white",activeforeground="white",borderwidth=0,activebackground="#7259b6",highlightbackground="white",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=575,y=450)   
#premier menu en cliquant sur "nouveau" 
def nouveau_1():
    global ent_tok
    global ent_id
    global next_helper
    next_helper = 5
    can.delete(ALL)
    for widgets in frame_p.winfo_children():
        if widgets.winfo_class() != 'Canvas':
            widgets.destroy()
    can.create_image(0,0, image= linear_gradient_2)
    can.create_image(378,235,image=ent)
    can.create_text(265,140,fill="grey",text="ID du Bot",font=Font_desc)
    ent_id = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
    ent_id.place(x=225,y=150,width=300,height=50)
    can.create_text(290,260,fill="grey",text="TOKEN du Bot",font=Font_desc)
    ent_tok = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_titre,fg="#686868")
    ent_tok.place(x=225,y=270,width=300,height=50)
    button_next = Button(frame_p,image = button_open_link,width= 125,height=25,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",highlightbackground="#7159b5",text = 'perdus?',compound="center",font=Font_button,command=tuto_1)
    button_next.place(x=180,y=365)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",highlightbackground="white",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450) 
    button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",highlightbackground="#7159b5",text = 'suivant',compound="center",font=Font_button,command=interface_suivante)
    button_next.place(x=600,y=450) 

def nouveau_2():
    global cmd
    global next_helper
    cmd=15
    next_helper = 6
    can.delete(ALL)
    for widgets in frame_p.winfo_children():
        if widgets.winfo_class() != 'Canvas':
            widgets.destroy()
    can.create_image(0,0, image= linear_gradient_2)
    for i in range(9):# créé automatiquement 9 boutons avec des textes différents(rend le code plus lent mais plus propre)
        commande = Button(frame_p,image =commande_img,width= 155,height=45,relief=FLAT,bg="#a569c2",fg="#a569c2",activeforeground="#a569c2",borderwidth=0,activebackground="#a569c2",highlightbackground="white",text = 'Menu',compound="center",font=Font_button,command=lambda m=1+i:ftn_commande(m))
        if i<=2:
            commande.place(x=125+(180*i),y=75)
        elif i>=3 and i<=5:
            commande.place(x=125+(180*(i-3)),y=200)
        elif i>5 and i<=7:
            commande.place(x=125+(180*(i-6)),y=325)
        elif i == 8:
            commande.place(x=575,y=435)      
        if i == 1:
            commande['text']= "move"
        elif i == 2:
            commande['text']= "kick"
        elif i == 3:
            commande['text']= "ban"
        elif i == 3:
            commande['text']= "déconnecte quelqu'un"
        elif i == 4:
            commande['text']= "rich presence"
        elif i == 5:
            commande['text']= "message"
        elif i == 6:
            commande['text']= "rejoins serv"
        elif i == 7:
            commande['text']= "calcul"
        elif i == 8:
            commande['text']= "préfixe"
    
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",highlightbackground="white",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)

def cmd_name():
    global next_helper
    next_helper = 7
    can.delete(ALL)
    for widgets in frame_p.winfo_children():
        if widgets.winfo_class() != 'Canvas':
            widgets.destroy()
    can.create_image(0,0, image= linear_gradient_2)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",highlightbackground="white",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)
    can.create_text(265,140,fill="grey",text="nom de la commande",font=Font_desc)
    ent_id = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
    ent_id.place(x=225,y=150,width=300,height=50)    
    

#ouvre des liens différents en fonciton de la fenêtre dans laquelle le bouton est cliqué
def open_link():
    global olhelper
    if olhelper == 1:
        webbrowser.open_new("https://discord.com/developers/applications")

#les polices principales du programme
Font_button = font.Font(family="Abadi MT",size=14,weight="bold")
Font_PyBot = font.Font(family="Gadugi",size=22,weight="bold")
Font_desc = font.Font(family="Arial Baltic",size=14)
Font_titre = font.Font(family="Gadugi",size=16,weight="bold")
Font_titre_gros = font.Font(family="Gadugi",size=25,weight="bold")
Font_commande = font.Font(family="Arial Baltic",size=16)

#importations et modifications (si nécessaire) d'images
linear_gradent_home = PhotoImage(file="PyBot-NSI-1ere\images\linear-gradient-home.png")
button_home_img = PhotoImage(file="PyBot-NSI-1ere\images\-button-home.png")
button_home_img_resized = button_home_img.subsample(2)
button_open_link = button_home_img.subsample(3)
DDPconnexion = PhotoImage(file="PyBot-NSI-1ere\images\DDP-connexion.png")
DDPconnexion_resized = DDPconnexion.subsample(2)
linear_gradient_1 = PhotoImage(file="PyBot-NSI-1ere\images\linear-gradient-1.png")
button_next_img = PhotoImage(file="PyBot-NSI-1ere\images\-button-next.png")
button_next_img_resized = button_next_img.subsample(3)
img_bck_white = PhotoImage(file="PyBot-NSI-1ere\images\prerequis.png")
new_app = PhotoImage(file="PyBot-NSI-1ere\images\-app-nvx.png")
new_bot = PhotoImage(file="PyBot-NSI-1ere\images\-bot-nvx.png")
linear_gradient_2 = PhotoImage(file="PyBot-NSI-1ere\images\linear-gradient-2.png")
ent = PhotoImage(file="PyBot-NSI-1ere\images\ent.png")   
ent = ent.subsample(2)
commande_img = PhotoImage(file="PyBot-NSI-1ere\images\commande.png")
commande_img = commande_img.subsample(2)

menu_home()
frame_p.mainloop()