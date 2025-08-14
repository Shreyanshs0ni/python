import random


def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"The guess is {guess}, higher(h), lower(l) or correct(c)?"
        ).lower()
        if feedback == "h":
            low = guess + 1
        elif feedback == "l":
            high = guess - 1

    print("Woohooo!")


computer_guess(100)
