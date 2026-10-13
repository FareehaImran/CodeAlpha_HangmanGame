import random

WORDS = ["code", "program", "computer", "compiler", "python"]
MAX_WRONG = 6

def show_status(word, guessed, wrong_count):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    print("Wrong guesses left:", MAX_WRONG - wrong_count)
    print("Letters tried:", " ".join(sorted(guessed)) if guessed else "none")

def play():
    word = random.choice(WORDS)
    guessed = []
    wrong_count = 0

    print("========= HANGMAN =========")
    print("Guess the word one letter at a time. You get", MAX_WRONG, "wrong guesses.")

    while wrong_count < MAX_WRONG:
        show_status(word, guessed, wrong_count)

        # Check for Win
        if all(letter in guessed for letter in word):
            print("\nYou Won! The Word was:", word)
            return

        guess = input("Enter a letter: ").lower().strip()

        # Invalid Input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed:
            print("You already guessed this letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            wrong_count += 1
            print("Wrong guess!")

    print("\nGame Over! The word was:", word)

def main():
    while True:
        play()
        again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if again != "y":
            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    main()


