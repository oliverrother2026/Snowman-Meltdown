import random

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Select a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Show the current snowman and guessing progress."""
    print("\n" + "=" * 30)
    print(STAGES[mistakes])

    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    wrong_letters = [
        letter for letter in guessed_letters if letter not in secret_word
    ]

    print("Word:         ", display_word)
    print("Wrong letters:", ", ".join(wrong_letters) or "none")
    print(f"Mistakes:      {mistakes}/{len(STAGES) - 1}")
    print("=" * 30)


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
