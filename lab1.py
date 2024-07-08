"""
SDEV 300 6384
Author: Isaac Finehout
Lab 1: Python Start
20 August 2023


user_input (str): User input
is_entering_data (bool): Lets the user renter data if they entered it wrong
first_name (str): User's first name
last_name (str): User's last name
age (int): User's age
is_american (bool): Whether the user is American
state (str): User's state
zipcode (int): User's zipcode
"""
import sys  # Used to exit if the user chooses not to continue


def ask_to_continue():
    """
    Check to see if the user wants to continue, and exit if they don't
    if the user enters yes
        continue the program
    if the user enters no
        confirm
            exit program
    else
        ask the user to renter their answer
    """
    is_valid_input: bool = False
    user_input: str = "PLACEHOLDER"

    while not is_valid_input:
        user_input = input("Do you want to continue?\n=>")
        if user_input.casefold()[0] == 'y':
            # Set is_valid_input equal to True and continue the program
            is_valid_input = True
        elif user_input.casefold()[0] == 'n':
            # Ask the user to confirm program exit
            print(f"Enter {user_input} one more time to confirm system exit: ")
            if input() == user_input:
                # If the user enters a no answer twice, exit the program
                sys.exit()
            # Do nothing and continue the program if the user doesn't confirm exit
        else:
            # If the user doesn't enter valid input, ask them to renter
            print("Please enter a yes or no answer.")


def validate_first_name(user_input: str) -> str:
    """
    Used to validate the first name
    Verifies the name is under 20 characters

    :param user_input: user_input from the outer function
    :return: return user_input to set it equal to first_name
    """
    is_user_input_valid: bool = False
    while not is_user_input_valid:
        if len(user_input) > 20:
            print("The first name must be under 20 characters. Please reenter the first name.")
            user_input = input()
        else:
            is_user_input_valid = True
    return user_input


def validate_last_name(user_input: str) -> str:
    """
    Used to validate the last name
    Verifies the name is under 20 characters

    :param user_input: user_input from the outer function
    :return: return user_input to set it equal to last_name
    """
    is_user_input_valid: bool = False
    while not is_user_input_valid:
        if len(user_input) > 20:
            print("The last name must be under 20 characters. Please reenter the last name.")
            user_input = input()
        else:
            is_user_input_valid = True
    return user_input


def validate_age(user_input: str) -> int:
    """
    Used to validate the age
    Verifies the age is an integer between 18-120

    :param user_input: user_input from the outer function
    :return: return user_input to set it equal to age
    """
    is_user_input_valid: bool = False

    while not is_user_input_valid:
        try:
            if int(user_input) < 18 or 120 < int(user_input):
                print("The age must be greater than 18, or under 120.")
                ask_to_continue()
                user_input = input("Please enter your age.\n")
            else:
                is_user_input_valid = True
        except ValueError:
            print("The age must be a whole number.")
            user_input = input("Please enter your age.\n")
    return int(user_input)


def validate_is_american(user_input: str) -> bool:
    """
    Used to validate if the user is American

    :param user_input: user_input from the outer function
    :return: return whether user_input is yes to set it equal to is_american
    """
    is_user_input_valid: bool = False
    while not is_user_input_valid:
        if not (user_input.casefold()[0] in ['y', 'n']):
            user_input = input("Please enter yes or no.\n")
        else:
            is_user_input_valid = True
    return user_input.casefold().startswith('y')


def validate_state(user_input: str) -> str | None:
    """
    Used to validate the state
    Verifies the input is one of the 50 state codes

    :param user_input: user_input from the outer function
    :return: return user_input to set it equal to state
    """
    is_user_input_valid: bool = False
    state_codes = (
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    )
    while not is_user_input_valid:
        if user_input in state_codes:
            return user_input
        print("Please enter a valid uppercase two-digit state code (e.g., TX)")
        user_input = input().upper()
    return None


def validate_zipcode(user_input: str) -> int:
    """
    Used to validate the zipcode
    Verifies the zipcode is a 5-digit integer

    :param user_input: user_input from the outer function
    :return: return user_input to set it equal to the zipcode
    """
    is_user_input_valid: bool = False
    while not is_user_input_valid:
        try:
            if int(user_input) < 0:
                raise ValueError
            if len(user_input) != 5:
                print("The zip code must be 5 digits long.")
                user_input = input("Please enter a new zipcode.\n")
            else:
                is_user_input_valid = True
        except ValueError:
            print("The zip code must be a whole number.")
            user_input = input("Please enter a new zipcode.\n")
    return int(user_input)


def main():
    """
    Runs the voter registration program
    There are six main entries, one for each piece of data
    Before and after the 6 entries are an introduction and conclusion
    Each entry follows the style of pseudocode displayed below:

    Call function ask_to_continue() to see if the user wants to continue
    Set user_input equal to input from the user
    Call a function for the specific input to validate
    """
    first_name: str
    last_name: str
    age: int
    is_american: bool
    state: str
    zipcode: int
    user_input: str

    print("*"*64)
    print("Welcome to the Python Voter Registration Application.")

    ask_to_continue()
    user_input = input("What is your first name?\n")
    first_name = validate_first_name(user_input)

    ask_to_continue()
    user_input = input("What is your last name?\n")
    last_name = validate_last_name(user_input)

    ask_to_continue()
    user_input = input("What is your age?\n")
    age = validate_age(user_input)

    ask_to_continue()
    user_input = input("Are you a U.S. Citizen?\n")
    is_american = validate_is_american(user_input)

    ask_to_continue()
    user_input = input("What state do you live in (two-letter state code, e.g., TX)?\n").upper()
    state = validate_state(user_input)

    ask_to_continue()
    user_input = input("What is your zipcode?\n")
    zipcode = validate_zipcode(user_input)

    print("Thanks for registering to vote. Here is the information we received:")
    print(f"Name (first last): {first_name} {last_name}")
    print(f"Age: {age}")
    print("U.S. Citizen:", "Yes" if is_american else "No")
    print(f"State: {state}")
    print(f"Zipcode: {zipcode}")
    print("Thanks for trying the Voter Registration Application.")
    if is_american:
        print("Your voter registration card should be shipped within 3 weeks.")
    else:
        print("Please reapply once you receive citizenship for your voter registration card.")
    print("*"*64)


main()
