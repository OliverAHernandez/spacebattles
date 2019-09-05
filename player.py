class Player():
    def __init__(self, name, movement, health):
        self.name = name
        self.movement = movement
        self.health = health
    def Movement(self):
        if self.movement == "up".lower():
            return 1
        else:
            return 2
    def Health(self):
        if DamageTaken:
            self.health -= 1
            print("{0} has {1} lives left".format(self.name,self.health))
        if self.health == 0:
            print("{} Has Been Eliminated".format(self.name))
        return self.health


#Code Testing
"""player1 = Player("player1", "up",3)
player2 = Player("player2", "down",3)
print(player1.Movement())
print(player2.Movement())
print("\t")
for i in range(3):
    DamageTaken = True
    player1.Health()"""
