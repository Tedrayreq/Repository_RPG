from random import randint

from personnage import *
from profession import *
from objet import *
from monstre import *
from quete import *
from map import *
from boss import *
from pnj import *
from ville import *
from lieu import *
from functions import *

# Création héros
pseudo = input("Quel est ton nom ?\n")
print("Bon courage", pseudo, "\n")
heros = Personnage(pseudo)
heros.position = map1
heros.quetes = [quete1, quete2, quete3]
heros.Gagner_objet(arme1)
heros.Equiper_objet(arme1)
heros.gold = 100
choix = ""
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

            # Alea niv monstre
            rand_niv_monstre = randint(heros.position.niv_min, heros.position.niv_max)
            monstre.niv = rand_niv_monstre
            monstre.hp += monstre.niv*10
            monstre.current_hp = monstre.hp
            monstre.force += monstre.niv*2
            combat(heros, monstre)
        
            if heros.Vivant():
                continuer = input("Continuer ? \"n\" pour arrêter\n")
                if continuer == "n":
                    continuer_combat = False
            else:
                print("...")

    # Afficher stats
    elif choix == "2":
        clear()
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
        print("INVENTAIRE\n")
        heros.Afficher_inventaire()
        print("\nACTUELLEMENT EQUIPE\n")
        heros.Afficher_equiper()
        #sous_menu_inventaire(personnage, choix)
        input("\nentrer pour exit")

    # Ville
    elif choix == "5":
        clear()
        input("Vous retournez en ville")
        # personnage.Move(ville1)
        #menu_ville(personnage, personnage.position)
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
                        input("Vous saluez le", pnj1.nom)
                        continuer = True
                        while continuer:
                            menu_tavernier()
                            dialogue = input()
                            if dialogue == "1":
                                if heros.gold >= 20:
                                    input(pnj3.dialogue[1])
                                    heros.gold -= 20
                                    input("Vous payez 20po votre chambre et passez une bonne nuit de sommeil !")
                                    heros.current_hp = heros.hp
                                else:
                                    input(pnj3.dialogue[3])

                            elif dialogue == "2":
                                if heros.gold >= 10:
                                    input(pnj3.dialogue[2])
                                    heros.gold -= 10
                                    heros.current_hp += 10
                                    input("Rien de tel qu'une bonne bière !")
                                else:
                                    input(pnj3.dialogue[3])


                            elif dialogue == "3" and not pnj3 in lieu1.occupant:
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
                                heros.Gagner_objet(arme4)
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