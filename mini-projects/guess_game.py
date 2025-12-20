import random

def number_guessing_game():
    """
    A simple number guessing game in Python.
    The user tries to guess a randomly generated number.
    """
    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Loop until the user guesses the correct number
    while guess != secret_number:
        try:
            # Get user input and convert it to an integer
            guess_input = input("Enter your guess: ")
            guess = int(guess_input)
            attempts += 1

            # Provide feedback on the guess
            if guess < secret_number:
                print("Too low, try a higher number.\n")
            elif guess > secret_number:
                print("Too high, try a lower number.\n")
        except ValueError:
            # Handle cases where the user enters non-integer input
            print("Invalid input. Please enter a valid integer number.")

    # This code executes once the while loop breaks (i.e., the guess is correct)
    print(f"Congratulations! You guessed the number {secret_number} correctly!")
    print(f"It took you {attempts} attempts.")

if __name__ == "__main__":
    number_guessing_game()
