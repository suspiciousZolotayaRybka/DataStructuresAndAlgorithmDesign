"""
SDEV 300 6384
Author: Isaac Finehout
Date: 20 August 2023
Lab 2: Math and Secret Generation
"""
import string
import secrets
import datetime
import math
import os
RED: str = "\033[91m"
RESET: str = "\033[0m"
NEW_PAGE: str = "\n"*30


def print_menu() -> None:
    """
    Print the main menu
    """
    print("== == == == == == == == == == == == == == == == == == == == == == ==")
    print("🚀  MAIN MENU  🚀")
    print("== == == == == == == == == == == == == == == == == == == == == == ==")
    print(RED + "1|" + RESET + "🔒 Generate Secure Password")
    print(RED + "2|" + RESET + "% Calculate and Format a Percentage")
    print(RED + "3|" + RESET + "📆 How many days from today until July 4, 2025")
    print(RED + "4|" + RESET + "📐 Use the Law of Cosines to calculate the leg of a triangle")
    print(RED + "5|" + RESET + "🛢 Calculate the volume of a Right Circular Cylinder")
    print(RED + "6|" + RESET + "⛔ Exit program")
    print()


def get_integer(min_value: int, max_value: int) -> int | None:
    """
    Used throughout the CLI program to validate the user's input
    """
    is_valid_input: bool = False
    while not is_valid_input:
        try:
            int_choice: int = int(input("=>"))
            if min_value <= int_choice <= max_value:
                return int_choice
            print(RED + f"Please enter a number between {min_value}-{max_value}: " + RESET)
        except ValueError:
            print(RED + "Please enter an integer: " + RESET)
    return None


def get_float(min_value: float, max_value: float) -> float | None:
    """
    Used throughout the CLI program to validate the user's input
    """
    is_valid_input: bool = False
    while not is_valid_input:
        try:
            float_choice: float = float(input("=>"))
            if min_value <= float_choice <= max_value:
                return float_choice
            print(RED + f"Please enter a number between {min_value}-{max_value}: " + RESET)
        except ValueError:
            print(RED + "Please enter a float: " + RESET)
    return None


def generate_secure_password() -> None:
    """
    Generate an 11 to 64-character alphanumeric password with at least one lowercase character, one
    uppercase character, at least three digits, and at least three symbols as chosen by the user.
    """

    # Prompt user for length, and presence of upper/lowercase, punctuation symbols, and digits
    print("Please enter an integer between 11-64 for the length of your password.")
    len_password = get_integer(11, 64)
    print("Include lowercase letters?\n1 - Yes\n2 - No")
    has_lowercase: bool = (get_integer(1, 2)) == 1
    print("Include uppercase letters?\n1 - Yes\n2 - No")
    has_uppercase: bool = (get_integer(1, 2)) == 1
    print("Include punctuation symbols?\n1 - Yes\n2 - No")
    has_punct: bool = (get_integer(1, 2)) == 1
    print("Include digits 0-9?\n1 - Yes\n2 - No")
    has_digits: bool = (get_integer(1, 2)) == 1

    has_at_least_one_symbol: bool = has_lowercase or has_uppercase or has_punct or has_digits

    alphabet = ""
    if has_at_least_one_symbol:
        # If the password has at least one chosen symbol, concatenate it to the password alphabet
        if has_lowercase:
            alphabet += string.ascii_lowercase
        if has_uppercase:
            alphabet += string.ascii_uppercase
        if has_punct:
            alphabet += string.punctuation
        if has_digits:
            alphabet += string.digits
    else:
        # If the user chose no symbol, inform them of their error
        print(RED + "You must include at least one type of symbol in your password." + RESET
              + "\nPlease revisit and try again.")

    if has_at_least_one_symbol:
        # Only generate the user's password if they chose at least one symbol
        is_creating_password: bool = True
        password: str = ""

        # Boolean values check the validity of the password each time the loop executes
        # If the password contains the corresponding symbols, they must at least have the following:
        #     At least 1 lowercase
        #     At least 1 uppercase
        #     At least 3 digits
        #     At least 3 punctuation

        is_lowercase_valid: bool
        is_uppercase_valid: bool
        is_digits_valid: bool
        is_punct_valid: bool
        while is_creating_password:
            password = "".join(secrets.choice(alphabet) for i in range(len_password))
            is_lowercase_valid = any(c.islower() for c in password) or (not has_lowercase)
            is_uppercase_valid = any(c.isupper() for c in password) or (not has_uppercase)
            is_digits_valid = sum(c.isdigit() for c in password) >= 3 or (not has_digits)
            is_punct_valid = sum(c in string.punctuation for c in password) >= 3 or (not has_punct)
            # If all checks are valid, break the loop. Otherwise, renter and reform the password
            if is_lowercase_valid and is_uppercase_valid and is_digits_valid and is_punct_valid:
                break
        print("Secure Password:", password)


