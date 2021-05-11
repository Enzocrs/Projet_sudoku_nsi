"""
Programme lié à la base de données (sqlite3)
Version du 11 Mai 2021
Enzo CROSES
"""
import sqlite3


# Connexion à la base de données et association du curseur à la variable "c"
conn = sqlite3.Connection("database.db")
c = conn.cursor()

# Création du tableau qui gère les grilles

c.execute("""
CREATE TABLE IF NOT EXISTS Grilles(
    Id_Grille INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    ligne_1 TEXT
    ligne_2 TEXT
    ligne_3 TEXT
    ligne_4 TEXT
    ligne_5 TEXT
    ligne_6 TEXT
    ligne_7 TEXT
    ligne_8 TEXT
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




grille = [
        [7, 6, 5, 9, 2, 1, 4, 8, 3],
        [9, 8, 3, 5, 7, 4, 6, 1, 2],
        [4, 1, 2, 6, 3, 8, 5, 9, 7],
        [2, 4, 8, 1, 5, 7, 3, 6, 9],
        [5, 7, 1, 3, 9, 6, 8, 2, 4],
        [3, 9, 6, 4, 8, 2, 1, 7, 5],
        [6, 3, 9, 2, 1, 5, 7, 4, 8],
        [1, 2, 7, 8, 4, 3, 9, 5, 6],
        [8, 5, 4, 7, 6, 9, 2, 3, 1]
    ]

def inserer_nouvelle_grille(grille):
	c.execute("""
		INSERT INTO Grilles (ligne_1) VALUES (?)""", grille
		)

inserer_nouvelle_grille(grille)
# Fermeture du fichier
conn.commit()
c.close()