"""
SDEV 300 6384
Author: Isaac Finehout
Date: 9 September 2023
Lab 4: Lists and Sets
"""
import re
import numpy as np
# Used to display menu numbers and error
RED: str = "\033[91m"
RESET: str = "\033[0m"
NEW_PAGE: str = "\n"*30


def print_menu():
    """
    Allow the user to select a single state from a list.
    :return:
    Return the input entered by the user."""
    print("***************** Welcome to the Python Matrix Application***********")
    print("Do you want to play the Matrix Game?")
    user_input_menu: str = ""
    while user_input_menu.casefold() not in ['y', 'n']:
        user_input_menu = input("Please enter Y for Yes or N for No: ")
    return user_input_menu


def validate_regex(regex_string, input_prompt):
    """
    Prompts the user to enter a correct regex string.
    :param regex_string:
    The regex string entered by the user.
    :param input_prompt:
    The input prompt ensuring the user enters the right regex string.
    :return:
    """
    user_input: str
    is_valid_input: bool = False
    while not is_valid_input:
        user_input = input(input_prompt)
        if re.match(regex_string, user_input):
            return user_input
        print(RED + "Invalid Input." + RESET)
    return None


def find_row_numbers(row_string: str):
    """
    Uses string slicing to find integers for each row in the 3x3 matrix
    from strings previously validated by regex
    :param row_string:
    The string containing three valid integers separated by two spaces
    :return:
    Returns the three integers in the row,
    each representing a column in the 3x3 matrix
    """
    col_1: int
    col_2: int
    col_3: int
    col_1: int = int(row_string[0:row_string.find(" ")])
    col_2: int = int(row_string[row_string.find(" ") + 1:
                                row_string.find(" ", row_string.find(" ") + 1)])
    col_3: int = int(row_string[row_string.find(" ", row_string.find(" ") + 1):])
    return col_1, col_2, col_3


def validate_matrix() -> np.array:
    """
    Ensures the user enters a valid 3x3 matrix.
    :return:
    The 3x3 matrix entered by the user.
    """
    first_row: str
    second_row: str
    third_row: str
    print("Enter your 3x3 matrix:")
    first_row = validate_regex(r"\d+ \d+ \d+", "Enter first row:")
    second_row = validate_regex(r"\d+ \d+ \d+", "Enter second row:")
    third_row = validate_regex(r"\d+ \d+ \d+", "Enter third row:")
    num_1, num_2, num_3 = find_row_numbers(first_row)
    num_4, num_5, num_6 = find_row_numbers(second_row)
    num_7, num_8, num_9 = find_row_numbers(third_row)
    return np.array([[num_1, num_2, num_3],
                     [num_4, num_5, num_6],
                     [num_7, num_8, num_9]])


def play_python_numpy():
    """
    Plays the main python numpy game.
    """
    zip_plus_four: str = validate_regex(
        r"\d{5}-\d{4}", "Enter your zip code+4 (XXXXX-XXXX):")
    print("The zip code is", zip_plus_four)

    phone_number: str = validate_regex(
        r"\d{3}-\d{3}-\d{4}", "Enter your phone number (XXX-XXX-XXXX):")
    print("The phone number is", phone_number)

    first_matrix: np.array = validate_matrix()
    print("Your first 3x3 matrix is:\n" + str(first_matrix))

    second_matrix: np.array = validate_matrix()
    print("Your second 3x3 matrix is:\n" + str(second_matrix))

    print("Select a Matrix Operation from the list below:")
    print("a. Addition\nb. Subtraction\nc. Matrix Multiplication\n"
          "d. Element by element multiplication")
    # Ensure the user can only enter option a, b, c, or d
    user_choice_play: str = input()
    while user_choice_play.casefold() not in ['a', 'b', 'c', 'd']:
        user_choice_play = input(RED + "Please choose a b c or d:" + RESET)

    # Create a new matrix based on the user's choice
    new_matrix: np.array
    if user_choice_play == 'a':
        new_matrix = np.add(first_matrix, second_matrix)
        print("You selected Addition. The results are:\n"
              + str(new_matrix))
    elif user_choice_play == 'b':
        new_matrix = np.subtract(first_matrix, second_matrix)
        print("You selected Subtraction. The results are:\n"
              + str(new_matrix))
    elif user_choice_play == 'c':
        new_matrix = np.matmul(first_matrix, second_matrix)
        print("You selected  multiplication. The results are:\n"
              + str(new_matrix))
    else:
        new_matrix = np.multiply(first_matrix, second_matrix)
        print("You selected element by element multiplication. The results are:\n"
              + str(new_matrix))
    print("The transpose is:\n" + str(np.transpose(new_matrix)))
    print("The row and column mean values of the results are:"
          + "\nRow: "
          + f"{(new_matrix[0][0] + new_matrix[0][1] + new_matrix[0][2])/3:.2f} "
          + f"{(new_matrix[1][0] + new_matrix[1][1] + new_matrix[1][2])/3:.2f} "
          + f"{(new_matrix[2][0] + new_matrix[2][1] + new_matrix[2][2])/3:.2f}"
          + "\nColumn: "
          + f"{(new_matrix[0][0] + new_matrix[1][0] + new_matrix[2][0])/3:.2f} "
          + f"{(new_matrix[0][1] + new_matrix[1][1] + new_matrix[2][1])/3:.2f} "
          + f"{(new_matrix[0][2] + new_matrix[1][2] + new_matrix[2][2])/3:.2f}")


if __name__ == "__main__":
    # While the program is running, print the menu, get user choice, and process user choice.
    is_program_running: bool = True
    user_choice: str
    while is_program_running:
        user_choice = print_menu()
        if user_choice.casefold() == "y":
            play_python_numpy()
        else:
            print("*********** Thanks for playing Python Numpy ***************")
            is_program_running = False  # pylint: disable=invalid-name
