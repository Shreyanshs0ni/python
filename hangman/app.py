import random
import string
from words import words  # Make sure words.py has a list named 'words'


def getValidWord(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = getValidWord(words)
    word_letters = set(word)  # letters to guess
    alphabets = set(string.ascii_uppercase)
    used_letters = set()  # guessed letters
    lives = 6

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show current progress
        print(
            f"\nYou have {lives} lives left and used letters: {' '.join(sorted(used_letters))}"
        )

        # Display current word with underscores for missing letters
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current Word: ", " ".join(word_list))

        # Get user guess
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Letter '{user_letter}' not in word.")
        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character. Please enter a letter.")

    # End game messages
    if lives == 0:
        print(f"\nYou died! The word was: {word}")
    else:
        print(f"\nYou guessed the word {word} !!")


hangman()
