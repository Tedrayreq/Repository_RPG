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
from Potion import *
from monstre import *
from quete import *
from map import *
from boss import *
from lieu import *
from ville import *
from pnj import *

#############################################################

# Profession (self, nom, bonushp, bonusforce)
peon = Profession("péon", 0, 0)
agriculteur = Profession("agriculteur", 50, 0)
artisan = Profession("artisan", 0, 10)

##############################################################

# Objet (self, nom, type, dgts, heal, gold)
    # armes
arme1 = Arme("épée rouillée", 10, 0, 0, 10)
arme2 = Arme("\033[32mépée solide\033[37m", 20, 0, 0, 20)
arme3 = Arme("\033[36mépée tranchante\033[37m", 30, 0, 0, 30)
arme4 = Arme("\033[35mépee qui-en-jette\033[37m", 50, 0, 0, 50)

    # armures
        # tête
tete1 = Tete("chapeau de paille", 0, 10, 0, 10)
tete2 = Tete("\033[32mbonnet en cuir\033[37m", 0, 20, 0, 20)
tete3 = Tete("\033[36mheaume\033[37m", 0, 30, 0, 30)
tete4 = Tete("\033[35mheaume enchanté\033[37m", 0, 50, 0, 50)

        # torse
torse1 = Torse("gilet de fortune", 0, 10, 0, 10)
torse2 = Torse("\033[32marmure de cuir\033[37m", 0, 20, 0, 20)
torse3 = Torse("\033[36marmure en plaque\033[37m", 0, 30, 0, 30)
torse4 = Torse("\033[35marmure en plaque enchantée\033[37m", 0, 50, 0, 50)

        # jambe
jambe1 = Jambiere("pantalon déchiré", 0, 10, 0, 10)
jambe2 = Jambiere("\033[32mjambière en cuir\033[37m", 0, 20, 0, 20)
jambe3 = Jambiere("\033[36mjambière en plaque\033[37m", 0, 30, 0, 30)
jambe4 = Jambiere("\033[35mjambière en plaque enchantée\033[37m", 0, 50, 0, 50)

        # pied
pied1 = Pied("simple botines", 0, 10, 0, 10)
pied2 = Pied("\033[32mbottes en cuir\033[37m", 0, 20, 0, 20)
pied3 = Pied("\033[36mbottes lourdes\033[37m", 0, 30, 0, 30)
pied4 = Pied("\033[35mbottes en plaque enchantées\033[37m", 0, 50, 0, 50)

        # main
gant1 = Gant("mitaines", 0, 10, 0, 10)
gant2 = Gant("\033[32mgants en cuir\033[37m", 0, 20, 0, 20)
gant3 = Gant("\033[36mgants en plaque\033[37m", 0, 30, 0, 30)
gant4 = Gant("\033[35mgants en plaque enchantés\033[37m", 0, 50, 0, 50)

        # epaule
epaule1 = Epaule("epaules de tissu", 0, 10, 0, 10)
epaule2 = Epaule("\033[32mépaule en cuir\033[37m", 0, 20, 0, 20)
epaule3 = Epaule("\033[36mépaule en plaque\033[37m", 0, 30, 0, 30)
epaule4 = Epaule("\033[35mépaule en plaque enchanté\033[37m", 0, 50, 0, 50)

        # ceinture
ceinture1 = Ceinture("ceinture simple", 0, 10, 0, 10)
ceinture2 = Ceinture("\033[32mceinture en cuir\033[37m", 0, 20, 0, 20)
ceinture3 = Ceinture("\033[36mceinture en plaque\033[37m", 0, 30, 0, 30)
ceinture4 = Ceinture("\033[35mceinture en plaque enchanté\033[37m", 0, 50, 0, 50)

    #potions
potion1 = Potion("potion de soin de base", 0, 0, 20, 20)
potion2 = Potion("\033[32mpotion de soin moyenne\033[37m", 0, 0, 50, 50)
potion3 = Potion("\033[36mpotion de soin supérieure\033[37m", 0, 0, 100, 100)
potion4 = Potion("\033[35mpotion totale\033[37m", 0, 0, 500, 1000)

