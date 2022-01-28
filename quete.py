class Quete:
    def __init__(self, nom, description, xp, gold, monstre, combien):
        self.nom = nom
        self.description = description
        self.xp = xp
        self.gold = gold
        self.monstre = monstre
        self.combien = combien
        self.compteur_kill = 0
        self.done = False
        self.active = False
        self.rendue = False


    def Kill(self):
        if not self.active or self.rendue:
            return False
        elif self.done:
            return True
        elif self.active:
            if not self.monstre.Vivant() and self.compteur_kill < self.combien:
                self.compteur_kill += 1
                if self.compteur_kill == self.combien:
                    self.done = True
                    return True
                else :
                    return False

    def Rendre_quete(self):
        if self.Kill():
            self.rendue = True

    def Afficher_quete(self):
        print("Quête:", self.nom)
        print("\nDescription :", self.description)
        print("\nRécompenses :\nxp :", self.xp, "\nGold :", self.gold, "pièces d'or")
        print("\nSuivi :\nTuer", self.combien, self.monstre.nom)
        print("Actuellement :", self.compteur_kill, "/", self.combien)
