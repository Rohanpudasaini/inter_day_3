# 16. Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

class Mario:
    def __init__(self, name="Mario", health=100, attack= 5, attack_range = 2) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.coin = 0
        self.powerup = []
        self.stamina = 1000
        self.attack_range = attack_range
    
    def move(self,tiles:int):
        if tiles*0.2 <= self.stamina:
            self.stamina -= tiles*0.2
            print(f"Mario moved {tiles} tiles")
        else:
            print("Not enough stamina")
    
    def collect_coin(self, coin):
        self.coin += coin
        print(f"collected {coin}s coin")

    def jump(self,tiles:int):
        if tiles*0.4 <= self.stamina:
            self.stamina -= tiles*0.4
            print(f"Mario jumpped {tiles} tiles")
        else:
            print("Not enough stamina")
    # @classmethod
    def attack_enemy(self, enemy):
        enemy.decrease_health(self.attack)



class Enemy:
    def __init__(self,damage, attack_range, health=100) -> None:
        self.damage = damage
        self.attack_range = attack_range
        self.health = health
    
    def attack(self):
        print(f"The enemy is attacking with {self.damage} damage for {self.attack_range} range, be alert!!")
    
    def decrease_health(self, damage_done):
        self.health -= damage_done
        print(f"{self.health} health remaning")


class Boss(Enemy):
    def __init__(self, damage, attack_range, health=400) -> None:
        super().__init__(damage, attack_range, health)

mario = Mario()
mario.collect_coin(5)
mario.move(5)
mario.jump(5)
enemy1 = Enemy(5,2)
enemy2 = Boss(10,1)
mario.attack_enemy(enemy1)
mario.attack_enemy(enemy2)