##################################################################

# Monstre (self, nom, hp, force, xp, table_butin)
monstre1 = Monstre("sanglier", 30, 5, 10, [arme1, tete1, torse1, jambe1, pied1, gant1, epaule1, ceinture1, potion1])
monstre2 = Monstre("gobelin", 40, 10, 20, [arme2, tete2, torse2, jambe2, pied2, gant2, epaule2, ceinture2, potion2])
monstre3 = Monstre("orc", 60, 30, 40, [arme3, tete3, torse3, jambe3, pied3, gant3, epaule3, ceinture3, potion3])

# Boss (self, nom, hp, force, xp, table_butin)
boss1 = Boss("Le Roi gobelin", 200, 50, 100, [tete4, torse4, jambe4, pied4, gant4, epaule4, ceinture4, potion4])

##################################################################

# Description quete
description1 = "Pour tout vous dire, récemment les sangliers de la région nous empêchent de semer pour les futures récoltes.\nIls sont trop nombreux, si vous pouviez y remédier je vous en serai reconnaissant.\nRamenez-moi la preuve que vous vous êtes débarassé de 5 de ces bestiaux et je vous récompenserai.\n"
description2 = "Les gobelins sont à nos portes. \nAventurier, vous semblez apte à faire disparaître cette vermine. \nApportez moi la preuve de 5 gobelin tué et la ville vous récompensera !\n"
description3 = "Les cadavres s'ammoncèlent... \nOn nous signale la présence d'un orc rodant dans les environ. \nDébarrassez-nous en, vous serez grandement récompensé !\n"

# Quete (self, nom, description, xp, gold, monstre, combien)
quete1 = Quete("Un risque à écarter", description1, 100, 100, monstre1, 5)
quete2 = Quete("Il est grand temps de faire le ménage !", description2, 200, 400, monstre2, 5)
quete3 = Quete("Un défi à la hauteur de votre réputation !", description3, 500, 1000, monstre3, 1)

##################################################################

# Map (self, nom, niv_min, niv_max, bestiaire)
map1 = Map("La forêt", 1, 5, [monstre1, monstre2, monstre3])
map2 = Map("La grotte sombre", 5, 10, [monstre2, monstre3])
map3 = Map("Les ruines", 10, 15, [monstre3, boss1])
liste_map = [map1, map2, map3]

###################################################################

# Dialogue pnj
dialogue1 = ["Il cherche à s'rincer le gosier le voyageur ?\nEn quoi je peux vous être utile ?\n",
                "Pas de souci voyageur je vous prépare ça fisa !\n", "Et une pinte pour le voyageur !\n",
                "Désolé, la maison ne fait pas crédit !\n",
                "C'était un très bon client...\nIl n'a pas survécu, il a malheureusement croisé la route d'une troupe de gobelin ou d'un orc je ne me souviens plus trop.\nLe pauvre n'a pas survécu..."]
dialogue2 = ["Bonjour aventurier, montrez moi vos trouvailles on pourra peut-être faire affaire !"]
dialogue3 = ["\nBonjour...\n", "\nEffectivement, ça va pas très fort en ce moment...\n",
                "\nDes gobelin ?! J'avais déjà le moral à zéro mais là vous m'achevez ! Va voir ailleurs si j'y suis !\n",
                "\nMerci l'ami !\n", "\nPassez une bonne journée...\n"]
dialogue4 = []

# Pnj (self, nom, position)
pnj1 = Pnj("Tavernier", dialogue1)
pnj2 = Pnj("Vendeur", dialogue2)
pnj3 = Pnj("Fermier", dialogue3)
pnj4 = Pnj("Garde", dialogue4)

###################################################################

# Lieu (self, nom, occupant)
lieu1 = Lieu("Taverne", [pnj1, pnj3])
lieu2 = Lieu("Shop", [pnj2])
lieu3 = Lieu("Guilde", [pnj4])

# Ville (self, nom, lieu)
ville1 = Ville("Petit-Village", [lieu1, lieu2, lieu3])

