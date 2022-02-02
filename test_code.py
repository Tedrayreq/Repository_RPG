# from random import randint

# from personnage import *
# from profession import *
# from objet import *
# from monstre import *
# from quete import *
# from map import *
# from boss import *
# from pnj import *
# from ville import *
# from lieu import *
# from functions import *
# from Combat import *

arme1 = Objet("épée rouillée", 10, 0, 0, 10)
tete1 = Objet("chapeau de paille", 0, 10, 0, 10)

monstre1 = Monstre("sanglier", 30, 5, 10, [arme1, tete2])

map1 = Map("La forêt", 1, 5, [monstre1, monstre2, monstre3])



# Création héros
pseudo = input("Quel est ton nom ?\n")
print("Bon courage", pseudo, "\n")
heros = Personnage(pseudo)
heros.position = map1
heros.quetes = [quete1]
heros.Gagner_objet(arme1)
heros.Equiper_objet(arme1)
heros.gold = 100
input("Appuyer sur entrer pour continuer\n")

combat1 = Combat(heros, monstre1)
combat1.Start_combat()