import random

class InvalidInputError(Exception):
    """Custom exception for invalid user input."""
    def __init__(self, message="Invalid input ❌. Please enter an integer between 1 and 10."):
        super().__init__(message)

def generate_secret_number():
    return random.randint(1, 10)

def validate_input(user_input):
    try:
        number = int(user_input)
        if 1 <= number <= 10:
            return number
        raise InvalidInputError()
    except ValueError:
        raise InvalidInputError()

def play_game():
    secret_number, max_attempts, attempts = generate_secret_number(), 5, 0
    print(f"\nYou have {max_attempts} attempts to guess the secret number.🎲")
    while attempts < max_attempts:
        try:
            guess = validate_input(input("Guess the secret number (between 1 and 10): 🔢 "))
            attempts += 1
            if guess == secret_number:
                print(f"Congratulations! 🎉 You guessed the correct number in {attempts} attempt(s).")
                return attempts
            remaining = max_attempts - attempts
            print(f"Wrong guess. ❌ {'You have {} attempt(s) left.'.format(remaining) if remaining else f'Sorry, you failed. The secret number was {secret_number}.'}")
        except InvalidInputError as e:
            print(e)
    print("Your score: 0 😔")
    return 0

def main():
    print("\nWelcome to the Number Guessing Game! 🎮")
    while True:
        score = play_game()
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again in ('yes', 'y'):
                break
            elif play_again in ('no', 'n'):
                print(f"\nThanks for playing! 👋 Your final score was {score}.")
                return
            print("Invalid input ❌. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()