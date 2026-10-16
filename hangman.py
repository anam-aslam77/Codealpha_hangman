# Hangman in Python
import random

words = ("Limitless", "sledge", "AUDI SUV", "lamborghini", "bhugatti")

# Dictionary of hangman drawings
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}


def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print("The answer was:", answer)


def main():
    answer = random.choice(words).lower()

    hint = [" " if letter == " " else "_" for letter in answer]

    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        print("Guessed letters:",
              ", ".join(sorted(guessed_letters)) or "None")

        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter one letter.")
            continue

        # Check repeated guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        # Check the guessed letter
        if guess in answer:
            print("Correct guess!")

            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            print("Wrong guess!")
            wrong_guesses += 1

        # Check winning condition
        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False

        # Check losing condition
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()