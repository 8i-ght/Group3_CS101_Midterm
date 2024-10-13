def starting_menu():

        print('Greetings, my aspiring magic users! The Tianyuan Academy of Magic has been a sanctuary for wizards, witches, and sorcerers for centuries, and we are thrilled to invite you to become a part of our enchanting community. You are about to be embark on a magical journey.')
    
        print("1. Introduce the Houses")
        print("2. Take the Quiz")
        print("3. Exit")

def house_introduction():

        print("\nHouse Introductions:")
        print("1. Dragon House: Power, Leadership, Ambition and Nobility.")
        print("2. Phoenix House: Hope, Resilience, Grace, Creativity.")
        print("3. Tiger House: Honor, Bravery, and Loyalty.")
        print("4. Fox House: Cunning, Wit, Charm\n")

def validate_input(question_prompt, valid_options):
    while True:
        choice = input(question_prompt)
        if choice in valid_options:
            return choice
        else:
            print("Invalid input. Please try again.")


def start_quiz():
    
    def validate_answer(question, valid_answer): 
        while True:
            answer = input(question)
            if answer in valid_answer:
                return answer

    bravery = input("Do you face your fear? (yes/no): ").strip().lower()
    cunning = input("Are you clever and skillful at achieving your goals by tricking or deceiving others? (yes/no): ").strip().lower()
    loyalty = input("Are you faithful and steadfast in their allegiance to a person, cause, or ideal, even when faced with temptation to betray or desert? (yes/no): ").strip().lower()
    ambition = input("Are you always striving to reach for a goal? (yes/no): ").strip().lower()
    nobility = input("As a member of the society, do you belong in the highest social class? (yes/no): ").strip().lower()
    honor = input("Do you have a strong sense of what is right and wrong, and try to live up to those principles? (yes/no): ").strip().lower()
    charm = input("Does other people find you charismatic? (yes/no): ").strip().lower()
    hope = input("At any circumstances, do you have a positive outlook and are persistence? (yes/no): ").strip().lower()
    resilience = input("When faced with a difficult situation, are you able to adapt and recover from it? (yes/no): ").strip().lower()
    creativity = input("Can you come up with original ideas and use them to create new things, often in an imaginative way? (yes/no): ").strip().lower()
    wit = input("? (yes/no): ").strip().lower()
  


    if bravery == "yes" and ambition == "yes" and nobility == "yes":
        house = "Dragon"
    elif hope == "yes" and resilience == "yes" and creativity == "yes" :
        house = "Phoenix"
    elif honor == "yes" and bravery == "yes" and loyalty == "yes":
        house = "Tiger"
    elif cunning == "yes" and wit == "yes" and charm == "yes":
        house = "Fox"
    else:
        house = "Unknown"

    print(house)


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
