#Guess the number

import random

secret_number = random.randint(1, 20)
attempts = 0

print("==== GUESS THE NUMBER ===")
print("Guess a number between 1 and 20!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"You won in {attempts} attempts!")
        break

    elif guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")