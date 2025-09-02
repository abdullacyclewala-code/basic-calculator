import random

target = random.randint(1, 100)
max_attempts = 10

print("Welcome to Number Guessing Game!")
print("Guess the number between 1 and 100.")
print(f"You have {max_attempts} attempts.\n")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess → "))
    
    if guess > target:
        print("Too high! Try again.\n")
    elif guess < target:
        print("Too low! Try again.\n")
    else:
        print(f" Correct! The number was {target}. You guessed it in {attempt} attempts.")
        break
else:
    print(f" Out of attempts! The correct number was {target}.")
    
print("Thanks for playing!")
