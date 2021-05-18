"""
Programme lié à la base de données (sqlite3)
Version du 12 Mai 2021
Responsable: Enzo CROSES
"""
import sqlite3

import graph as ui


# Connexion à la base de données et association du curseur à la variable "c"
conn = sqlite3.Connection("database.db")
c = conn.cursor()

# Création du tableau qui gère les grilles

c.execute("""
CREATE TABLE IF NOT EXISTS Grilles(
    Id_ligne INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    ligne_1 TEXT,
    ligne_2 TEXT,
    ligne_3 TEXT,
    ligne_4 TEXT,
    ligne_5 TEXT,
    ligne_6 TEXT,
    ligne_7 TEXT,
    ligne_8 TEXT,
    ligne_9 TEXT
)
""")


# Création du tableau qui gère les joueurs

c.execute("""
CREATE TABLE IF NOT EXISTS Joueurs(
    Id_Joueur INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    Pseudo TEXT,
    Password TEXT,
    Grilles_jouées TEXT
)
""")

# ================================================== Ajouter grille ===================================================

# Modifier les valeurs pour insérer une nouvelle grille, ne jamais modifier les clefs
dico_grille = {
    "ligne_1" : "765921483",
    "ligne_2" : "983574612",
    "ligne_3" : "412638597",
    "ligne_4" : "248157369",
    "ligne_5" : "571396824",
    "ligne_6" : "396482175",
    "ligne_7" : "639215748",
    "ligne_8" : "127843956",
    "ligne_9" : "854769231"
}

def inserer_nouvelle_grille(dico_grille):
	c.execute("""
		INSERT INTO Grilles (ligne_1, ligne_2, ligne_3, ligne_4, ligne_5, ligne_6, ligne_7, ligne_8, ligne_9)
        VALUES (:ligne_1, :ligne_2, :ligne_3, :ligne_4, :ligne_5, :ligne_6, :ligne_7, :ligne_8, :ligne_9)"""
        , dico_grille
		)

# Remettre en commentaire après éxecution
# inserer_nouvelle_grille(dico_grille)

# ================================================== Ajouter joueur ===================================================

# NE RIEN MODIFIER
dico_joueur = {
    "pseudo" : ui.new_pseudo.get(),
    "password" : ui.new_password.get()
}

def inserer_nouveau_joueur(dico_joueur):
    c.execute("""
    INSERT INTO Joueurs (pseudo, password)
    VALUES (:pseudo, :password)"""
    , dico_joueur
    )
# inserer_nouveau_joueur(dico_joueur)

# ============================================ Connexion de l'utilisateur =============================================


conn.commit()
c.close()