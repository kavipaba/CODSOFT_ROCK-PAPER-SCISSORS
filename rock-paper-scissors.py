import random

options = ("rock","paper","scissors")
running = True

while running:

    player = None
    computer = random.choice(options)
 
    while player not in options:
        player = input("Enter a choice (rock,paper,scissors):")
  #wrong input
        if player not in options:
            print("Your input is not valid. Please enter 'rock', 'paper', or 'scissors'.")
            
    print(f"Player: {player}")
    print(f"Computer: {computer}")
  #answers
    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose")

    if not input("Play Again? (y/n):").lower() == "y":
        running = False

print("Thank You for Playing!")    