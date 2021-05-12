"""
Ce programme contient uniquement des fonctions pour permettre d'accelerer les taches longues de la programmation
Responsable: Enzo CROSES et Hugo LEROUX
"""


def converti_ligne(ligne):
	"""
	converti 123456789 en [1, 2, 3, 4, 5, 6, 7, 8, 9]
	"""
	liste = [int(car) for car in str(ligne)]
	print(liste)

while 1:
	converti_ligne(int(input("Entrer chiffre: ")))