import random


# Predefined list of words
WORDS = ["python", "laptop", "coding", "planet", "school"]

MAX_WRONG_GUESSES = 6


def display_word(word, guessed_letters):
    """
    Display the word with guessed letters
    and hide the letters that haven't been guessed.
    """
    displayed_word = ""

    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    return displayed_word.strip()


def play_game():
    # Select a random word from the list
    word = random.choice(WORDS)

    # Store letters guessed by the player
    guessed_letters = []

    # Store incorrect guesses
    wrong_letters = []

    wrong_guesses = 0

    print("\n" + "=" * 40)
    print("        WELCOME TO HANGMAN")
    print("=" * 40)

    print(f"\nYou have {MAX_WRONG_GUESSES} incorrect guesses.")
    print("Guess the word one letter at a time.")

    # Main game loop
    while wrong_guesses < MAX_WRONG_GUESSES:

        # Display current progress
        print("\nWord:", display_word(word, guessed_letters))

        if wrong_letters:
            print("Wrong letters:", ", ".join(wrong_letters))
        else:
            print("Wrong letters: None")

        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print("\n Congratulations!")
            print(f"You guessed the word: {word}")
            return

        # Get player's guess
        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1:
            print(" Please enter exactly one letter.")
            continue

        if not guess.isalpha():
            print("Please enter a letter, not a number or symbol.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter.")
            continue

        # Correct guess
        if guess in word:
            guessed_letters.append(guess)
            print("Correct guess!")

        # Incorrect guess
        else:
            wrong_letters.append(guess)
            wrong_guesses += 1

            remaining = MAX_WRONG_GUESSES - wrong_guesses

            print("Incorrect guess!")
            print(f"Remaining incorrect guesses: {remaining}")

    # Player lost
    print("\n" + "=" * 40)
    print("           GAME OVER")
    print("=" * 40)
    print(f"The word was: {word}")
    print("Better luck next time!")


def main():
    """
    Run the game and allow the player
    to play multiple rounds.
    """

    while True:
        play_game()

        print("\nWould you like to play again?")
        choice = input("Enter 'y' for yes or 'n' for no: ").lower().strip()

        if choice == "n":
            print("\nThanks for playing Hangman! 👋")
            break

        elif choice != "y":
            print("Invalid choice. Ending the game.")
            break


# Start the program
if __name__ == "__main__":
    main()