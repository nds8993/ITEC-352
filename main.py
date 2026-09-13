# Week 4 Assignment - main.py
# Name: Nicholas Spencer
# Date: September 13, 2026

# Import the Sneaker class from the objects module.
from objects import Sneaker


def main():
    # Create two Sneaker objects.
    sneaker1 = Sneaker("Nike", "Air Max 90", 130.00)
    sneaker2 = Sneaker("Adidas", "Ultraboost", 180.00)

    # Display the original object information.
    print("Original Sneaker Information:")
    print(sneaker1.display_info())
    print(sneaker2.display_info())

    # Use a method to change the price of sneaker1.
    sneaker1.apply_discount(20)
    sneaker2.apply_discount(20)

    print("\nAfter 20% Discount:")
    print(sneaker1.display_info())
    print(sneaker2.display_info())


# Run the program.
if __name__ == "__main__":
    main()
