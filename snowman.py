"""Start Snowman Meltdown."""

from game_logic import play_game


def main():
    while True:
        play_game()

        while True:
            answer = input("Play again? (y/n): ").lower().strip()
            if answer in ("y", "n"):
                break
            print("Please enter y or n.")

        if answer == "n":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()