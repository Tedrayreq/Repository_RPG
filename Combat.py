from random import randint

class Combat():
    def __init__(self, personnage, monstre):
        self.personnage = personnage
        self.monstre = monstre
        self.fuite = False
        self.tour = 0

    # display
    def clear(self):
        print("\033[H\033[J", end="")

    def Ouverture(self):
        self.clear()
        print("--------------------------------------------")
        print("Vous affrontez ", self.monstre.nom, "de niv :", self.monstre.niv)
        print("Vous avez :", self.personnage.current_hp,"hp")
        print("Le monstre a :", self.monstre.current_hp,"hp")
        input("--------------------------------------------")

    def menu_combat(self):
        self.clear()
        print("Vos PV :", self.personnage.current_hp, "/", self.personnage.hp, 
              "              ", 
              self.monstre.nom, "de niv", self.monstre.niv, "PV restant :", self.monstre.current_hp, "/", self.monstre.hp,
              "\n\nQue voulez-vous faire ?\n"
              "1 - Attaquer\n"
              "2 - Utiliser une compétence\n"
              "3 - Utiliser objet\n"
              "4 - Tenter de fuir")

    def Over(self):
        if not self.personnage.Vivant() or not self.monstre.Vivant() or self.fuite:
            return True
        else:
            return False

    def Alea_niv_monstre(self):
        rand_niv_monstre = randint(self.personnage.position.niv_min, self.personnage.position.niv_max)
        self.monstre.niv = rand_niv_monstre
        self.monstre.hp += self.monstre.niv*10
        self.monstre.current_hp = self.monstre.hp
        self.monstre.force += self.monstre.niv*2

    # Calcul dgts
    def Dgt_attaque_personnage(self):
        self.clear()
        luck_personnage = randint(1, 100)
        coef_attaque_personnage = 1
        print("Vous faites un", luck_personnage)
        if luck_personnage <= 10:
            print("Aie, vous glissez pendant votre attaque et vous fracassez au sol...")
            coef_attaque_personnage = 0
        
        elif 10 < luck_personnage <= 20:
            print("Vous manquez tomber et portez votre attaque du bout de votre épée !")
            coef_attaque_personnage = 0.5

        elif 20 < luck_personnage <= 80:
            print("Vous portez votre attaque !")

        elif 80 < luck_personnage <= 90:
            print("Votre attaque frôle la perfection !")
            coef_attaque_personnage = 1.5

        elif 90 < luck_personnage <= 100:
            print("Votre attaque fend l'air et s'abat avec fracas sur votre ennemi : magnifique !")
            coef_attaque_personnage = 2
        
        dgts_personnage = (self.personnage.force + self.personnage.niv) * coef_attaque_personnage
        print("Votre attaque inflige ", dgts_personnage, " hp au monstre adverse")
        self.monstre.Perdre_hp(dgts_personnage)
        self.tour += 1

    def Dgt_attaque_monstre(self):
        self.clear()
        luck_monstre = randint(1, 100)
        coef_attaque_monstre = 1
        if self.monstre.current_hp > 0:
            print("Le monstre fait un", luck_monstre)
            if luck_monstre <= 10:
                print("Le monstre va pour vous porter un coup, trébuche et s'écrase au sol !")
                coef_attaque_monstre = 0

            elif 10 < luck_monstre <= 20:
                print("Le monstre trébuche et vous effleure !")
                coef_attaque_monstre = 0.5

            elif 20 < luck_monstre <= 80:
                print("Le monstre vous attaque !")

            elif 80 < luck_monstre <= 90:
                print("L'attaque du monstre va faire mal, attention !")
                coef_attaque_monstre = 1.5

            elif 90 < luck_monstre <= 100:
                print("Vous sentez la puissance du coup que le monstre vous a porté, la douleur est insoutenable...")
                coef_attaque_monstre = 2
            
            dgts_monstre = (self.monstre.force + self.monstre.niv) * coef_attaque_monstre
            print("L'attaque du monstre vous fait perdre ", dgts_monstre, " hp")
            self.personnage.Perdre_hp(dgts_monstre)

        else:
            coef_attaque_monstre = 0
        self.tour += 1

    def Action_personnage(self):
        self.clear()
        self.menu_combat()
        choix_menu = input("> ")
        if choix_menu == "1":
            self.Dgt_attaque_personnage()
            input()

        elif choix_menu == "2":
            input("Pas encore dispo deso pas deso xP")
        
        elif choix_menu == "3":
            input("pas encore config deso pas deso")

        elif choix_menu == "4":
            fuite = randint(1, 100)
            if fuite > 70:
                self.clear()
                input("Vous prenez la fuite")
                self.fuite = True

            else:
                input("Vous n'arrivez pas à vous échapper")
                self.tour += 1


    def Action_monstre(self):
        # Prévoir attaque ou sort par la suite
        self.Dgt_attaque_monstre()
        input()

    def Fin_combat(self):
        if not self.personnage.Vivant():
            input("Tout devient noir, vous mourrez.")
        elif self.fuite:
            input("...")
        else:
            montant_xp = int(self.monstre.xp) * int(self.monstre.niv)
            self.clear()
            print("---------------------")
            print("Vous êtes victorieux !\nVous gagnez", montant_xp,"xp !")
            print("---------------------\n")
            self.personnage.Gain_xp(montant_xp)
            self.personnage.Level_up()
            rand_table_loot = randint(0, (len(self.monstre.table_butin)-1))
            #self.personnage.Gagner_objet(self.monstre.table_butin[rand_table_loot])
            self.monstre.table_butin[rand_table_loot].Looter(self.personnage)
            print("Vous trouvez :",self.monstre.table_butin[rand_table_loot].nom,"sur le monstre !")
            for i in self.personnage.quetes:
                if i.active and not i.done:
                    i.Kill()

            input()
        self.monstre.Restart()


    # Méthode combat
    def Start_combat(self):
        self.clear()
        self.Alea_niv_monstre()
        self.Ouverture()
        while not self.Over():
            if self.tour%2 == 0:
                self.Action_personnage()
            
            else:
                self.Action_monstre()
            
        self.Fin_combat()