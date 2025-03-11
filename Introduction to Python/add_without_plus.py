def add_without_plus(a, b):
    """Return sum of two numbers without using '+' operator.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: Sum of the two numbers.
    """
    # Using subtraction of negative to achieve addition
    return a - (-b)


def get_number(prompt):
    """Prompt user for a number, ensuring valid numerical input.

    Args:
        prompt (str): The input prompt displayed to the user.

    Returns:
        float: A valid numerical input from the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """Main function to execute the addition without '+' operator."""
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    result = add_without_plus(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
