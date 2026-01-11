import random

choices = ["stone", "paper", "scissors"]

while True:
    user = input("\nEnter stone, paper, scissors (or quit): ").lower()
    
    if user == "quit":
        print("Game ended. Thanks for playing!")
        break
    
    if user not in choices:
        print("Invalid choice!")
        continue
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if user == computer:
        print("Tie!")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
