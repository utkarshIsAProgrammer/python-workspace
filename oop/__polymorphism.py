# simple polymorphism


class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Bark"


class Cat(Animal):
    def speak(self):
        return "Meow"


def make_it_speak(animal):
    print(animal.speak())


pets = [Dog(), Cat(), Animal()]
for pet in pets:
    make_it_speak(pet)
