"""
SDEV 300 6384
Author: Isaac Finehout
Date: 1 September 2023
Lab 3: Lists and Sets
"""
import matplotlib.pyplot as plt
from PIL import Image
# Used to display menu numbers and error
RED: str = "\033[91m"
RESET: str = "\033[0m"
NEW_PAGE: str = "\n"*30
# Constants for array indices
STATE: int = 0
CAPITAL: int = 1
POPULATION: int = 2
FLOWER: int = 3


def get_integer(min_value: int, max_value: int) -> int | None:
    """
    Used throughout the CLI program to validate the user's input.
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


def print_menu():
    """
    Print the main menu.
    """
    print("-"*58)
    print(" "*14, "U.S. State Information System")
    print("-"*58)
    print()
    print("Please choose an option from the menu: ")
    print(RED + "1." + RESET, "Display all U.S. States")
    print(RED + "2." + RESET, "Search for a specific state")
    print(RED + "3." + RESET, "Provide a bar graph of top 5 populated states")
    print(RED + "4." + RESET, "Update state population for a specific state")
    print(RED + "5." + RESET, "Exit the program")
    print()


def display_all(states_info_all: list):
    """
    Display all states to the user.
    """
    print("-"*58)
    print(" "*18, "U.S. States Information")
    print("-"*58)
    print()
    print(f"{'State':<30}{'Capital':<30}{'Population':<30}{'Flower':<30}")
    print("="*120)
    # Print each state's info separated by dashes (-)
    for state in states_info_all:
        print(f"{state[STATE]:<30}", end="")
        print(f"{state[CAPITAL]:<30}", end="")
        print(f"{state[POPULATION]:<30,}", end="")
        print(f"{state[FLOWER]:<30}")
        print('-'*120)
    print("="*120)


def select_state(states_info_select: list) -> int:
    """
    Allow the user to select a single state from a list.
    :param states_info_select:
    a list of the states and their attributes
    :return:
    Return the chosen state by the user."""
    chosen_state: int
    print("-"*58)
    print(" "*22, "State Selector")
    print("-"*58)
    print()
    print("Please select a US state form the list below, or 51 to return to main menu:")
    for i in range(50):
        print(f"{i + 1:>2}.{states_info_select[i][STATE]:<15}", end="")
        if i % 4 == 3:
            # Add a line break after every fourth state
            print()
    print("\n51. Return to Main Menu")
    chosen_state = get_integer(1, 51)
    if chosen_state == 51:
        return -1
    return chosen_state - 1


def display_single_state(state: int, states_info_single: list):
    """
    Allow the user to select a single state from a list.
    :param state:
    the index location of the chosen state to display
    :param states_info_single:
    a list of the states and their attributes
    :return:
    Return the chosen state by the user."""
    if state == -1:
        # The user chose 51 and does not want to view a state.
        print("You chose to return to the main menu.")
    else:
        # The user chose a state to view.
        print()
        print(f"State: {states_info_single[state][STATE]}")
        print(f"Capital: {states_info_single[state][CAPITAL]}")
        print(f"Population: {states_info_single[state][POPULATION]:,}")
        print(f"Flower: {states_info_single[state][FLOWER]}")
        print()
        # Find the name of the flower file and show it to the user
        flower_name = states_info_single[state][FLOWER]
        img: Image = Image.open("images/" + flower_name.replace(" ", "_") + ".webp")
        plt.title(flower_name)
        plt.imshow(img)
        plt.show()


def display_top5_graph(states_info_top5):
    """
    Display a pylot bar graph of the top five populated states
    :param states_info_top5:
    a list of the states and their attributes
    :return:
    Return the chosen state by the user."""
    # Sorted functionality in Python documentation: https://docs.python.org/3/howto/sorting.html
    # A similar example is under "Key Functions"
    states_info_top5 = sorted(states_info_top5, key=lambda state: state[POPULATION])
    states_info_top5.reverse()
    # Fill in lists for the top five bar graph
    states: list[str] = [states_info_top5[4][STATE],
                         states_info_top5[3][STATE],
                         states_info_top5[2][STATE],
                         states_info_top5[1][STATE],
                         states_info_top5[0][STATE]]
    populations: list[int] = [states_info_top5[4][POPULATION],
                              states_info_top5[3][POPULATION],
                              states_info_top5[2][POPULATION],
                              states_info_top5[1][POPULATION],
                              states_info_top5[0][POPULATION]]
    colors = ["blue", "lightgray", "red", "lightgray", "blue"]
    # Fill in and display the bar graph to the user
    plt.bar(states, populations, color=colors)
    plt.title("Top 5 States")
    plt.show()


def update_state_population(state: int, states_info_update: list) -> list:
    """
    Update the state's population chosen by the user.
    :param state:
    An integer for user choice
    :param states_info_update:
    a list of the states and their attributes
    :return:
    The updated list of states"""
    if state == -1:
        # The user chose 51 and does not want to change state population.
        print("You chose to return to the main menu.")
    else:
        # The user chose a population to change.
        print()
        print(f"Enter the new population for {states_info_update[state][STATE]}"
              f" (current: {states_info_update[state][POPULATION]:,}).")
        new_population: int = get_integer(10_000, 1_000_000_000)
        states_info_update[state][POPULATION] = new_population
        print(f"{states_info_update[state][STATE]}'s new population:"
              f" {states_info_update[state][POPULATION]:,}")
    return states_info_update


def process_choice(choice: int, states_info_process: list) -> tuple[bool, list]:
    """
    Call function for the program based on the user's choice.
    :param choice:
    An integer for user choice
    :param states_info_process:
    a list of the states and their attributes
    :return:
    Whether the program is still running and the updated states_info list."""
    current_state: int
    if choice == 1:
        display_all(states_info_process)
    elif choice == 2:
        current_state = select_state(states_info_process)
        display_single_state(current_state, states_info_process)
    elif choice == 3:
        display_top5_graph(states_info_process)
    elif choice == 4:
        current_state = select_state(states_info)
        states_info_process = update_state_population(current_state, states_info_process)
    else:
        print(NEW_PAGE)
        print("Thank you for visiting the Lab 3 Application!")
        return False, states_info_process
    # If user chooses any option other than 6 (exit) prompt them to continue once finished
    input("Press ENTER to continue...")
    print(NEW_PAGE)
    return True, states_info_process


if __name__ == '__main__':
    # While the program is running, print the menu, get user choice, and process user choice.
    states_info: list = [
        ["Alabama", "Montgomery", 5098746, "Camellia"],
        ["Alaska", "Juneau", 732984, "Forget-me-not"],
        ["Arizona", "Phoenix", 7453517, "Saguaro Cactus Blossom"],
        ["Arkansas", "Little Rock", 3063152, "Apple Blossom"],
        ["California", "Sacramento", 38915693, "California Poppy"],
        ["Colorado", "Denver", 5868555, "Rocky Mountain Columbine"],
        ["Connecticut", "Hartford", 3629055, "Mountain Laurel"],
        ["Delaware", "Dover", 1031985, "Peach Blossom"],
        ["Florida", "Tallahassee", 22661577, "Orange Blossom"],
        ["Georgia", "Atlanta", 11037723, "Cherokee Rose"],
        ["Hawaii", "Honolulu", 1433238, "Hibiscus"],
        ["Idaho", "Boise", 1973752, "Syringa"],
        ["Illinois", "Springfield", 12477595, "Violet"],
        ["Indiana", "Indianapolis", 6852542, "Peony"],
        ["Iowa", "Des Moines", 3203345, "Wild Rose"],
        ["Kansas", "Topeka", 2936378, "Sunflower"],
        ["Kentucky", "Frankfort", 4518031, "Goldenrod"],
        ["Louisiana", "Baton Rouge", 4553384, "Magnolia"],
        ["Maine", "Augusta", 1393442, "White Pine"],
        ["Maryland", "Annapolis", 6154710, "Black-eyed Susan"],
        ["Massachusetts", "Boston", 6974258, "Mayflower"],
        ["Michigan", "Lansing", 10030722, "Apple Blossom"],
        ["Minnesota", "St. Paul", 5722897, "Pink and White Lady's Slipper"],
        ["Mississippi", "Jackson", 2930528, "Magnolia"],
        ["Missouri", "Jefferson City", 6186091, "Hawthorn"],
        ["Montana", "Helena", 1139507, "Bitterroot"],
        ["Nebraska", "Lincoln", 1972292, "Goldenrod"],
        ["Nevada", "Carson City", 3209142, "Sagebrush"],
        ["New Hampshire", "Concord", 1402957, "Purple Lilac"],
        ["New Jersey", "Trenton", 9255437, "Purple Violet"],
        ["New Mexico", "Santa Fe", 2110011, "Yucca"],
        ["New York", "Albany", 19496810, "Rose"],
        ["North Carolina", "Raleigh", 10832061, "Dogwood"],
        ["North Dakota", "Bismarck", 780588, "Wild Prairie Rose"],
        ["Ohio", "Columbus", 11747774, "Scarlet Carnation"],
        ["Oklahoma", "Oklahoma City", 4048375, "Oklahoma Rose"],
        ["Oregon", "Salem", 4223973, "Oregon Grape"],
        ["Pennsylvania", "Harrisburg", 12931957, "Mountain Laurel"],
        ["Rhode Island", "Providence", 1090483, "Violet"],
        ["South Carolina", "Columbia", 5372002, "Yellow Jessamine"],
        ["South Dakota", "Pierre", 923484, "Pasque Flower"],
        ["Tennessee", "Nashville", 7134327, "Iris"],
        ["Texas", "Austin", 30500280, "Bluebonnet"],
        ["Utah", "Salt Lake City", 3422487, "Sego Lily"],
        ["Vermont", "Montpelier", 647156, "Red Clover"],
        ["Virginia", "Richmond", 8709873, "American Dogwood"],
        ["Washington", "Olympia", 7830827, "Western Rhododendron"],
        ["West Virginia", "Charleston", 1764786, "Rhododendron"],
        ["Wisconsin", "Madison", 5904977, "Wood Violet"],
        ["Wyoming", "Cheyenne", 583279, "Indian Paintbrush"]
    ]
    is_program_running: bool = True
    user_choice: int
    while is_program_running:
        print_menu()
        user_choice = get_integer(1, 5)
        is_program_running, states_info = process_choice(user_choice, states_info)
