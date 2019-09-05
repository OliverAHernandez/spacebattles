
class Ammunition:
    def __init__(self,ammo_speed, ammo_image,ammo_size, ammo_damage):
        self.ammo_speed = ammo_speed
        self.ammo_image = ammo_image
        self.ammo_size = ammo_size
        self.ammo_damage = ammo_damage

    def increaseFire(self):
        return 2 * self.ammo_speed

    def tripleFire(self):
        bullet1,bullet2,bullet3 = self.ammo_image
        return(bullet1,bullet2,bullet3)


    def laser(self):
        self.ammo_image = "insert lazer image"
        self.ammo_damage = "max damage"
        self.ammo_speed = 'changed'


