from abc import ABC, abstractmethod


class Vehicle(ABC):  # Vehicle is an abstract class, inheriting from ABC
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass  # Abstract method, must be implemented by subclasses

    @abstractmethod
    def stop_engine(self):
        pass  # Abstract method, must be implemented by subclasses

    @abstractmethod
    def honk(self):
        pass  # Abstract method, must be implemented by subclasses


class Car(Vehicle):  # Car is a subclass of
    __count = 0

    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
        Car.__count += 1

    @classmethod
    def get_car_count(cls):
        return cls.__count

    def start_engine(self):
        print(f"The engine of the {self.make} {self.model} car is starting.")

    def stop_engine(self):
        print(f"The engine of the {self.make} {self.model} car is stopping.")

    def honk(self):
        print(f"The {self.make} {self.model} car honks: Beep beep!")


my_car = Car("Toyota", "t", 4)
irfan_car = Car("Honda", "t", 4)
harry_car = Car("Honda", "t", 4)
print(Car.get_car_count())


class Truck(Vehicle):  # Truck is a subclass of Vehicle
    def __init__(self, make, model, load_capacity):
        super().__init__(make, model)
        self.load_capacity = load_capacity

    def start_engine(self):
        print(f"The engine of the {self.make} {self.model} truck is starting with a roar.")

    def stop_engine(self):
        print(f"The engine of the {self.make} {self.model} truck is stopping.")

    def honk(self):
        print(f"The {self.make} {self.model} truck honks loudly: HONK HONK!")
