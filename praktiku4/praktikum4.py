class hero:
    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health

    def info(self, tipe):
        print(f"nama = {self, name} \nhealth = {self.health}\ntipe = {tipe}")

class stat_str(hero):
    def __init__(self, name, health):
        super().__init__(name, 100)
        #super.tipe = "strenght"
    def info(self, tipe):
        #super().info("strenght")
        print(f"nama = {self, name} \nhealth = {self.health}\ntipe = {tipe}")

class start_dex(hero):
    def __init__(self, name):
        super().__init__(name)