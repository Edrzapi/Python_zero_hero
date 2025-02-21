class Vehicle:
    def __init__(self, mot: bool):
        self.mot = mot


class Car(Vehicle):
    # Further learning - GC: Garbage Collection
    def __init__(self, make: str, model: str, milage: int, year: int, mot: bool):
        super().__init__(mot)
        self.__make = make
        self.__model = model
        self.__milage = milage
        self.__year = year

    def get_year(self):
        return self.__year

    def set_year(self, update_year):
        self.__year = update_year

    def get_make(self):
        return self.__make

    def set_make(self, update_make):
        self.__make = update_make

    def get_model(self):
        return self.__model

    def set_model(self, update_model):
        self.__model = update_model

    def get_milage(self):
        return self.__milage

    def set_milage(self, update_milage):
        self.__milage = update_milage

    def __str__(self) -> str:
        return f'Make: {self.__make}, Model: {self.__model}, Milage: {self.__milage}, Year: {self.__year}, MOT Status: {self.mot}'


my_car = Car("Toyota", "mr2", 1990, 95000, False)
irfan_car = Car("Honda", "Civic", 2008, 100000, True)
harry_car = Car("Honda", "c220", 2015, 90000, True)
# harry_car.make = "Iveco" - not cool, pretty unsafe in a wider application
print(harry_car.get_make())  # use a get/setter to access variables, far safer!
print(harry_car)
