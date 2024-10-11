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
        "I feel I can take charge a lead a group succesfully (1. Strongly Agree 2. Agree 3. Disagree 4. Strongly Disagree): ",
        "When I'm dead I want people to remember me as: (1. The Good 2. The Great 3. The Wise 4. The Bold): ",
        "Are you a night owl or an early bird? (1. Night Owl 2. Early Bird 3. It doesn't matter): ",
        "Which of these traits do you value the most? (1. Power 2. Creativity 3. Loyalty 4. Wit): ",
        "My friends would describe me as: (1. Ambitious 2. Creative 3. Loyal 4. Witty): ",
        "If I got reincarnated, I would want to be: (1. A Dragon 2. A Phoenix 3. A Tiger 4. A Fox): ",
        "How is success best achieved? (1. Through power 2. Through resilience 3. Through honor 4. Through Cleverness): ",
        "I handle stress by (1. Taking charge 2. Being creative 3. Relying on others 4. Thinking my way out): ",
        "I would rather be (1. Feared 2. Loved 3. Respected 4. Admired): "
    ]

    # Create a dictionary to store the scores of each house
scores = {"Dragon House": 0, "Phoenix House": 0, "Tiger House": 0, "Fox House": 0}

# Create validation function to ensure that the user input is within the guidelines
# Display the question to the user if the user input is valid add the score if not valid display an error message
def validate_input(prompt, valid_options):
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        else:
            print("Invalid input. Please try again.")

# Loop through the questions and add the score to the correct house
# Using the validate_input function to ensure the user input is valid
# Question arugment shows the user the question prompt the array of numbers are the valid options
for question in questions:
    answer = validate_input(question, ['1', '2', '3', '4'])
    if answer == '1':
        scores["Dragon House"] += 1
    elif answer == '2':
        scores["Phoenix House"] += 1
    elif answer == '3':
        scores["Tiger House"] += 1
    elif answer == '4':
        scores["Fox House"] += 1

