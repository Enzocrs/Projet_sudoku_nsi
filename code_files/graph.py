"""
PARTIE GRAPHIQUE DE L'APPLICATION
Entièrement faîte à l'aide de Tkinter
Version du 04 Mai 2021
"""
from tkinter import *


window = Tk()

# =========================================== Caractéristiques de la fenêtre ==========================================

window.title("Su-Do-Ku !")
window.geometry("1920x1080")
window.minsize(850, 500)
window.state("zoomed")
window.config(background = "#2E3440")
window.iconbitmap("iconsudok.ico")
window.rowconfigure(0,weight=1)
window.columnconfigure(0, weight=1)

def show_frame(frame):
	frame.tkraise()

# ================================================= Ecran  ====================================================

# ========================= Info frame ====================================
frame_welcome = Frame(window)
frame_personne = Frame(window, bg = "green")
frame_choice_level = Frame(window, bg = "red")
frame_jeu = Frame(window, bg="blue")

for frame in (frame_welcome,frame_personne,frame_choice_level):
	frame.grid(row = 0,column = 0, sticky = 'nsew')

show_frame(frame_welcome)

# ============= frame_welcome =============

label_welcome = Label(frame_welcome, text = "Bienvenue sur l'application incontournable pour jouer au Su - DoKu !",
                      font = ("Arial", 30), bg = "#2E3440", fg = "white")
label_welcome.place(relx = 0.2, rely= 0.4)


label_creators = Label(frame_welcome, text = "By Enzo CROSES and Hugo LEROUX", font = ("Arial", 12), bg = "#2E3440",
                       fg = "white")
label_creators.place(relx = 0.9, rely= 0.5,anchor = CENTER)


welcome_button = Button(frame_welcome, text = "Commencez à jouer !", font = ("Arial", 15), bg ="#2E3440", fg = "white",
                        activebackground ="#2E3440", command = lambda:show_frame(frame_personne))
welcome_button.place(relx = 0.5, rely= 0.5,anchor = CENTER)

# ============= frame personne =============

label_welcome = Label(frame_personne, text = "Veuillez sélectioner l'utilisateur",
                      font = ("Arial", 20), bg = "#2E3440", fg = "white")
label_welcome.pack()

bttn_invit = Button(frame_personne, text="invité",command = lambda:show_frame(frame_choice_level))
bttn_new = Button(frame_personne, text="créer compte")
bttn_connect = Button(frame_personne, text="connexion")

bttn_invit.pack(pady = 10)
bttn_new.pack(pady = 10)
bttn_connect.pack(pady = 10)

# ============= frame choix niveaux =============

"""boutons différents"""
nombre = IntVar()
nombre.set(1)
level_1 = Radiobutton(frame_choice_level, text="level_1", variable=nombre, value=1)
level_2 = Radiobutton(frame_choice_level, text="level_2", variable=nombre, value=2)
level_3 = Radiobutton(frame_choice_level, text="level_3", variable=nombre, value=3)
select_Button = Button(frame_choice_level, text="démarrer le niveau", command=lambda:show_frame(frame_game))


level_1.pack()
level_2.pack()
level_3.pack()
select_Button.pack()

# ============= frame jeu =============

label_disclaimer = Label(frame_jeu, text="En cours de création")
retour = Button(frame_jeu, text="Retourner au menu précédent", command=lambda:show_frame(frame_choice_level))








window.mainloop()
