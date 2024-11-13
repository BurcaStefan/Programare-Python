class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Nume: {self.name}, Ani: {self.age}")

    def make_sound(self):
        pass

    def move(self):
        pass

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Ham/Miau"

    def move(self):
        return "Merge"

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Chirp"

    def move(self):
        return "Zboara"

class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type

    def make_sound(self):
        return "Blub"

    def move(self):
        return "Inoata"
    
mammal = Mammal("Caine", 5, "Negru")
print(mammal.display())
print(mammal.make_sound())
print(mammal.move())

bird = Bird("Colibri", 2, 10)
print(bird.display())
print(bird.make_sound())
print(bird.move())

fish = Fish("Nemo", 1, "Dulce")
print(fish.display())
print(fish.make_sound())
print(fish.move())