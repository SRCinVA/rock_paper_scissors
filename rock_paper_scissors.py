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
        


print("Goodbye!")
