from personnage import *
from profession import *
from objet import *
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
arme1 = Objet("épée rouillée", 10, 0, 0, 10)
arme2 = Objet("épée solide", 20, 0, 0, 20)
arme3 = Objet("épée tranchante", 30, 0, 0, 30)
arme4 = Objet("épee qui-en-jette", 50, 0, 0, 50)

    # armures
        # tête
tete1 = Objet("chapeau de paille", 0, 10, 0, 10)
tete2 = Objet("bonnet en cuir", 0, 20, 0, 20)
tete3 = Objet("heaume", 0, 30, 0, 30)
tete4 = Objet("heaume enchanté", 0, 50, 0, 50)

        # torse
torse1 = Objet("gilet de fortune", 0, 10, 0, 10)
torse2 = Objet("armure de cuir", 0, 20, 0, 20)
torse3 = Objet("armure en plaque", 0, 30, 0, 30)
torse4 = Objet("armure en plaque enchantée", 0, 50, 0, 50)

        # jambe
jambe1 = Objet("pantalon déchiré", 0, 10, 0, 10)
jambe2 = Objet("jambière en cuir", 0, 20, 0, 20)
jambe3 = Objet("jambière en plaque", 0, 30, 0, 30)
jambe4 = Objet("jambière en plaque enchantée", 0, 50, 0, 50)

        # pied
pied1 = Objet("simple botines", 0, 10, 0, 10)
pied2 = Objet("bottes en cuir", 0, 20, 0, 20)
pied3 = Objet("bottes lourdes", 0, 30, 0, 30)
pied4 = Objet("bottes en plaque enchantées", 0, 50, 0, 50)

        # main
gant1 = Objet("mitaines", 0, 10, 0, 10)
gant2 = Objet("gants en cuir", 0, 20, 0, 20)
gant3 = Objet("gants en plaque", 0, 30, 0, 30)
gant4 = Objet("gants en plaque enchantés", 0, 50, 0, 50)

        # epaule
epaule1 = Objet("epaules de tissu", 0, 10, 0, 10)
epaule2 = Objet("épaule en cuir", 0, 20, 0, 20)
epaule3 = Objet("épaule en plaque", 0, 30, 0, 30)
epaule4 = Objet("épaule en plaque enchanté", 0, 50, 0, 50)

        # ceinture
ceinture1 = Objet("ceinture simple", 0, 10, 0, 10)
ceinture2 = Objet("ceinture en cuir", 0, 20, 0, 20)
ceinture3 = Objet("ceinture en plaque", 0, 30, 0, 30)
ceinture4 = Objet("ceinture en plaque enchanté", 0, 50, 0, 50)

    #potions
potion1 = Potion("potion de soin de base", 0, 0, 20, 20)
potion2 = Potion("potion de soin moyenne", 0, 0, 50, 50)
potion3 = Potion("potion de soin supérieure", 0, 0, 100, 100)
potion4 = Potion("potion totale", 0, 0, 500, 1000)

##################################################################

# Monstre (self, nom, hp, force, xp, table_butin)
monstre1 = Monstre("sanglier", 30, 5, 10, [arme1, tete1, torse1, jambe1, pied1, gant1, epaule1, ceinture1, potion1])
monstre2 = Monstre("gobelin", 40, 10, 20, [arme2, tete2, torse2, jambe2, pied2, gant2, epaule2, ceinture2, potion2])
monstre3 = Monstre("orc", 60, 30, 40, [arme3, tete3, torse3, jambe3, pied3, gant3, epaule3, ceinture3, potion3])

# Boss (self, nom, hp, force, xp, table_butin)
boss1 = Boss("Le Roi gobelin", 200, 50, 100, [tete4, torse4, jambe4, pied4, gant4, epaule4, ceinture4, potion4])

##################################################################

# Description quete
description1 = "Récemment, les sangliers de la région nous empêche de semer pour les futures récoltes.\nIls sont trop nombreux, si vous pouviez y remédier je vous en serai reconnaissant.\nRamenez-moi la preuve que vous vous êtes débarassé de 5 de ces bestiaux et je vous récompenserai."
description2 = "Les gobelins sont à nos portes. \nAventurier, vous semblez apte à faire disparaître cette vermine. \nApportez moi la preuve de 5 gobelin tué et la ville vous récompensera !"
description3 = "Les cadavres s'ammoncèlent. \nOn nous signale la présence d'un orc rodant dans les environ. \nDébarrassez-nous en, vous serez grandement récompensé"

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
dialogue1 = ["Il cherche à s'rincer le gosier le voyageur ?\En quoi je peux vous être utile ?", "Pas de souci voyageur je vous prépare ça fisa !", "Et une pinte pour le voyageur !", "Désolé, la maison ne fait pas crédit !", "C'était un très bon client...\nIl n'a pas survécu, il a malheureusement croisé la route d'une troupe de gobelin ou d'un orc je ne me souviens plus trop.\nLe pauvre n'a pas survécu..."]
dialogue2 = ["Bonjour aventurier, montrez moi vos trouvailles on pourra peut-être faire affaire !"]
dialogue3 = ["Bonjour...", "Effectivement, ça va pas très fort en ce moment...", "Des gobelin ?! J'avais déjà le moral à zéro mais là vous m'achevez ! Va voir ailleurs si j'y suis !", "Merci l'ami !", "Passez une bonne journée..."]
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

