class Objet:
    def __init__(self, nom, dgts, hp, heal, gold):
        self.nom = nom
        self.type_item = "Items"
        self.dgts = dgts
        self.hp = hp
        self.heal = heal
        self.gold = gold

    def Looter(self, personnage):
        personnage.new_inventaire[self.type_item].append(self)