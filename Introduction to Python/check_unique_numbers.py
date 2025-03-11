#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

from collections import Counter

# Function to check if all elements in a sequence are unique
def are_all_unique(sequence):
    """Check if all elements in a sequence are unique."""
    return len(sequence) == len(set(sequence))

# Prompt the user for input and validate it
if __name__ == "__main__":
    """Prompt user for numbers, check uniqueness, and display duplicate frequencies if any."""
    while True:
        try:
            # Replace commas with spaces, split by whitespace, and strip extra spaces
            numbers_input = input("Enter numbers separated by spaces or commas to get unique numbers:").strip()
            numbers_split = [num.strip() for num in numbers_input.replace(',', ' ').split() if num.strip()]
            
            # Convert inputs to integers
            numbers = list(map(int, numbers_split))
            break  # Exit loop on valid input
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces or commas.")

    # Check uniqueness and handle duplicates
    if are_all_unique(numbers):
        print("All numbers are unique.")
    else:
        print("There are duplicate numbers.")
        frequency = Counter(numbers)
        print("Frequency of duplicate numbers:")
        for num, count in frequency.items():
            if count > 1:
                print(f"Number {num}: {count} times.")
