import random


secret_number = random.randint(1, 100)

# Ask the user to guess the number
guess = int(input("Guess the number between 1 and 100: "))


if guess == secret_number:
    print("Congratulations! You guessed the number correctly!")
else:
    print("Sorry, the number was", secret_number)


# You can try modifying this by giving user no of attempts before game over, hints etc