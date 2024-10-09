# CS101 Midterm 
# Group 3
# Kayden Roberts and Vy Tran
# This program will ask the user a series of questions and based on the answers assign them to a certain house
# You will also have the option to get a brief introduction of the different housing options
# We will prompt the user to enter numbers to navigate through the menus and to answer the questions
def starting_menu():
    # Display the starting menu to the users.
    print("Welcome to The Tianyuan Academy of Magic housing assignment!")
    print("1. Introduce the Houses")
    print("2. Take the Quiz")
    print("3. Exit")

def house_introduction():
    # Introduce each of the houses to the user
    print("\nHouse Introductions:")
    print("1. Dragon House: Power, leadership, ambition, nobility.")
    print("2. Phoenix House: Hope, resilience, grace, creativity.")
    print("3. Tiger House: Honor, bravery, loyalty.")
    print("4. Fox House: Cunning, wit, charm.\n")

def quiz_questions():
    # Ask the user a series of questions inside the array to determine their house
    questions = [
        "I feel I can take charge a lead a group succesfully (1. Strongly Agree 2. Agree 3. Disagree 4. Strongly Disagree): "
    ]

    # Create a dictionary to store the scores of each house
scores = {"Dragon House": 0, "Phoenix House": 0, "Tiger House": 0, "Fox House": 0}

