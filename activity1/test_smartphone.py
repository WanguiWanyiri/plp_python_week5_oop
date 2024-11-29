# test_smartphone.py
from smartphone import Smartphone, GamingPhone

def test_smartphone():
    print("Testing Smartphone:")
    phone = Smartphone("Samsung", "Galaxy S23", 899, 65)
    phone.display_info()
    phone.make_call("987-654-3210")
    phone.charge(20)

def test_gaming_phone():
    print("\nTesting GamingPhone:")
    gaming_phone = GamingPhone("Asus", "ROG Phone 6", 999, 80, True)
    gaming_phone.display_info()
    gaming_phone.play_game("Fortnite")
    gaming_phone.charge(15)

if __name__ == "__main__":
    test_smartphone()
    test_gaming_phone()
