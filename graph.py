"""
PARTIE GRAPHIQUE DE L'APPLICATION
Entièrement faîte à l'aide de Tkinter
Version du 31 Mars 2021
"""
from tkinter import *


window = Tk()

# =========================================== Caractéristiques de la fenêtre ==========================================

window.title("Su-Do-Ku !")
window.geometry("1080x720")
window.minsize(850, 500)
window.config(background = "#2E3440")

# ================================================= Ecran de Bienvenue ================================================

frame_welcome = Frame(window, bg = "#2E3440")

label_welcome = Label(frame_welcome, text = "Bienvenue sur l'application incontournable pour jouer au Su - DoKu !",
                      font = ("Arial", 20), bg = "#2E3440", fg = "white")
label_welcome.pack()


label_creators = Label(frame_welcome, text = "By Enzo CROSES and Hugo LEROUX", font = ("Arial", 12), bg = "#2E3440",
                       fg = "white")
label_creators.pack()

welcome_button = Button(frame_welcome, text = "Commencez à jouer !", font = ("Arial", 15), bg ="#2E3440", fg = "white")
welcome_button.pack(pady = 20, fill = X)

frame_welcome.pack(expand = TRUE)

window.mainloop()
