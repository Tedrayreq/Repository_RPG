class Boss:
    def __init__(self, nom, hp, force, xp, table_butin):
        self.nom = nom
        self.hp = hp
        self.current_hp = self.hp
        self.force = force
        self.xp = xp
        self.table_butin = table_butin