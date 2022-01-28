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


# choix 1 explorer
        # alea coffre ou combat
        # continuer ou arrêter explo -> retour en ville + (cls)
    
# choix 2 profil
    # Afficher stats
        # exit (cls)
    # Afficher quêtes
        # exit (cls)
    # Afficher inventaire
        # Afficher inventaire
        # Afficher equipé
            # Menu inventaire :
                # 1 - Equiper item
                # 2 - Ranger item équipé dand l'inventaire
                # 3 - Utiliser potion
                # 4 - exit ( cls)
    # Continuer ou arrêter explo -> retour en ville + (cls)

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

#################################################################################
#                                   fonction combat                             #
#################################################################################

def combat(personnage, monstre):
    clear()
    print("--------------------------------------------")
    print("Vous affrontez ", monstre.nom, "de niv :", monstre.niv)
    print("Vous avez :", personnage.current_hp,"hp")
    print("Le monstre a :", monstre.current_hp,"hp")
    input("--------------------------------------------")
    
    while personnage.Vivant() and monstre.Vivant():
        luck_personnage = randint(1, 100)
        luck_monstre = randint(1, 100)
        coef_attaque_personnage = 1
        coef_attaque_monstre = 1

        print("Vous faites un", luck_personnage)
        if luck_personnage <= 10:
            print("Aie, vous glissez pendant votre attaque et vous fracassez au sol...")
            coef_attaque_personnage = 0
        
        elif 10 < luck_personnage <= 20:
            print("Vous manquez tomber et portez votre attaque du bout de votre épée !")
            coef_attaque_personnage = 0.5

        elif 20 < luck_personnage <= 80:
            print("Vous portez votre attaque !")

        elif 80 < luck_personnage <= 90:
            print("Votre attaque frôle la perfection !")
            coef_attaque_personnage = 1.5

        elif 90 < luck_personnage <= 100:
            print("Votre attaque fend l'air et s'abat avec fracas sur votre ennemi : magnifique !")
            coef_attaque_personnage = 2
        
        dgts_personnage = (personnage.force + personnage.niv) * coef_attaque_personnage
        print("Votre attaque inflige ", dgts_personnage, " hp au monstre adverse\n")
        monstre.Perdre_hp(dgts_personnage)

        if monstre.current_hp > 0:
            print("Le monstre fait un", luck_monstre)
            if luck_monstre <= 10:
                print("Le monstre va pour vous porter un coup, trébuche et s'écrase au sol !")
                coef_attaque_monstre = 0

            elif 10 < luck_monstre <= 20:
                print("Le monstre trébuche et vous effleure !")
                coef_attaque_monstre = 0.5

            elif 20 < luck_monstre <= 80:
                print("Le monstre vous attaque !")

            elif 80 < luck_monstre <= 90:
                print("L'attaque du monstre va faire mal, attention !")
                coef_attaque_monstre = 1.5

            elif 90 < luck_monstre <= 100:
                print("Vous sentez la puissance du coup que le monstre vous a porté, la douleur est insoutenable...")
                coef_attaque_monstre = 2
            
            dgts_monstre = (monstre.force + monstre.niv) * coef_attaque_monstre
            print("L'attaque du monstre vous fait perdre ", dgts_monstre, " hp\n")
            personnage.Perdre_hp(dgts_monstre)

        else:
            coef_attaque_monstre = 0

        print("--------------------------------------------")
        print("Il vous reste :", personnage.current_hp, "hp\nIl reste au monstre :", monstre.current_hp, "hp")
        print("--------------------------------------------\n")
        input()
        clear()
        print("--------------------------------------------")

    if personnage.Vivant() == False:
        print("Tout devient noir, vous mourrez.")
    
    else:
        montant_xp = int(monstre.xp) * int(monstre.niv)
        clear()
        print("---------------------")
        print("Vous êtes victorieux !\nVous gagnez", montant_xp,"xp !")
        print("---------------------\n")
        personnage.Gain_xp(montant_xp)
        personnage.Level_up()
        rand_table_loot = randint(0, (len(monstre.table_butin)-1))
        personnage.Gagner_objet(monstre.table_butin[rand_table_loot])
        print("Vous trouvez :",monstre.table_butin[rand_table_loot].nom,"sur le monstre !")
        for i in personnage.quetes:
            if i.active and not i.done:
                i.Kill()

        input()

    monstre.Restart()
