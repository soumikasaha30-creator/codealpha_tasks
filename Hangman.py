import random


# List of possible words
words = ["Apple", "Banana", "Cherry", "Fig", "Grape"]

# Randomly choose a word
secret_word = random.choice(words).upper()

# Initialize variables
guessed_letters = []  # list to store guessed letters
attempts_left = 6  # number of chances
word_display = ["_" for _ in secret_word]  # create underscores for the word

print("Welcome to Hangman!")
print("Guess the word before you run out of attempts!")
print(" ".join(word_display))
print()

while attempts_left > 0 and "_" in word_display:
    guess = input("Enter a letter: ").upper()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single valid letter (A-Z).")
        continue

    # if letter already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    #  guessed_letters list
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                word_display[i] = guess
    else:
        attempts_left -= 1
        print(f" Wrong guess! Attempts left: {attempts_left}")

    # Display current progress
    print(" ".join(word_display)) 
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print()

# Check win/lose
if "_" not in word_display:
    print(f" Congratulations! You guessed the word: {secret_word}")
else:
    print(f" Game Over! The word was: {secret_word}")
# End of Hangman Game