class Vehicle:
    """
    A class representing a vehicle with operations like start, stop, status, and fuel management.
    """

    def __init__(self, id: int, mot: bool, fuel_level: float = 100.0):
        """
        Initializes the Vehicle object with operational state (MOT) and a given fuel level.

        Args:
            mot (bool): A boolean indicating whether the vehicle is operational or not.
            fuel_level (float): The initial fuel level of the vehicle (default is 100.0%).
        """
        self.id = id
        self.mot = mot
        self.is_running = False if not mot else True
        self.fuel_level = fuel_level

    def start(self):
        """
        Starts the vehicle if it is operational and has fuel.
        """
        if self.fuel_level <= 0:
            print("Cannot start the vehicle. No fuel.")
            return

        if not self.is_running:
            self.is_running = True
            print("The vehicle has started.")
        else:
            print("The vehicle is already running.")

    def stop(self):
        """
        Stops the vehicle by setting the operational state to not running.
        """
        if self.is_running:
            self.is_running = False
            print("The vehicle has stopped.")
        else:
            print("The vehicle is already stopped.")

    def refuel(self, amount: float):
        """
        Refuels the vehicle by a given amount, ensuring fuel level doesn't exceed 100%.

        Args:
            amount (float): The amount of fuel to add (must be positive).
        """
        if amount < 0:
            print("Invalid fuel amount. Cannot be negative.")
            return

        self.fuel_level = min(self.fuel_level + amount, 100.0)  # Fuel cannot exceed 100%
        print(f"Vehicle refueled. Current fuel level: {self.fuel_level:.1f}%")

    def check_fuel(self):
        """
        Returns the current fuel level of the vehicle.

        Returns:
            float: The current fuel level as a percentage.
        """
        return self.fuel_level

    def __str__(self) -> str:
        """
        Provides a string representation of the Vehicle object, showing its operational status and fuel level.

        Returns:
            str: A formatted string with the vehicle's MOT status and fuel level.
        """
        return f"Vehicle - MOT Status: {'Operational' if self.mot else 'Not Operational'}, Fuel Level: {self.fuel_level:.1f}%"

    def display_status(self):
        """
        Displays the current status of the vehicle (running or not running) and the fuel level.
        """
        running_status = "Running" if self.is_running else "Not Running"
        return f"The vehicle is {running_status}. Current fuel level: {self.fuel_level:.1f}%"

    def check_mot(self):
        """
        Checks if the vehicle is operational.

        Returns:
            bool: Whether the vehicle is operational.
        """
        return self.mot

    def update_mot(self, status: bool):
        """
        Updates the operational status of the vehicle (MOT status).

        Args:
            status (bool): The new MOT status. True for operational, False for not operational.
        """
        self.mot = status
        self.is_running = self.mot
        print(f"Vehicle MOT updated. Now it is {'operational' if self.mot else 'not operational'}.")
