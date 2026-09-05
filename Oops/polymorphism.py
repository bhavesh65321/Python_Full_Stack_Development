#Polymorphism Implementation ##
## Poly means many and morphism means form

class Animal:
    def __init__(self,name : str) -> None:
        self.name : str = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} is meowing")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.make_sound()
cat.make_sound()