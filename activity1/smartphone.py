# smartphone.py

class Smartphone:
    def __init__(self, brand, model, price, battery_level):
        self.brand = brand
        self.model = model
        self.price = price
        self._battery_level = battery_level  # Private attribute for battery level

    # Getter and setter for battery level to control access and validation
    @property
    def battery_level(self):
        return self._battery_level

    @battery_level.setter
    def battery_level(self, value):
        if 0 <= value <= 100:
            self._battery_level = value
        else:
            print("Invalid battery level. Must be between 0 and 100.")

    def make_call(self, number):
        """Simulate making a phone call."""
        print(f"Calling {number}... 📞")

    def charge(self, amount):
        """Simulate charging the phone."""
        self.battery_level += amount  # Uses setter to ensure valid battery level
        print(f"Charging... Battery level is now {self.battery_level}% 🔋")

    def display_info(self):
        """Display smartphone details."""
        print(f"Brand: {self.brand}, Model: {self.model}")
        print(f"Price: ${self.price}, Battery Level: {self.battery_level}%")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, battery_level, gaming_mode_enabled=False):
        super().__init__(brand, model, price, battery_level)
        self.gaming_mode_enabled = gaming_mode_enabled

    def display_info(self):
        """Override to include gaming mode status."""
        super().display_info()
        print(f"Gaming Mode Enabled: {self.gaming_mode_enabled}")

    def play_game(self, game_name):
        """Simulate playing a game on the gaming phone."""
        if self.gaming_mode_enabled:
            print(f"Playing {game_name} in high performance mode! 🎮")
        else:
            print(f"Cannot play {game_name}. Gaming mode is off. 😞")

# Example usage:
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 999, 50)
    phone.display_info()
    phone.make_call("123-456-7890")
    phone.charge(40)
    
    gaming_phone = GamingPhone("Razer", "Phone 2", 899, 75, True)
    gaming_phone.display_info()
    gaming_phone.play_game("PUBG")
    gaming_phone.charge(10)
