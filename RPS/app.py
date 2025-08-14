import random


def play(choice):
    rps = ["rock", "paper", "scissors"]
    compChoice = random.choice(rps)

    print(f"Computer chose: {compChoice}")

    if choice == compChoice:
        print("It's a tie")
    elif (
        (choice == "rock" and compChoice == "scissors")
        or (choice == "paper" and compChoice == "rock")
        or (choice == "scissors" and compChoice == "paper")
    ):
        print("You won!")
    else:
        print("you lose!")


userChoice = input("rock, paper or scissors?").lower()
play(userChoice)
