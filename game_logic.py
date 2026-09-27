import random

from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Select a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Show the snowman and the letters guessed so far."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)


def play_game():
    """Run one game of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations, you saved the snowman!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman melted! The word was:", secret_word)