from objet import *

class Potion(Objet):
    def __init__(self, nom, dgts, hp, heal, gold):
        super().__init__(nom, dgts, hp, heal, gold)
        self.nom = nom
        self.dgts = dgts
        self.hp = 0
        self.heal = heal
        self.gold = gold

    def Utiliser(self, personnage):
        personnage.current_hp += self.hp
        print("Vous utilisez une", self.nom, ", vous récupérez", self.heal, "hp")

    def Ranger(self, personnage):
        personnage.new_inventaire["potion"].append()

    def Afficher(self, personnage):
        for i in personnage.new_inventaire["potion"]:
            print(self.nom)