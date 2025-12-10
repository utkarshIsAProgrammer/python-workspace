# multiple and multilevel inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bunny")
print(rabbit.name)
rabbit.flee()
rabbit.sleep()

hawk = Hawk("Grok")
print(hawk.name)
hawk.hunt()
hawk.eat()

fish = Fish("Fin")
print(fish.name)
fish.flee()
fish.sleep()
fish.hunt()
fish.eat()
