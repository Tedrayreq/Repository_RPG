from Stuff import *

class Torse(Stuff):
    def __init__(self, nom, dgts, hp, heal, gold):
        super().__init__(nom, dgts, hp, heal, gold)
        self.nom = nom
        self.type_item = "Torses"
        self.dgts = dgts
        self.hp = hp
        self.heal = heal
        self.gold = gold