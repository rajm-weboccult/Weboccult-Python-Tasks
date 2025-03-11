import math

def find_common_divisors(a, b):
    """
    Find all common divisors between two positive integers.
    
    Args:
        a, b: Positive integers
        
    Returns:
        A list of common divisors
    """
    smaller = min(a, b)
    common_divisors = set()

    # Check divisors from 1 up to the square root of the smaller number
    for i in range(1, int(math.sqrt(smaller)) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.add(i)
            if i != a // i and a // i <= smaller and a % (a // i) == 0 and b % (a // i) == 0:
                common_divisors.add(a // i)
                
    return sorted(common_divisors)

def get_positive_integer(prompt):
    """Prompt the user for a positive integer and validate input."""
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                print("Please enter a positive integer.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
print("To find common divisors of following numbers")

# User input for integers a and b
a = get_positive_integer("Enter the first positive integer: ")
b = get_positive_integer("Enter the second positive integer: ")

# Get common divisors and display the result
common_divisors = find_common_divisors(a, b)
print(f"The common divisors of {a} and {b} are: {common_divisors}")

