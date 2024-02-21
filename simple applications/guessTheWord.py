import random

# List of words for the game
word_list = ["python", "java", "ruby", "javascript", "html", "css", "php"]

# Select a random word from the list
word = random.choice(word_list)

# Initialize variables
guessed_word = ["_"] * len(word)  # Displayed word with underscores
attempts = 7  # Number of attempts allowed
used_letters = []  # List to store used letters

print("Welcome to the Word Guessing Game!")
print(" ".join(guessed_word))  # Display the initial state of the word

while attempts > 0 and "_" in guessed_word:
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter and not already guessed
    if len(guess) == 1 and guess.isalpha() and guess not in used_letters:
        used_letters.append(guess)

        if guess in word:
            print("Correct!")
            # Update the guessed word with the correct letter
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Incorrect!")
            attempts -= 1

        print("Attempts left:", attempts)
        print(" ".join(guessed_word))  # Display the updated word
        print("Used letters:", ", ".join(used_letters))  # Display used letters
    else:
        print("Invalid input or letter already guessed.")

# Check if the player won or lost
if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Sorry, you ran out of attempts. The word was:", word)
