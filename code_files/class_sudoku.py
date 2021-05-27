"""
Ce programme contient toute les fonctions liées au jeu en lui même
Version du 27/05/2021
Responsable: Enzo CROSES
"""
from random import shuffle

import app

def rendre_jouable():
    """
    Transforme une grille pleine en grille jouable, retourne une liste qui en contient 9
    dans ces 9 listes il y a les chiffres invisibles, soit ceux que le joueur doit trouver
    """
    grille = app.recuperer_grille()
    
    
