class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def move(self):
        print(f"{self.name} is moving.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        print(f"{self.name} says Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):
        print(f"{self.name} says Meow!")

    def scratch(self):
        print(f"{self.name} is scratching the post.")

#
# class Animal:
#     def speak(self):
#         print("The animal speaks.")
#
#     def move(self):
#         print("The animal moves.")
#
# # Dog inherits Animal without overriding methods
# class Dog(Animal):
#     pass
#
# # Creating an instance of Dog
# dog = Dog()
# dog.speak()  # Output: The animal speaks.
# dog.move()   # Output: The animal moves.
#
