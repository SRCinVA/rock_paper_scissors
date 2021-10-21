import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock, paper, scissors, or q (to quit): ").lower()

    if user_input == "q":
        break  # this will end the while loop and bring us down to "goodbye"

    # clever: he set up all options into one list and is just checking if the content is in there
    if user_input not in options:
        continue  # ... which just asks them to type in something valid
    
    random_number = random.randint(0,2) # 0 is rock, 1 is paper, and 2 is scissors
    computer_pick = options[random_number] # it just pulls an index randomly from the list
    print("The computer", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a tie!!")

    else:
        print("You lost!!")
        computer_wins += 1

print("Goodbye!")
