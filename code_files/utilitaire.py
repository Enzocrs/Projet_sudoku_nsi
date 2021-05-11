"""
Ce programme contient uniquement des fonctions pour permettre d'accelerrer les taches longues de la programmation
"""


def converti_ligne(ligne):
	"""
	converti 123456789 en [1, 2, 3, 4, 5, 6, 7, 8, 9]
	"""
	liste = []
	for car in str(ligne):
		liste.append(int(car))
	print(liste)

while 1:
	converti_ligne(int(input("Entrer chiffre: ")))