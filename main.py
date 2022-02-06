from random import randint

from personnage import *
from profession import *
from objet import *
from Stuff import *
from Arme import *
from Tete import *
from Torse import *
from Jambiere import *
from Pied import *
from Gant import *
from Epaule import *
from Ceinture import *
from monstre import *
from quete import *
from map import *
from boss import *
from pnj import *
from ville import *
from lieu import *
from Combat import *
from functions import *

# Création héros
pseudo = input("Quel est ton nom ?\n")
print("Bon courage", pseudo, "\n")
heros = Personnage(pseudo)
heros.position = map1
heros.quetes = [quete1, quete2, quete3]
#heros.Gagner_objet(arme1)
arme1.Looter(heros)
#heros.Equiper_objet(arme1)
arme1.Equiper(heros)
heros.gold = 100
input("Appuyer sur entrer pour continuer\n")

# Main
while heros.Vivant():    
    
    # Menu hors ville
    menu_hors_ville()
    choix = input()
    # Explorer
    if choix == "1":
        clear()
        print("Vous continuez l'exploration")
        print("Vous êtes dans", heros.position.nom)
        input()
        continuer_combat = True
        while heros.Vivant() and continuer_combat:
            # which encounter
            rand_monstre = randint(1, 10)
            if rand_monstre <= 5:
                monstre = monstre1
            elif 5 < rand_monstre < 10:
                monstre = monstre2
            elif rand_monstre == 10:
                monstre = monstre3

            instance_combat = Combat(heros, monstre)
            instance_combat.Start_combat()
        
            if heros.Vivant():
                continuer = input("Continuer ? \"n\" pour arrêter\n")
                if continuer == "n":
                    continuer_combat = False
            else:
                print("...")

    # Afficher stats
    elif choix == "2":
        clear()
        print("STATS\n")
        heros.Afficher_stats()
        input("\nentrer pour exit")

    # Afficher quetes
    elif choix == "3":
        clear()
        heros.Afficher_quetes()
        input("\nentrer pour exit")
    
    # Afficher inventaire
    elif choix == "4":
        clear()
        inventaire = True
        while inventaire:
            clear()
            heros.Afficher_gold()
            print("Que voulez-vous consultez ?\n"
                  "1 - Sac\n"
                  "2 - Stuff équipé\n"
                  "3 - \"e\" pour exit")
            choix_inventaire = input("> ")

            #Sac
            if choix_inventaire == "1":
                clear()
                print("Sac")
                if len(heros.new_inventaire["Items"]) + len(heros.new_inventaire["Potions"]) + len(heros.new_inventaire["Armes"]) + len(heros.new_inventaire["Têtes"]) + len(heros.new_inventaire["Epaules"]) + len(heros.new_inventaire["Torses"]) + len(heros.new_inventaire["Gants"]) + len(heros.new_inventaire["Jambières"]) + len(heros.new_inventaire["Pieds"]) + len(heros.new_inventaire["Ceintures"]) == 0:
                    input("Votre sac est vide")
                else:
                    k = 0
                    for i in heros.new_inventaire:
                        print("\n" + i)
                        if len(heros.new_inventaire[i]) == 0:
                            print("vide")
                        else:
                            for j in heros.new_inventaire[i]:
                                print(j.nom)
                    input()
            
            # Stuff
            elif choix_inventaire == "2":
                clear()
                print("Stuff équipé")
                j = 0
                for cle, valeur in heros.stuff.items():
                    j += 1
                    if len(valeur) == 0:
                        print(j, "-", cle, ":", "vide")
                    else:
                        print(j, "-", cle, ":", valeur[0].nom, "force :", valeur[0].dgts, "; hp :", valeur[0].hp)
                print("Voulez-vous équiper un item ? y")
                choix_equiper = input("> ")
                if choix_equiper == "y":
                    equiper_mode = True
                    while equiper_mode:
                        clear()
                        print("Sur quel emplacement désirez-vous équiper un items ?\n"
                              "1 - Armes\n"
                              "2 - Têtes\n"
                              "3 - Epaules\n"
                              "4 - Torses\n"
                              "5 - Gants\n"
                              "6 - Jambières\n"
                              "7 - Pieds\n"
                              "8 - Ceintures\n"
                              "\"e\" pour exit")
                        choix_emplacement = input("> ")
                        if choix_emplacement == "e":
                            equiper_mode = False
                        
                        # Armes
                        elif choix_emplacement == "1":
                            clear()
                            print("Emplacement Armes")
                            if len(heros.stuff["Armes"]) == 0:
                                print("Actuellement rien d'équipé")
                            else:
                                print("Actuellement équipé :", heros.stuff["Armes"][0].nom, "force :", heros.stuff["Armes"][0].dgts, "; hp :", heros.stuff["Armes"][0].hp)
                            if len(heros.new_inventaire["Armes"]) == 0:
                                input("Vous n'avez rien d'équipable pour cet emplacement")
                            else:
                                print("Objet équipable :")
                                j = 0
                                for i in heros.new_inventaire["Armes"]:
                                    j += 1
                                    print(j, " - ", i.nom, "force :", i.dgts, "; hp :", i.hp)
                                print("Quel item voulez-vous équiper ?")
                                choix_arme = input("> ")

                                if check_int(choix_arme):
                                    choix_arme = int(choix_arme)
                                    if choix_arme <= len(heros.new_inventaire["Armes"]):
                                        heros.new_inventaire["Armes"][choix_arme-1].Equiper(heros)
                        
                        # Têtes
                        elif choix_emplacement == "2":
                            clear()
                            print("Emplacement Têtes")
                            if len(heros.stuff["Têtes"]) == 0:
                                print("Actuellement rien d'équipé")
                            else:
                                print("Actuellement équipé :", heros.stuff["Têtes"][0].nom, "force :", heros.stuff["Têtes"][0].dgts, "; hp :", heros.stuff["Têtes"][0].hp)
                            if len(heros.new_inventaire["Têtes"]) == 0:
                                input("Vous n'avez rien d'équipable pour cet emplacement")
                            else:
                                print("Objet équipable :")
                                j = 0
                                for i in heros.new_inventaire["Têtes"]:
                                    j += 1
                                    print(j, " - ", i.nom, "force :", i.dgts, "; hp :", i.hp)
                                print("Quel item voulez-vous équiper ?")
                                choix_arme = input("> ")

                                if check_int(choix_arme):
                                    choix_arme = int(choix_arme)
                                    if choix_arme <= len(heros.new_inventaire["Têtes"]):
                                        heros.new_inventaire["Têtes"][choix_arme-1].Equiper(heros)

                        # Epaules
                        elif choix_emplacement == "3":
                            clear()
                            print("Emplacement Epaules")
                            if len(heros.stuff["Epaules"]) == 0:
                                print("Actuellement rien d'équipé")
                            else:
                                print("Actuellement équipé :", heros.stuff["Epaules"][0].nom, "force :", heros.stuff["Epaules"][0].dgts, "; hp :", heros.stuff["Epaules"][0].hp)
                            if len(heros.new_inventaire["Epaules"]) == 0:
                                input("Vous n'avez rien d'équipable pour cet emplacement")
                            else:
                                print("Objet équipable :")
                                j = 0
                                for i in heros.new_inventaire["Epaules"]:
                                    j += 1
                                    print(j, " - ", i.nom, "force :", i.dgts, "; hp :", i.hp)
                                print("Quel item voulez-vous équiper ?")
                                choix_arme = input("> ")

                                if check_int(choix_arme):
                                    choix_arme = int(choix_arme)
                                    if choix_arme <= len(heros.new_inventaire["Epaules"]):
                                        heros.new_inventaire["Epaules"][choix_arme-1].Equiper(heros)

                        # Torses
                        elif choix_emplacement == "4":
                            clear()
                            print("Emplacement Torses")
                            if len(heros.stuff["Torses"]) == 0:
                                print("Actuellement rien d'équipé")
                            else:
                                print("Actuellement équipé :", heros.stuff["Torses"][0].nom, "force :", heros.stuff["Torses"][0].dgts, "; hp :", heros.stuff["Torses"][0].hp)
                            if len(heros.new_inventaire["Torses"]) == 0:
                                input("Vous n'avez rien d'équipable pour cet emplacement")
                            else:
                                print("Objet équipable :")
                                j = 0
                                for i in heros.new_inventaire["Torses"]:
                                    j += 1
                                    print(j, " - ", i.nom, "force :", i.dgts, "; hp :", i.hp)
                                print("Quel item voulez-vous équiper ?")
                                choix_arme = input("> ")

                                if check_int(choix_arme):
                                    choix_arme = int(choix_arme)
                                    if choix_arme <= len(heros.new_inventaire["Torses"]):
                                        heros.new_inventaire["Torses"][choix_arme-1].Equiper(heros)

                        # Gants
                        elif choix_emplacement == "5":
                            clear()
                            print("Emplacement Gants")
                            if len(heros.stuff["Gants"]) == 0:
                                print("Actuellement rien d'équipé")
                            else:
                                print("Actuellement équipé :", heros.stuff["Gants"][0].nom, "force :", heros.stuff["Gants"][0].dgts, "; hp :", heros.stuff["Gants"][0].hp)
                            if len(heros.new_inventaire["Gants"]) == 0:
                                input("Vous n'avez rien d'équipable pour cet emplacement")
                            else:
                                print("Objet équipable :")
                                j = 0
                                for i in heros.new_inventaire["Gants"]:
                                    j += 1
                                    print(j, " - ", i.nom, "force :", i.dgts, "; hp :", i.hp)
                                print("Quel item voulez-vous équiper ?")
                                choix_arme = input("> ")

                                if check_int(choix_arme):
                                    choix_arme = int(choix_arme)
                                    if choix_arme <= len(heros.new_inventaire["Gants"]):
                                        heros.new_inventaire["Gants"][choix_arme-1].Equiper(heros)

                        # Jambières
                        elif choix_emplacement == "6":
                            clear()
                            print("Emplacement Jambières")
                            if len(heros.stuff["Jambières"]) == 0:
                                print("Actuellement rien d'équipé")
                            else:
                                print("Actuellement équipé :", heros.stuff["Jambières"][0].nom, "force :", heros.stuff["Jambières"][0].dgts, "; hp :", heros.stuff["Jambières"][0].hp)
                            if len(heros.new_inventaire["Jambières"]) == 0:
                                input("Vous n'avez rien d'équipable pour cet emplacement")
                            else:
                                print("Objet équipable :")
                                j = 0
                                for i in heros.new_inventaire["Jambières"]:
                                    j += 1
                                    print(j, " - ", i.nom, "force :", i.dgts, "; hp :", i.hp)
                                print("Quel item voulez-vous équiper ?")
                                choix_arme = input("> ")

                                if check_int(choix_arme):
                                    choix_arme = int(choix_arme)
                                    if choix_arme <= len(heros.new_inventaire["Jambières"]):
                                        heros.new_inventaire["Jambières"][choix_arme-1].Equiper(heros)

                        # Pieds
                        elif choix_emplacement == "7":
                            clear()
                            print("Emplacement Pieds")
                            if len(heros.stuff["Pieds"]) == 0:
                                print("Actuellement rien d'équipé")
                            else:
                                print("Actuellement équipé :", heros.stuff["Pieds"][0].nom, "force :", heros.stuff["Pieds"][0].dgts, "; hp :", heros.stuff["Pieds"][0].hp)
                            if len(heros.new_inventaire["Pieds"]) == 0:
                                input("Vous n'avez rien d'équipable pour cet emplacement")
                            else:
                                print("Objet équipable :")
                                j = 0
                                for i in heros.new_inventaire["Pieds"]:
                                    j += 1
                                    print(j, " - ", i.nom, "force :", i.dgts, "; hp :", i.hp)
                                print("Quel item voulez-vous équiper ?")
                                choix_arme = input("> ")

                                if check_int(choix_arme):
                                    choix_arme = int(choix_arme)
                                    if choix_arme <= len(heros.new_inventaire["Pieds"]):
                                        heros.new_inventaire["Pieds"][choix_arme-1].Equiper(heros)

                        # Ceintures
                        elif choix_emplacement == "8":
                            clear()
                            print("Emplacement Ceintures")
                            if len(heros.stuff["Ceintures"]) == 0:
                                print("Actuellement rien d'équipé")
                            else:
                                print("Actuellement équipé :", heros.stuff["Ceintures"][0].nom, "force :", heros.stuff["Ceintures"][0].dgts, "; hp :", heros.stuff["Ceintures"][0].hp)
                            if len(heros.new_inventaire["Ceintures"]) == 0:
                                input("Vous n'avez rien d'équipable pour cet emplacement")
                            else:
                                print("Objet équipable :")
                                j = 0
                                for i in heros.new_inventaire["Ceintures"]:
                                    j += 1
                                    print(j, " - ", i.nom, "force :", i.dgts, "; hp :", i.hp)
                                print("Quel item voulez-vous équiper ?")
                                choix_arme = input("> ")
                                while not check_int(choix_arme):
                                    if choix_arme == "e":
                                        equiper_mode = False
                                    else:
                                        print("Quel item voulez-vous équiper ? \"e\" pour exit")
                                        choix_arme = input("> ")
                                if choix_arme <= len(heros.new_inventaire["Ceintures"]):
                                    choix_arme = int(choix_arme)
                                    heros.new_inventaire["Ceintures"][choix_arme-1].Equiper(heros)
            
            elif choix_inventaire == "e":
                inventaire = False

    # Ville
    elif choix == "5":
        clear()
        input("Vous retournez en ville")
        heros.Move(ville1)
        dialogue = ""
        
        while heros.position == ville1:
            # Menu ville
            menu_ville()
            choix_menu_ville = input("Où voulez-vous aller ?\n")
            
            # Taverne
            if choix_menu_ville == "1":
                # Menu
                taverne = True
                while taverne:
                    clear()
                    print("Vous êtes à la Taverne")
                    print("Vous apercevez :")
                    j = 0
                    for i in lieu1.occupant:
                        j += 1
                        print(j, "-", i.nom)
                    choix_pnj = input("A qui voulez-vous parler ?\ne pour exit\n")

                    # Tavernier
                    if choix_pnj == "1":
                        clear()
                        print("Vous saluez le", pnj1.nom)
                        input()
                        continuer = True
                        while continuer:
                            clear()
                            menu_tavernier()
                            dialogue = input()
                            if dialogue == "1":
                                if heros.gold >= 20:
                                    clear()
                                    input(pnj1.dialogue[1])
                                    heros.gold -= 20
                                    input("Vous payez 20po votre chambre et passez une bonne nuit de sommeil !")
                                    heros.current_hp = heros.hp
                                else:
                                    clear()
                                    input(pnj1.dialogue[3])

                            elif dialogue == "2":
                                if heros.gold >= 10:
                                    clear()
                                    input(pnj1.dialogue[2])
                                    heros.gold -= 10
                                    heros.current_hp += 10
                                    input("Rien de tel qu'une bonne bière !")
                                else:
                                    clear()
                                    input(pnj1.dialogue[3])


                            elif dialogue == "3" and not pnj3 in lieu1.occupant:
                                clear()
                                print(pnj1.dialogue[4])

                            elif dialogue == "e":
                                continuer = False

                    # Fermier
                    elif choix_pnj == "2" and pnj3 in lieu1.occupant:
                        clear()

                        if heros.quetes[0].rendue and heros.quetes[1].rendue and heros.quetes[2].rendue:
                            # Le fermier est vivant et la quête rendue
                            input("Bonjour l'ami !")

                        elif heros.quetes[0].done and not heros.quetes[0].rendue and heros.quetes[1].rendue and heros.quetes[2].rendue:
                            # Le fermier est encore vivant la quête non rendue
                            if heros.quetes[0].Kill():
                                print("Aventurier !\n"
                                      "J'ai eu vent de vos exploits.\n"
                                      "Si vous n'aviez pas fait le ménage avant de revenir me prévenir que vous aviez tué ces sanglier...\n"
                                      "Je serai retourné à mes champs et...\n"
                                      "Les gobelins ou l'orc qui rodaient aux alentours dont vous vous êtes occupé m'auraient tué !\n"
                                      "Vous êtes un vrai héros"
                                      "Ce n'est pas grand chose, mais prenez ceci en plus de la récompense de quête, j'insiste !")
                                #heros.Gagner_objet(arme4)
                                arme4.Looter(heros)
                                input("Vous obtenez l'épée-qui-en-jette !\n"
                                      "Prendre le temps de bien faire les choses est la meilleure des voies !")
                                heros.quetes[0].Rendre_quete()

                        elif heros.quetes[0].done and not heros.quetes[0].rendue and heros.quetes[1].rendue and not heros.quetes[2].rendue:
                            # Le pnj est voué à mourir si la quête est rendue
                            if heros.quetes[0].Kill():
                                input("Merci, pour ces sangliers et les gobelins, je vais pouvoir retourner travailler dans mes champs !")
                                heros.quetes[0].Rendre_quete()    
                                lieu1.occupant.remove(pnj3)

                        elif heros.quetes[0].done and not heros.quetes[0].rendue and not heros.quetes[1].rendue and not heros.quetes[2].rendue:
                            # Le pnj est voué à mourir si la quête est rendue
                            if heros.quetes[0].Kill():
                                input("Merci de m'avoir débarassé de ces fichus sangliers ! Je retourne à mes champs !")
                                heros.quetes[0].Rendre_quete()
                                lieu1.occupant.remove(pnj3)

                        elif heros.quetes[0].active and not heros.quetes[0].done and not heros.quetes[0].rendue and not heros.quetes[1].rendue and not heros.quetes[2].rendue:
                            # Quete non finie, destin du fermier en suspend
                            input("Vous avançez ?")

                        else:
                            print("Vous saluez le", pnj3.nom)
                            print(pnj3.dialogue[0])
                            input("ça n'a pas l'air d'aller très fort...")
                            print(pnj3.dialogue[1])
                            dialogue = input("1 - Je vous paye un coup à boire ? (- 10po)\n"
                                             "2 - J'ai cru comprendre que les gobelins rodaient dans les environs\n")
                            
                            if dialogue == "1" and heros.gold >= 10:
                                heros.gold -= 10
                                input(pnj3.dialogue[3])
                                print(quete1.description)
                                heros.quetes[0].active = True
                                input("Vous acceptez la quête")
                        
                            elif dialogue == "1" and heros.gold < 10:
                                input(pnj3.dialogue[4])

                            elif dialogue == "2":
                                input(pnj3.dialogue[2])

                    elif choix_pnj == "e":
                        taverne = False

            # Shop
            elif choix_menu_ville == "2":
                if heros.gold == 0:
                    clear()
                    print("Vous êtes au Shop")
                    input("Z'avez pas d'argent pécor, du balai !")
                shop = True
                while shop:
                    clear()
                    menu_shop()
                    choix_shop = input()
                    
                    # Acheter
                    if choix_shop == "1":
                        acheter = True
                        while acheter:
                            clear()
                            print("Qu'est-ce-qui vous ferez plaisir ? \"e\" pour exit")
                            print("1 - Potion de soin de base rend 20 hp [40 po]")
                            if heros.niv >= 5:
                                print("2 - Potion de soin moyenne rend 50 hp [100 po]")
                            
                            if heros.niv >= 10:
                                print("3 - Potion de soin supérieure rend 100 hp [200 po]")
                            choix_achat = input("> ")
                            
                            if choix_achat == "1":
                                if heros.gold >= 40:
                                    heros.gold -= 40
                                    potion1.Looter(heros)
                                    input("Vous achetez une potion de soin de base contre 40 po")
                                else:
                                    input("T'essayes de m'arnaquez pécor ? Pas d'oseil pas de soin ! Y'a pas de couverture sociale ici !")
                            elif choix_achat == "2" and heros.niv >= 5:
                                if heros.gold >= 100:
                                    heros.gold -= 100
                                    potion1.Looter(heros)
                                    input("Vous achetez une potion de soin moyenne contre 100 po")
                                else:
                                    input("T'essayes de m'arnaquez pécor ? Pas d'oseil pas de soin ! Y'a pas de couverture sociale ici !")
                            
                            elif choix_achat == "3" and heros.niv >= 10:
                                if heros.gold >= 200:
                                    heros.gold -= 200
                                    potion1.Looter(heros)
                                    input("Vous achetez une potion de soin supérieure contre 200 po")
                                else:
                                    input("T'essayes de m'arnaquez pécor ? Pas d'oseil pas de soin ! Y'a pas de couverture sociale ici !")

                            elif choix_achat == "e":
                                acheter = False
                    
                    # Vendre
                    elif choix_shop == "2":
                        vendre = True
                        while vendre:
                            clear()
                            for i in heros.new_inventaire["Armes"]:
                                heros.inventaire.append(i)
                            for i in heros.new_inventaire["Têtes"]:
                                heros.inventaire.append(i)
                            for i in heros.new_inventaire["Torses"]:
                                heros.inventaire.append(i)
                            for i in heros.new_inventaire["Epaules"]:
                                heros.inventaire.append(i)
                            for i in heros.new_inventaire["Jambières"]:
                                heros.inventaire.append(i)
                            for i in heros.new_inventaire["Gants"]:
                                heros.inventaire.append(i)
                            for i in heros.new_inventaire["Pieds"]:
                                heros.inventaire.append(i)
                            for i in heros.new_inventaire["Ceintures"]:
                                heros.inventaire.append(i)
                            
                            if len(heros.inventaire) == 0:
                                input("Vous n'avez rien à vendre")
                                vendre = False
                            
                            else:
                                print("Que voulez-vous vendre ?")
                                j = 0
                                for i in heros.inventaire:
                                    j += 1
                                    print(j, "-", i.nom, "prix de vente :", i.gold, "po")
                                print("\n\"e\" pour quitter\n")
                                select_item = input("Quel item voulez-vous vendre ?\n")
                                if select_item == "e":
                                    vendre = False
                                    heros.inventaire = []
                                    break

                                while not check_int(select_item):
                                    if select_item == "e":
                                        vendre = False
                                        heros.inventaire = []
                                        break
                                    else:
                                        select_item = input("Quel item voulez-vous vendre ?\n")
                                select_item = int(select_item)
                                print("Vendre", heros.inventaire[select_item-1].nom, "contre", heros.inventaire[select_item-1].gold, "po ? \"y\" pour confirmer")
                                validation = input("> ")
                                if validation == "y":
                                    clear()
                                    print("Vous gagnez", heros.inventaire[select_item-1].gold)
                                    heros.gold += heros.inventaire[select_item-1].gold
                                    item_vendu = heros.inventaire[select_item - 1]
                                    heros.inventaire.remove(item_vendu)
                                    heros.new_inventaire[item_vendu.type_item].remove(item_vendu)
                                    input("Item vendu !")

                                
                    # Quitter
                    elif choix_shop == "e":
                        clear()
                        input("Vous quittez le Shop")
                        shop = False

            # Guilde
            elif choix_menu_ville == "3":
                # Condition d'entrée
                continuer = True
                while continuer:
                    if heros.niv < 5:
                        clear()
                        print("Groumppf !\n")
                        input("Vous ne semblez pas encore la bienvenue ici...\n")
                        input("On vous fait comprendre qu'il faut partir...")
                        continuer = False

                    else:
                        clear()
                        print("Vous êtes à la guilde")
                        print("Vous apercevez :")
                        j = 0
                        for i in lieu3.occupant:
                            j +=1
                            print(j, "-", i.nom)
                        choix_pnj = input("A qui voulez-vous parler ?\ne pour exit\n")

                        # Soldat
                        if choix_pnj == "1":
                            clear()
                            input("Que désirez-vous Aventurier ?")

                        # Quitter Guilde     
                        elif choix_pnj == "e":
                            clear()
                            input("Vous quittez la Guilde")
                            continuer = False
                        
            
            # Quitter ville        
            elif choix_menu_ville == "4":
                # Choix map
                clear()
                print("Vous quittez la ville")
                print("Où voulez-vous aller ?")
                j = 0
                for i in liste_map:
                    j += 1
                    print(j, "-", i.nom)
                choix_map = input()

                if choix_map == "1":
                    heros.Move(map1)
                    choix = ""
                    break
                elif choix_map == "2":
                    heros.Move(map2)
                    choix = ""
                    break
                elif choix_map == "3":
                    heros.Move(map3)
                    choix = ""
                    break

if heros.Vivant() == False:
    print("Votre \"histoire\" s'arrête ici...")