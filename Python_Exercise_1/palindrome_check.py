#Write a Python function to determine whether a given string is a palindrome

def is_palindrome(s):
    """Check if a string is a palindrome, ignoring non-alphanumeric characters and case."""
    # Normalize the string by removing non-alphanumeric characters and converting to lowercase
    change = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the normalized string is equal to its reverse
    return change == change[::-1]

# Prompt the user to input a string
text = input("Enter a word or sentence to check if it's a palindrome: ")

# Print whether the input string is a palindrome or not
print("The string is a palindrome." if is_palindrome(text) else "The string is not a palindrome.")
