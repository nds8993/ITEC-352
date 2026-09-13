# Week 4 Assignment - objects.py
# Name: Nicholas Spencer
# Date: September 13, 2026

class Sneaker:
    """Represents a sneaker with a brand, model, and price."""

    def __init__(self, brand, model, price):
        # Attributes are stored inside each Sneaker object.
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, discount_percent):
        """Reduces the sneaker price by the given percentage."""
        discount_amount = self.price * (discount_percent / 100)
        self.price = self.price - discount_amount

    def display_info(self):
        """Returns a formatted description of the sneaker."""
        return f"{self.brand} {self.model} - ${self.price:.2f}"
