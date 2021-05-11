"""
Programme lié à la base de données (sqlite3)
Version du 10 Mai 2021
Enzo CROSES
"""
import sqlite3
import data

a = data.dico_grilles["grille_1"]
print(a)

# Connexion à la base de données et association du curseur à la variable "c"
conn = sqlite3.Connection("database.db")
c = conn.cursor()

# Création du tableau qui gère les grilles

c.execute("""
CREATE TABLE IF NOT EXISTS Grilles(
    Id_Grille INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    Grille TEXT
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




# Fermeture du fichier
conn.commit()
c.close()