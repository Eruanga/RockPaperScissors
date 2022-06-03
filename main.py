import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("Computers turn: ", computer)
        print("Players turn: ", player)
        print("Its a Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computers turn: ", computer)
            print("Players turn: ", player)
            print("You lose!")
        if computer == "scissors":
            print("Computers turn: ", computer)
            print("Players turn: ", player)
            print("You Win!")

    elif player == "scissors":
        if computer == "rock":
            print("Computers turn: ", computer)
            print("Players turn: ", player)
            print("You lose!")
        if computer == "paper":
            print("Computers turn: ", computer)
            print("Players turn: ", player)
            print("You Win!")

    elif player == "paper":
        if computer == "scissors":
            print("Computers turn: ", computer)
            print("Players turn: ", player)
            print("You lose!")
        if computer == "rock":
            print("Computers turn: ", computer)
            print("Players turn: ", player)
            print("You Win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Thanks for playing")
