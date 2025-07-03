import random

# Predefined list of 5 words
word_list = ['apple', 'tiger', 'chair', 'bread', 'house']

# Randomly select a word from the list
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to the Word Guessing Game!")
print("You have 6 chances to guess the word.\n")

# Main game loop
while incorrect_guesses < max_attempts:
    # Display current state of guessed word
    display_word = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_'
    print("Word:", display_word)

    # Check if the user has guessed the whole word
    if display_word == secret_word:
        print("🎉 Congratulations! You've guessed the word correctly!")
        break

    # Ask the player for a letter
    guess = input("Guess a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.\n")
        continue

    # If the letter was already guessed
    if guess in guessed_letters:
        print("❗ You already guessed that letter. Try again.\n")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Good guess!\n")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_attempts - incorrect_guesses} attempts left.\n")

# If the player used all attempts
if incorrect_guesses == max_attempts:
    print(f"💀 Game Over! The word was '{secret_word}'.")
