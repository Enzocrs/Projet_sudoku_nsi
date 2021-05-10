import sqlite3

# Connexion à la base de données et association du curseur à la variable "c"
conn = sqlite3.Connection("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS Grilles(
    Id_Grille INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    Grille TEXT
)""")





# Fermeture du fichier
conn.commit()
c.close()