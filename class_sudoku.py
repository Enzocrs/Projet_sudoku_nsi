from random import shuffle
class Sudoku:
    """
    Créer la classe principale qui permettra de creer et d'intéragir avec un jeu
    """
  
    def __init__(self, grid=[]):
        self.grid = grid

    def create_grid(self):
        """
        On créer une grille que l'on mélange
        """
        # En partant de ce modèle, les lignes sont forcément jouables (pas de chiffres identiques)
        self.grid = [
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9]
        ]

        for row in self.grid:
            shuffle(row)

    
    def check_grid(self):
        """
        Va vérifier si les colonnes sont jouables, si c'est la cas, la grille est jouable car les lignes le sont forcément
        """
        #Pour chaque colonnes, on créer une liste des chiffres
        col_1 = [i[0] for i in self.grid]
        col_2 = [i[1] for i in self.grid]
        col_3 = [i[2] for i in self.grid]
        col_4 = [i[3] for i in self.grid]
        col_5 = [i[4] for i in self.grid]
        col_6 = [i[5] for i in self.grid]
        col_7 = [i[6] for i in self.grid]
        col_8 = [i[7] for i in self.grid]
        col_9 = [i[8] for i in self.grid]

        liste_col = [col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9]

        for colonne in liste_col:
            # si les colonnes ne sont pas de cette forme, cela signifie que la colonne possède deux chiffres identiques
            if sorted(colonne) != [1,2,3,4,5,6,7,8,9]:
                return False
        return True

    def create_playable_grid(self):
        """
        Permet de créer une grille de sudoku jouable
        """
        self.create_grid()
        while self.check_grid():
            self.create_grid()

# =================================================== Zone de test ====================================================
game_1 = Sudoku()
"""
game_2 = Sudoku()
game_3 = Sudoku()
game_4 = Sudoku()
game_5 = Sudoku()
game_6 = Sudoku()
game_7 = Sudoku()
game_8 = Sudoku()
game_9 = Sudoku()
game_10 = Sudoku()
"""
liste_game = [game_1]
for game in liste_game:
    game.create_playable_grid()
assert game_1.check_grid()
        
    
