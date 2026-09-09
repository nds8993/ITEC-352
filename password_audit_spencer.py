# Nicholas Spencer
# 09/08/26

"""
Password Strength Audit

Completed from the provided starter template.
Do not change the required function names or parameters.
"""


def get_password_count():
    """Prompt until the user enters a positive whole number; return that number."""

    # Creates a loop so the user can try again if invalid input is entered.
    while True:

        # Uses try/except ValueError to prevent the program from crashing
        # if the user enters something that cannot be converted to an integer.
        try:
            password_count = int(
                input("How many passwords would you like to audit? ")
            )

            # Only returns the number if it is greater than zero.
            if password_count > 0:
                return password_count
            else:
                print("Please enter a whole number greater than zero.")

        # Handles invalid input such as letters or symbols instead of a number.
        except ValueError:
            print("Please enter a whole number greater than zero.")


def evaluate_password(password):
    """Return Strong, Moderate, or Weak after examining one password."""

    # Creates local Boolean variables to track whether the password
    # contains uppercase, lowercase, digit, and special characters.
    # Each starts as False and changes to True when that type is found.
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    # Loops through and inspects every character in the password.
    for character in password:

        # Changes the appropriate Boolean variable to True
        # when that character type is found.
        if character.isupper():
            has_uppercase = True

        elif character.islower():
            has_lowercase = True

        elif character.isdigit():
            has_digit = True

        else:
            has_special = True

    # Counts how many of the four character-type requirements were met.
    # True counts as 1 and False counts as 0.
    type_total = (
        has_uppercase
        + has_lowercase
        + has_digit
        + has_special
    )

    # Uses if/elif/else to determine and return the correct password rating.
    # Strong requires at least 12 characters and all four character types.
    if len(password) >= 12 and type_total == 4:
        return "Strong"

    # Moderate requires at least 8 characters and at least three character types.
    elif len(password) >= 8 and type_total >= 3:
        return "Moderate"

    # Anything that does not meet the requirements above is Weak.
    else:
        return "Weak"


def display_summary(strong_count, moderate_count, weak_count):
    """Display the totals for each password-rating category."""

    # Prints a labeled final summary using the three parameters
    # passed into this function.
    print("\n--- Password Audit Summary ---")
    print("Strong passwords:  ", strong_count)
    print("Moderate passwords:", moderate_count)
    print("Weak passwords:    ", weak_count)


def main():
    """Coordinate the password audit."""

    # Creates local counters for Strong, Moderate, and Weak passwords.
    # Each counter starts at zero.
    strong_count = 0
    moderate_count = 0
    weak_count = 0

    # Calls get_password_count() and stores the returned number.
    password_count = get_password_count()

    # Loops once for each password the user wants to audit.
    for password_number in range(1, password_count + 1):

        password = input(f"\nPassword {password_number}: ")

        # Calls evaluate_password() and stores the returned rating.
        rating = evaluate_password(password)

        print("Rating:", rating)

        # Uses if/elif/else to update the appropriate password counter.
        if rating == "Strong":
            strong_count += 1

        elif rating == "Moderate":
            moderate_count += 1

        else:
            weak_count += 1

    # Calls display_summary() after all passwords have been evaluated.
    display_summary(
        strong_count,
        moderate_count,
        weak_count
    )


if __name__ == "__main__":
    main()
