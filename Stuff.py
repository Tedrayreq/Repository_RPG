from objet import *

class Stuff(Objet):
    def __init__(self, nom, dgts, hp, heal, gold):
        super().__init__(nom, dgts, hp, heal, gold)
        self.nom = nom
        self.type_item = "Stuff"
        self.dgts = dgts
        self.hp = hp
        self.heal = heal
        self.gold = gold

    def Ranger(self, personnage):
        personnage.stuff[self.type_item].remove(self)
        personnage.new_inventaire[self.type_item].append(self)
        personnage.Perte_stats_objet(self)

    def Equiper(self, personnage):
        if len(personnage.stuff[self.type_item]) == 0:
            personnage.stuff[self.type_item].append(self)
            personnage.new_inventaire[self.type_item].remove(self)
            personnage.Gain_stats_objet(self)
            print("Vous équipez", self.nom)
            input()
        else:
            print("Vous avez déjà", personnage.stuff[self.type_item][0].nom,"d'équipé")
            check = input("Voulez-vous le remplacer ? y/n")
            if check == "y":
                ancien = personnage.stuff[self.type_item][0]
                ancien.Ranger(personnage)
                # personnage.stuff[self.type_item].remove(ancien)
                # personnage.Perte_stats_objet(ancien)
                # personnage.new_inventaire[ancien.type_item].append(ancien)
                personnage.stuff[self.type_item].append(self)
                personnage.new_inventaire[self.type_item].remove(self)
                personnage.Gain_stats_objet(self)
                print("Vous équipez", self.nom,"et rangez", ancien.nom,"dans votre inventaire")
                input()
            else:
                print("Vous n'équipez pas", self.nom)
                input()
