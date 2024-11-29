# test_vehicle.py
from vehicle import Car, Plane, Boat

def test_vehicle_movement():
    print("Testing Vehicle Movement:")
    # Create instances of vehicles
    car = Car()
    plane = Plane()
    boat = Boat()

    # Call the move method on each instance (polymorphism)
    car.move()  # Expected output: Driving 🚗
    plane.move()  # Expected output: Flying ✈️
    boat.move()  # Expected output: Sailing ⛵

if __name__ == "__main__":
    test_vehicle_movement()
