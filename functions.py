from random import randint

from personnage import *
from profession import *
from objet import *
from monstre import *
from boss import *
from quete import *
from map import *
from pnj import *
from ville import *
from lieu import *
from data import *

##############################################################################
#                                Check erreur                                #
##############################################################################
def check_int(data):
    continuer = False
    try:
        data = int(data)
    except ValueError:
        print("Entrée incorrecte, veuillez rentrez un nombre")
    else:
        continuer = True
    finally:
        return continuer

#############################################################################
#                                   Utilities                               #
#############################################################################




#############################################################################
#                                   display                                 #
#############################################################################


def clear():
    print("\033[H\033[J", end="")

# Mise en place options du menu combat. 
# Class compétence non ajouté et non liée à class personnage
# Objet actuellement utilisables : class Potion
# Fuite impossible contre class Boss
# Prévoir boost chance de réussir fuite si niv perso < monstre
def menu_combat(personnage, monstre):
    clear()
    print("Vos PV :", personnage.current_hp, "              ", monstre.name, "PV restant :", monstre.current_hp)
    print("Que voulez-vous faire ?")
    print("1 - Attaquer")
    print("2 - Utiliser une compétence")
    print("3 - Utiliser objet")
    print("4 - Tenter de fuir")

def menu_hors_ville():
    clear()
    print("Que voulez-vous faire ?")
    print("1 - Continuer l'exploration")
    print("2 - Afficher stats")
    print("3 - Afficher quêtes")
    print("4 - Afficher inventaire")
    print("5 - Retourner en ville")

def menu_ville():
    clear()
    print("Vous êtes en ville")
    print("1 - Taverne")
    print("2 - Shop")
    print("3 - Guilde")
    print("4 - Quitter ville")

def menu_tavernier():
    print(pnj1.dialogue[0], "\n1 - J'aimerai prendre une chambre pour me reposer (-20po)"
                   "\n2 - Une pinte Tavernier ! (-10po)")
    if not pnj3 in lieu1.occupant:
        print("3 - Des nouvelles du fermier ?")
    print("\n\"e\" pour exit")

def menu_shop():
    print(pnj2.dialogue[0], "\n1 - Acheter un item (actuellement indisponible la crise tout ça tout ça)"
                            "\n2 - Vendre un item\n"
                            "\n\"e\" pour quitter Shop")
