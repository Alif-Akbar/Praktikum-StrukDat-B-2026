class Traveller:
    def __init__(self, name, vision,  weapon, region):
        self.name = name
        self.vision = vision
        self.weapon = weapon
        self.region = region

    def introduce(self, name, vision, weapon, region):
        print("Perkenalkan," , name , "yang berelemen" , vision , "bersenjata" , weapon , "yang berasal dari", region )

    def call(self, name):
        print("Halo," , name)      

p1 = Traveller("Ali", "Anemo", "Bow", "China")
p2 = Traveller("Rai", "Pyro", "Axe", "Japan")
p3 = Traveller("Ana", "Cryo", "Sword", "Rusia")

p1.name = "Ari"

p1.introduce(p1.name, p1.vision, p1.weapon, p1.region)
p1.call(p1.name)
p2.introduce(p2.name, p2.vision, p2.weapon, p2.region)
p2.call(p2.name)
p3.introduce(p3.name, p3.vision, p3.weapon, p3.region)
p3.call(p3.name)


