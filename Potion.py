from objet import *

class Potion(Objet):
    def __init__(self, nom, dgts, hp, heal, gold):
        super().__init__(nom, dgts, hp, heal, gold)
        self.nom = nom
        self.type_item = "Potions"
        self.dgts = dgts
        self.hp = 0
        self.heal = heal
        self.gold = gold

    def Utiliser(self, personnage):
        personnage.current_hp += self.hp
        if personnage.current_hp > personnage.hp:
            personnage.current_hp = personnage.hp
        personnage.new_inventaire["Potions"].remove(self)
        print("Vous utilisez une", self.nom, ", vous récupérez", self.heal, "hp")

    # à supprimer si check hérédité de class objet good
    # def Ranger(self, personnage):
    #     personnage.new_inventaire["Potions"].append()

    def Afficher(self, personnage):
        for i in personnage.new_inventaire["Potions"]:
            print(self.nom)
            # Ajouter compteur potions puis tri et affichage en mode :
            # potion_type1 x3
            # potion_type2 x5
            # etc.