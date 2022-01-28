class Monstre:
    def __init__(self, nom, hp, force, xp, table_butin):
        self.nom = nom
        self.hp = hp
        self.current_hp = hp
        self.force = force
        self.niv = 1
        self.xp = xp
        self.table_butin_init = table_butin
        self.table_butin = self.table_butin_init
        self.vivant = True

    def Perdre_hp(self, montant):
        self.current_hp -= montant

    
    def Vivant(self):
        if self.current_hp <= 0:
            self.vivant = False
        return self.vivant


    def Restart(self):
        if self.vivant == False:
            self.hp -= self.niv*10
            self.current_hp = self.hp
            self.force -= self.niv*2
            self.niv = 1
            self.table_butin = self.table_butin_init
            self.vivant = True

