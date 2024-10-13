# CS101 Midterm 
# Group 3
# Kayden Roberts and Vy Tran
# This program will ask the user a series of questions and based on the answers assign them to a certain house
# You will also have the option to get a brief introduction of the different housing options
# We will prompt the user to enter numbers to navigate through the menus and to answer the questions
def starting_menu():
        print('\nGreetings, my aspiring magic users! The Tianyuan Academy of Magic has been a sanctuary for wizards, witches, and sorcerers for centuries, and we are thrilled to invite you to become a part of our enchanting community. You are about to be embark on a magical journey.')
        print("1. Introduce the Houses")
        print("2. Take the Quiz")
        print("3. Exit")
# Introductions to all the houses
def house_introduction():
        print("\nHouse Introductions:")
        print("1. Dragon House: Power, Leadership, Ambition and Nobility.")
        print("2. Phoenix House: Hope, Resilience, Grace, Creativity.")
        print("3. Tiger House: Honor, Bravery, and Loyalty.")
        print("4. Fox House: Cunning, Wit, Charm\n")

# Validator for menu navigation
def validate_input(question_prompt, valid_options):
    while True:
        choice = input(question_prompt)
        if choice in valid_options:
            return choice
        else:
            print("Invalid input. Please try again.")

# Function to start the quiz and ask the user a series of yes/no questions
def start_quiz():
    # Function to validate the user's answer if not yes/no
    def validate_answer(question, valid_answer): 
        while True:
            answer = input(question)
            if answer in valid_answer:
                return answer
            else: print("Invalid input please try again!")

    bravery = validate_answer("\nDo you face your fear? (yes/no): ", ['yes', 'no']).strip()
    cunning = validate_answer("\nAre you clever and skillful at achieving your goals by tricking or deceiving others? (yes/no): ", ['yes', 'no'])
    loyalty = validate_answer("\nAre you faithful and steadfast in their allegiance to a person, cause, or ideal, even when faced with temptation to betray or desert? (yes/no): ", ['yes', 'no'])
    ambition = validate_answer("\nAre you always striving to reach for a goal? (yes/no): ", ['yes', 'no'])
    nobility = validate_answer("\nAs a member of the society, do you belong in the highest social class? (yes/no): ", ['yes', 'no'])
    honor = validate_answer("\nDo you have a strong sense of what is right and wrong, and try to live up to those principles? (yes/no): ", ['yes', 'no'])
    charm = validate_answer("\nDo other people find you charismatic? (yes/no): ", ['yes', 'no'])
    hope = validate_answer("\nIn any circumstances, do you have a positive outlook and are persistent? (yes/no): ", ['yes', 'no'])
    resilience = validate_answer("\nWhen faced with a difficult situation, are you able to adapt and recover from it? (yes/no): ", ['yes', 'no'])
    creativity = validate_answer("\nCan you come up with original ideas and use them to create new things, often in an imaginative way? (yes/no): ", ['yes', 'no'])
    wit = validate_answer("\nAre you quick and inventive in verbal humor? (yes/no): ", ['yes', 'no'])
  

# Assign the user to a house based on there answers
    if bravery == "yes" and ambition == "yes" and nobility == "yes":
        house = "Dragon"
    elif hope == "yes" and resilience == "yes" and creativity == "yes" :
        house = "Phoenix"
    elif honor == "yes" and bravery == "yes" and loyalty == "yes":
        house = "Tiger"
    elif cunning == "yes" and wit == "yes" and charm == "yes":
        house = "Fox"
    else:
        house = "You don't belong to any"

    print(f"\nCongratulations, you are now a part of the {house} house!")

# Main function for running the program
def main():
     while True:
        starting_menu()
        choice = validate_input("Please choose an option (1-3): ", ['1', '2', '3'])
        if choice == '1':
            house_introduction()
        elif choice == '2':
            start_quiz()
        elif choice == '3':
            print("Thank you for taking the quiz. Goodbye!")
            break
main()