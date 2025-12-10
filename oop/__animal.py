# base class
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."


# derived classes
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Mouse(Animal):
    def speak(self):
        return "Squeak!"


dog = Dog("Caesar")
cat = Cat("Tom")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.sleep())
print(dog.speak())

print(cat.name)
print(cat.sleep())
print(cat.speak())

print(mouse.name)
print(mouse.eat())
print(mouse.speak())
