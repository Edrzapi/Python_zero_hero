class Garage:
    def __init__(self):
        self.vehicles = []  # List to store vehicles

    def add_vehicle(self, vehicle):
        """Add a vehicle to the garage."""
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle_id=None, vehicle_type=None):
        """Remove a vehicle by its ID or type."""
        if vehicle_id is not None:
            self.vehicles = [v for v in self.vehicles if v.id != vehicle_id]
        elif vehicle_type is not None:
            self.vehicles = [v for v in self.vehicles if not isinstance(v, vehicle_type)]

    def fix_vehicle(self):
        """Iterate through each vehicle and calculate a bill based on its type."""
        bill = 0
        for v in self.vehicles:
            if isinstance(v, Car):
                bill += 100  # Example cost for fixing a car
            elif isinstance(v, Motorbike):
                bill += 50  # Example cost for fixing a motorbike
        return bill

    def empty_garage(self):
        """Remove all vehicles from the garage."""
        self.vehicles.clear()

    def remove_by_type(self, vehicle_type):
        """Remove all vehicles of a certain type."""
        self.vehicles = [v for v in self.vehicles if not isinstance(v, vehicle_type)]


# Example vehicle classes for testing
class Vehicle:
    def __init__(self, id):
        self.id = id


class Car(Vehicle):
    pass


class Motorbike(Vehicle):
    pass


# Example usage
garage = Garage()
car1 = Car(1)
bike1 = Motorbike(2)
garage.add_vehicle(car1)
garage.add_vehicle(bike1)

print("Total fix cost:", garage.fix_vehicle())  # Output: 150
garage.remove_vehicle(vehicle_id=1)
print("Vehicles after removing car:", len(garage.vehicles))  # Output: 1
garage.empty_garage()
print("Vehicles after emptying:", len(garage.vehicles))  # Output: 0
