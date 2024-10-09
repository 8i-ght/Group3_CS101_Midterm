# main.py

def display_menu():
    """
    Display the main menu to the user.
    """
    print("Welcome to the Wizard House Assignment Program!")
    print("1. Introduce the Houses")
    print("2. Take the Quiz")
    print("3. Exit")

def introduce_houses():
    """
    Introduce each house to the user.
    """
    print("\nHouse Introductions:")
    print("1. Gryffindor: Brave and daring.")
    print("2. Hufflepuff: Loyal and hardworking.")
    print("3. Ravenclaw: Wise and witty.")
    print("4. Slytherin: Ambitious and cunning.\n")

def validate_input(prompt, valid_options):
    """
    Validate user input to ensure it is within the valid options.
    """
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        else:
            print("Invalid input. Please try again.")

def start_quiz():
    """
    Conduct the quiz and assign the user to a house based on their answers.
    """
    questions = [
        "Do you prefer dawn or dusk? (1. Dawn, 2. Dusk): ",
        "When I'm dead, I want people to remember me as: (1. The Good, 2. The Great, 3. The Wise, 4. The Bold): ",
        "Which instrument pleases your ear the most? (1. Violin, 2. Trumpet, 3. Piano, 4. Drum): ",
        "Which road tempts you the most? (1. The wide, sunny grassy lane, 2. The narrow, dark, lantern-lit alley, 3. The twisting, leaf-strewn path through woods, 4. The cobbled street lined with ancient buildings): ",
        "Do you prefer: (1. Forest, 2. River): ",
        "Which would you rather be: (1. Liked, 2. Imitated, 3. Trusted, 4. Praised): ",
        "Which of the following do you find most difficult to deal with? (1. Hunger, 2. Cold, 3. Loneliness, 4. Boredom): ",
        "Which would you rather be: (1. Envied, 2. Feared, 3. Liked, 4. Praised): "
    ]

    scores = {"Gryffindor": 0, "Hufflepuff": 0, "Ravenclaw": 0, "Slytherin": 0}

    for question in questions:
        answer = validate_input(question, ['1', '2', '3', '4'])
        if answer == '1':
            scores["Gryffindor"] += 1
        elif answer == '2':
            scores["Hufflepuff"] += 1
        elif answer == '3':
            scores["Ravenclaw"] += 1
        elif answer == '4':
            scores["Slytherin"] += 1

    assign_house(scores)

def assign_house(scores):
    """
    Assign the user to a house based on their quiz scores.
    """
    house = max(scores, key=scores.get)
    print(f"\nCongratulations! You have been assigned to {house}!")

def main():
    """
    Main function to run the program.
    """
    while True:
        display_menu()
        choice = validate_input("Please choose an option (1-3): ", ['1', '2', '3'])
        if choice == '1':
            introduce_houses()
        elif choice == '2':
            start_quiz()
        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()