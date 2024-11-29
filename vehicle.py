# vehicle.py

class Vehicle:
    def move(self):
        """Base move method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        """Override to define car-specific movement."""
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        """Override to define plane-specific movement."""
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        """Override to define boat-specific movement."""
        print("Sailing ⛵")

# Example usage:
if __name__ == "__main__":
    # Create instances of each vehicle type
    car = Car()
    plane = Plane()
    boat = Boat()

    # Polymorphism in action
    for vehicle in [car, plane, boat]:
        vehicle.move()
