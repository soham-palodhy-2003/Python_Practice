# Multilevel Inheritence = Inherits from a parent which inherits from another parent class

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating") 

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal): # Multiple Inheritence = Inherits from more than one parent class
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Desert")
fish = Fish("Moana")

hawk.sleep()