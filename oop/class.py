class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is {self.breed} says woof!")

d1 = Dog("Tommy","Labrador")
d2 = Dog("Bruno", "Pug")

d1.bark()
d2.bark()