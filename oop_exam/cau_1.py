from abc import ABC, abstractmethod


class Animal(ABC):
    # Initialize
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def display_info(self):
        pass


class Lion(Animal):
    def __init__(self, name, age, pride_size):
        super().__init__(name, age)
        self.__pride_size = pride_size

    @property
    def pride_size(self):
        return self.__pride_size

    @pride_size.setter
    def pride_size(self, pride_size):
        self.__pride_size = pride_size

    def make_sound(self):
        return "Roar"

    def display_info(self):
        print(f"Lion Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Pride Size: {self.pride_size}")
        print(f"Sound: {self.make_sound()}")


class Elephant(Animal):
    def __init__(self, name, age, trunk_length):
        super().__init__(name, age)
        self.__trunk_length = trunk_length

    @property
    def trunk_length(self):
        return self.__trunk_length

    @trunk_length.setter
    def trunk_length(self, trunk_length):
        self.__trunk_length = trunk_length

    def make_sound(self):
        return "Trumpet"

    def display_info(self):
        print(f"Elephant Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Trunk Length: {self.trunk_length} meters")
        print(f"Sound: {self.make_sound()}")


def print_animal_info(animal):
    if isinstance(animal, Animal):
        animal.display_info()
    else:
        print("The provided object is not an Animal.")


simba = Lion(name="Simba", age=5, pride_size=10)

dumbo = Elephant(name="Dumbo", age=8, trunk_length=2.5)

print_animal_info(simba)
print_animal_info(dumbo)

