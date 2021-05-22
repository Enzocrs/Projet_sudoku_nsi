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

# REMETTRE EN COMMENTAIRE APRES EXECUTION
# inserer_nouvelle_grille(dico_grille)

# ======================================== Vérification de l'unicité du pseudo ========================================
def est_unique():
	"""
    Cette fonction permet de bloquer l'ajout d'un nouvel utilisateur dans la base de données si son pseudo est
    identique à un pseudo déjà présent dans la base de données, afin d'éviter tout conflit
    """  
	c.execute("SELECT pseudo FROM joueurs WHERE pseudo=:pseudo", dico_joueur)
	meme_pseudo = c.fetchall()
	return not meme_pseudo

# ================================================== Ajouter joueur ===================================================

# NE RIEN MODIFIER
dico_joueur = {
    "pseudo" : ui.new_pseudo.get(),
    "password" : ui.new_password.get()
}

def inserer_nouveau_joueur(dico_joueur):
    if est_unique() and dico_joueur["password"]:
        c.execute("""
        INSERT INTO Joueurs (pseudo, password)
        VALUES (:pseudo, :password)"""
        , dico_joueur
        )
# REMETTRE EN COMMENTAIRE APRES EXECUTION
#inserer_nouveau_joueur(dico_joueur)

# ============================================ Connexion de l'utilisateur =============================================

dico_login = {
    "pseudo" : ui.log_pseudo.get(),
    "password" : ui.log_password.get()
}


def autoriser_connexion():
	"""
    Retourne un Booléen pour autoriser au non la connexion d'un utilisateur en fonction de la validité des informations
    entrées dans le formumaire de connexion
    """
	c.execute("SELECT * FROM joueurs WHERE pseudo=:pseudo AND password=:password", dico_login)
	connexion = c.fetchone()
	return bool(connexion)


conn.commit()
c.close()