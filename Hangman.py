import random

# List of predefined words
words = ["python", "computer", "programming", "keyboard", "internet"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""

    # Display the word
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    # Check if the player won
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter!")

    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")

    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("Wrong guess!")

# If attempts become 0
if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)