def format_percentage() -> None:
    """
    Calculate and format a percentage.
    Based on a simple example using the input 22, 57, and 3 as the
    numerator, denominator, and the number of decimal points.
    This results in 38.596
    """

    # Type-hint declare variables
    numerator: int
    denominator: int
    num_decimal: int

    # Receive user input
    print("Please enter your numerator.")
    numerator = get_integer(-2147483648, 2147483648)
    print("Please enter your denominator.")
    denominator = get_integer(-2147483648, 2147483648)
    print("Please enter the number of decimal places to be shown.")
    num_decimal = get_integer(0, 11)

    # Find the percentage and print
    percentage: float = (numerator/denominator) * 100
    print(f"Your percentage is: {percentage:.{num_decimal}f}")


def calculate_days() -> None:
    """
    Calculate the number of days until July 4, 2025
    """

    # Find today's date and assign July 4, 2025
    today: datetime.date = datetime.date.today()
    target_date: datetime.date = datetime.date(2025, 7, 4)

    # Find the number of days between the two dates
    num_days_delta: datetime.timedelta = target_date - today
    print(f"There are {num_days_delta.days} days between now ({today:%B} {today.day}, {today.year})"
          " and July 4, 2025")


def solve_triangle() -> None:
    """
    Use the law of cosines to solve for side c in a triangle.
    """

    # Declare variables
    angle_c: float
    side_a: float
    side_b: float
    side_c: float

    # Prompt the user for triangle values
    print("Please enter the value for angle c in degrees.")
    angle_c = get_float(0.0000001, 179.9999999)
    print("Please enter the value for side a.")
    side_a = get_float(0.0000001, 2147483648)
    print("Please enter the value for side b.")
    side_b = get_float(0.0000001, 2147483648)

    # Find the value for side c
    side_c = math.sqrt((side_a ** 2) + (side_b ** 2) -
                       (2*side_a*side_b*math.cos(math.radians(angle_c))))
    print(f"The length of a triangle side c with side a {side_a} units long,"
          f"side b {side_b} units long, and angle c {angle_c} degrees is:\n{side_c}.")


def calculate_cylinder_volume() -> None:
    """
    Calculate the volume of a right cylinder based on
    """

    # Declare variables
    radius: float
    height: float
    volume: float

    # Prompt the user for variable values
    print("Enter the value for the right cylinder radius.")
    radius = get_float(0.000001, 2147483648)
    print("Enter the value for the right cylinder height.")
    height = get_float(0.000001, 2147483648)

    # Find the right cylinder volume
    volume = ((math.pi * (radius ** 2)) * height)
    print(f"The volume for a right cylinder with a radius of"
          f"{radius} units and a height of {height} units is:"
          f"\n{volume} units.")


def process_user_choice(choice: int) -> bool:
    """
    Call functions for the program based on the user's choice
    """
    if choice == 1:
        generate_secure_password()
    elif choice == 2:
        format_percentage()
    elif choice == 3:
        calculate_days()
    elif choice == 4:
        solve_triangle()
    elif choice == 5:
        calculate_cylinder_volume()
    else:
        print(NEW_PAGE)
        print("Thank you for visiting the Lab 2 Application!")
        return False
    # If user chooses any option other than 6 (exit) prompt them to continue once finished
    input("Press ENTER to continue...")
    print(NEW_PAGE)
    return True


if __name__ == "__main__":
    # While the program is running, print the menu, get user choice, and process user choice
    is_program_running: bool = True  # pylint: disable=invalid-name
    user_choice: int
    while is_program_running:
        print_menu()
        user_choice = get_integer(1, 6)
        is_program_running = process_user_choice(user_choice)  # pylint: disable=invalid-name
