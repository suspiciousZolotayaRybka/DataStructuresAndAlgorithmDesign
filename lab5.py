"""
SDEV 300 6384
Author: Isaac Finehout
Date: 18 September 2023
Lab 5: File Data Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
RED: str = "\033[91m"
RESET: str = "\033[0m"
NEW_PAGE: str = "\n"*30


def print_menu(menu_prompt: str, menu_choices: list):
    """
    Print the main menu
    :param menu_prompt:
    The string that prompts the user to enter a menu choice.
    :param menu_choices:
    A list of string menu choices.
    """
    print(menu_prompt)
    count: int = 1
    for choice in menu_choices:
        print(f"{count}. {choice}")
        count += 1


def get_integer(min_value: int, max_value: int) -> int | None:
    """
    Used throughout the CLI program to validate the user's input
    :param min_value:
    The minimum value the user can enter, inclusive.
    :param max_value:
    The maximum value the user can enter, inclusive.
    :return:
    The user's choice.
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


def analyze_column(selected_column: str, clm: pd.Series):
    """
    Takes a column from a csv file and prints information about that column.
    :param selected_column:
    The name of the column.
    :param clm:
    The column data using Pandas
    """
    # Print out the required information for the column, then show its histogram
    print("You selected", selected_column)
    print("The statistics for this column are:")
    print("Count =", clm.count())
    print("Mean =", clm.mean())
    print("Standard Deviation =", clm.std())
    print("Min =", clm.min())
    print("Max =", clm.max())
    print("The histogram of this column is now displayed.")
    plt.title(selected_column)
    plt.hist(clm)
    plt.show()
    # Prompt the user to press enter once they have finished viewing the information
    print("Press ENTER to continue...")
    input()
    print(NEW_PAGE)


def population_data():
    """
    Contains menu options for viewing the population data excel.
    """
    # No with keyword or try...except...finally required to acquire and release resources
    # pd does this automatically
    population_df: pd.DataFrame = pd.DataFrame()
    is_population_df_valid: bool = False
    try:
        # Still need a try...except to catch FileNotFound error
        population_df = pd.read_csv("data/PopChange.csv")
        is_population_df_valid = True
    except FileNotFoundError:
        print(RED + "Error: data/PopChange.csv not found." + RESET)

    if is_population_df_valid:
        # If the file was found, enter the population loop
        print("You have entered Population Data.")
        user_pop_choice: int = 0
        while user_pop_choice != 4:
            # While the user is in the Population menu,
            # ask the user for the data they want to analyze
            print_menu("Select the Column you want to analyze:",
                       ["Pop Apr 1", "Pop Jul 1", "Change Pop", "Exit Column"])
            user_pop_choice: int = get_integer(1, 4)
            # Based on the user choice, call the function analyze_column
            # Use the appropriate pd.DataFrame column as an argument
            if user_pop_choice == 1:
                pop_apr_clm: pd.Series = population_df["Pop Apr 1"]
                analyze_column("Pop Apr 1", pop_apr_clm)
            elif user_pop_choice == 2:
                pop_jul_clm: pd.Series = population_df["Pop Jul 1"]
                analyze_column("Pop Jul 1", pop_jul_clm)
            elif user_pop_choice == 3:
                pop_chg_clm: pd.Series = population_df["Change Pop"]
                analyze_column("Change Pop", pop_chg_clm)
            else:
                # Exit if the user chooses 4
                print("You selected to exit the column menu.")


def housing_data():
    """
    Contains menu options for viewing the population data excel.
    """
    # No with keyword or try...except...finally required to acquire and release resources
    # pd does this automatically
    housing_df: pd.DataFrame = pd.DataFrame()
    is_housing_df_valid: bool = False
    try:
        # Still need a try...except to catch FileNotFound error
        housing_df = pd.read_csv("data/Housing.csv")
        is_housing_df_valid = True
    except FileNotFoundError:
        print(RED + "Error: data/Housing.csv not found." + RESET)

    if is_housing_df_valid:
        # If the file was found, enter the housing loop
        print("You have entered Housing Data.")
        user_housing_choice: int = 0
        while user_housing_choice != 6:
            # While the user is in the Population menu,
            # ask the user for the data they want to analyze
            print_menu("Select the Column you want to analyze:",
                       ["AGE", "BEDRMS", "BUILT", "ROOMS", "UTILITY", "Exit Column"])
            user_housing_choice: int = get_integer(1, 6)
            # Based on the user choice, call the function analyze_column
            # Use the appropriate pd.DataFrame column as an argument
            if user_housing_choice == 1:
                hsg_age_clm: pd.Series = housing_df["AGE"]
                analyze_column("AGE", hsg_age_clm)
            elif user_housing_choice == 2:
                hsg_bedrms_clm: pd.Series = housing_df["BEDRMS"]
                analyze_column("BEDRMS", hsg_bedrms_clm)
            elif user_housing_choice == 3:
                hsg_built_clm: pd.Series = housing_df["BUILT"]
                analyze_column("BUILT", hsg_built_clm)
            elif user_housing_choice == 4:
                hsg_rooms_clm: pd.Series = housing_df["ROOMS"]
                analyze_column("ROOMS", hsg_rooms_clm)
            elif user_housing_choice == 5:
                hsg_utility_clm: pd.Series = housing_df["UTILITY"]
                analyze_column("UTILITY", hsg_utility_clm)
            else:
                # Exit if the user chooses 6
                print("You selected to exit the column menu.")


def process_user_choice(choice: int) -> bool:
    """
    Call the appropriate function based on the user's choice from the main menu
    :param choice:
    The menu choice chosen by the user
    :return:
    Return a boolean that determines whether to continue running the program
    """
    if choice == 1:
        population_data()
    elif choice == 2:
        housing_data()
    else:
        # If user chooses 3 (exit) return False in order to leave the program
        print("*************** Thanks for using the Data Analysis App**********")
        return False
    # If user chooses any option other than 3 (exit) prompt them to continue once finished
    print("Press ENTER to continue...")
    input()
    print(NEW_PAGE)
    return True


if __name__ == "__main__":
    # While the program is running, print the menu, get user choice, and process user choice
    is_program_running: bool = True  # pylint: disable=invalid-name
    user_choice: int
    print("***************** Welcome to the Python Data Analysis App**********")
    while is_program_running:
        print_menu("Select the file you want to analyze:",
                   ["Population Data", "Housing Data", "Exit the Program"])
        user_choice = get_integer(1, 3)
        is_program_running = process_user_choice(user_choice)  # pylint: disable=invalid-name
