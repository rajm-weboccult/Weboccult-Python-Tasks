#Write a Python function that takes a list of words and returns a new list with all words that start with a vowel.

import re

# Function to filter words starting with vowels
def filter_vowel_words(words):
    """Filter and return words that start with a vowel."""
    vowels = 'aeiou'
    return [word for word in words if word and word[0].lower() in vowels]

# Input processing and filtering
if __name__ == "__main__":
    """Extract words from input, filter those starting with vowels, and display the result."""
    words_input = input("Enter words: ")
    # Use regex to extract clean words (allowing apostrophes within words)
    words = re.findall(r"\b[\w']+\b", words_input.lower())  # Convert to lowercase for case-insensitivity
    
    # Filter words starting with vowels
    filtered_words = filter_vowel_words(words)
    print("Words starting with vowels:", filtered_words)