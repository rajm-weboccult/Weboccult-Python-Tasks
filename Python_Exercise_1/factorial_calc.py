#Create a Python program to calculate the factorial of a given number. Use both iterative and recursive approaches.

"""
Python program to calculate factorial using iterative and recursive approaches.
"""

import math

# Function to calculate factorial iteratively using the Gamma function
def factorial_iterative(n):
    """Calculate factorial iteratively using math.gamma."""
    return math.gamma(n + 1)

# Function to calculate factorial recursively (only for integers)
def factorial_recursive(n):
    """Calculate factorial recursively."""
    return 1 if n <= 1 else n * factorial_recursive(n - 1)

# Function to get a valid non-negative number from the user
def get_valid_number():
    """Prompt user for a valid non-negative number."""
    while True:
        try:
            number = float(input("Enter a non-negative number to calculate its factorial: "))
            if number < 0:
                print("Factorial is not defined for negative numbers. Please try again.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid non-negative number.")

# Main program execution
if __name__ == "__main__":
    """Main program to calculate and display factorial."""
    number = get_valid_number()
    
    # Check if the input is an integer or a float
    if number.is_integer():  # Input is an integer (e.g., 5.0 is treated as 5)
        int_number = int(number)
        print(f"Iterative Factorial ({int_number}):", factorial_iterative(int_number))
        print(f"Recursive Factorial ({int_number}):", factorial_recursive(int_number))
    else:  # Input is a non-integer float (e.g., 2.2)
        print(f"Iterative Factorial ({number}):", factorial_iterative(number))