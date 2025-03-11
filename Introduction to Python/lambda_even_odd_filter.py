def filter_even_odd(numbers):
    """Filter the list into even and odd numbers."""
    # Using lambda to filter even and odd numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    
    return even_numbers, odd_numbers

print("To get the seperate list of odd and even numbers of following")

def get_integer_list():
    """Prompt the user to input a list of integers (comma or space separated)."""
    while True:
        try:
            # Take input as a string (comma or space-separated)
            input_list = input("Enter a list of integers (comma or space separated): ")
            # Split by either comma or space
            numbers = [int(x.strip()) for x in input_list.replace(',', ' ').split()]
            return numbers
        except ValueError:
            print("Invalid input. Please enter a valid list of integers.")

# User input for list of integers
numbers = get_integer_list()

# Filter even and odd numbers
even_numbers, odd_numbers = filter_even_odd(numbers)

# Output the results
print(f"Even: {even_numbers}")
print(f"Odd: {odd_numbers}")
