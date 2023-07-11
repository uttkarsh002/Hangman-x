import random

# List of words to choose from
words = ["apple", "banana", "cherry", "orange", "mango"]

# Select a random word from the list
secret_word = random.choice(words)

# Create a list to store the player's correct guesses
correct_guesses = ["_"] * len(secret_word)

# Set the number of attempts
max_attempts = 6
attempts = 0

print("Welcome to Hangman!")
print("Try to guess the secret word.")

# Game loop
while attempts < max_attempts:
    # Print the current state of the word
    print(" ".join(correct_guesses))

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is correct
    if guess in secret_word:
        # Update the correct_guesses list with the correct guess
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                correct_guesses[i] = guess
    else:
        print("Incorrect guess!")
        attempts += 1

    # Check if the player has guessed the entire word
    if "_" not in correct_guesses:
        print("Congratulations! You guessed the word:", secret_word)
        break

    # Check if the player has used all their attempts
    if attempts == max_attempts:
        print("Game over! The word was:", secret_word)
