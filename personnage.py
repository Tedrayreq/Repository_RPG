from profession import *

class Personnage:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.profession = Profession("péon", 0, 0)
        self.hp = 100
        self.current_hp = 100
        self.xp = 0
        self.niv = 1
        self.force = 20
        self.inventaire = []
        self.new_inventaire = {"Items": [], "Potions":[], "Armes":[], "Têtes": [], "Epaules": [], 
                               "Torses": [], "Gants": [], "Jambières": [], "Pieds": [], "Ceintures": []}
        self.stuff = {"Armes": [], "Têtes": [], "Epaules": [], "Torses": [], "Gants": [], 
                      "Jambières": [], "Pieds": [], "Ceintures": []}
        self.equiper = []
        self.vivant = True
        self.position = ""
        self.quetes = []
        self.gold = 0
    
    def Gain_stats_objet(self, objet):
        self.force += objet.dgts
        self.hp += objet.hp

    def Perte_stats_objet(self, objet):
        self.force -= objet.dgts
        self.hp -= objet.hp


    # def Equiper_objet(self, objet):
    #     self.equiper.append(objet)
    #     self.inventaire.remove(objet)
    #     self.force += objet.dgts
    #     self.hp += objet.hp


    # def Ranger_objet(self, objet):
    #     self.inventaire.append(objet)
    #     self.equiper.remove(objet)
    #     self.force -= objet.dgts
    #     self.hp -= objet.hp

    # def Gagner_objet(self, objet):
    #     self.inventaire.append(objet)


    # def Perdre_objet(self,objet):
    #     self.inventaire.remove(objet)


    def Choix_profession(self, profession):
        self.profession = str(profession)


    def Gain_xp(self, montant):
        self.xp += montant
        if self.xp == self.niv*100:
            return True


    def Level_up(self):
        if self.xp >= self.niv*100:
            ecart = self.xp - self.niv*100
            self.niv += 1
            self.xp = 0
            self.xp += ecart
            self.hp += 10
            self.force += 5
            self.current_hp = self.hp
            print("\033[34m--------------------")
            print("Vous gagnez un niv !")
            print("--------------------\033[37m")


    def Afficher_gold(self):
        print("Vous avez actuellement :", self.gold, "pièces d'or\n")

    
    def Afficher_inventaire(self):
        if len(self.inventaire) == 0:
            print("L'inventaire est vide\n")
        else:
            for i in self.inventaire:
                print(i.nom)


    def Afficher_equiper(self):
        if len(self.equiper) == 0:
            print("Vous n'avez rien d'équipé\n")
        else:
            for i in self.equiper:
                print(i.nom)

    
    def Afficher_quetes(self):
        check = False
        for i in self.quetes:
            if i.active:
                check = True
                print("Quête :", i.nom)
                print("\nDescription :\n", i.description)
                print("\nRécompenses :\nxp :", i.xp, "\nGold :", i.gold, "pièces d'or")
                print("\nSuivi :\nTuer", i.combien, i.monstre.nom)
                print("Actuellement :", i.compteur_kill, "/", i.combien)
                if i.Kill():
                    print("Vous pouvez rendre cette quete")
        if not check:
            print("Vous n'avez pas de quête")

    
    def Prendre_quete(self, quete):
        self.quetes.append(quete)


    def Rendre_quete(self, quete):
        if quete.done:
            self.Gain_xp(quete.xp)
            self.Level_up()
            self.gold += quete.gold
            quete.rendue = True
            print("Vous gagnez:\n", self.quetes[0].xp, "xp et", self.quetes[0].gold, "po")
            input()


    def Perdre_hp(self, montant):
        self.current_hp -= montant

    
    def Gagner_hp(self, montant):
        if self.current_hp + montant > self.hp:
            self.current_hp = self.hp
        else:
            self.current_hp += montant


    def Afficher_current_hp(self):
        print("Vous avez :", self.current_hp, "hp restant.")
    

    def Afficher_stats(self):
        print(self.pseudo, "de niv:", self.niv, "               ","HP:", self.current_hp, "/", self.hp)
        print("xp:", self.xp, "/", (self.niv*100))
        print("\nforce", self.force)


    def Vivant(self):
        if self.current_hp <= 0:
            self.vivant = False
        return self.vivant


    def Move(self, position):
        self.position = position