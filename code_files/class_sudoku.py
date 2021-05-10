from random import shuffle
class Sudoku:
    """
    Créer la classe principale qui permettra de creer et d'intéragir avec un jeu
    """
    
    """
    pk init on peut le faire en même temps que create / si on init create est fauyx c plus modifier
    """
    #modification du init
    def __init__(self):
        self.grid = []

    def create_grid(self):
        """
        On créer une grille que l'on mélange
        """
        # En partant de ce modèle, les lignes sont forcément jouables (pas de chiffres identiques)
        

# =================================================== Zone de test ====================================================
    
