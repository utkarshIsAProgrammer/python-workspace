# duck typing polymorphism


class Duck:
    def fly(self):
        print("Duck flying")


class Airplane:
    def fly(self):
        print("Airplane flying")


def start_flying(thing):
    thing.fly()


start_flying(Duck())
start_flying(Airplane())
