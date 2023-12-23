class Creature:
    
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("i can eat")
    
class SwimmerInterface:    
    def swim(self):
        print("I can Swim")
        
class WalkerInterface:     
    
    def walk(self):
        print("I can Walk")
class TalkerInterface:       
    def talk(self):
        print("I can talk")

class Human(Creature, SwimmerInterface, WalkerInterface, TalkerInterface):
    pass

class Fish(Creature, SwimmerInterface):
    pass

class Snake(Creature):
    pass


fish = Fish("skumbria")
javohir = Human("Javohir")
snake = Snake("Python")

snake.eat()

javohir.walk()
javohir.swim()
javohir.talk()

fish.eat()
fish.swim()