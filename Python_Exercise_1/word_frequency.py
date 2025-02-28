#Write a Python program that takes a text input and counts the frequency of each word. Display the result in a dictionary format

from collections import Counter

# Custom function to remove punctuation
def remove_punctuation(text):
    """Remove punctuation from text while preserving apostrophes in contractions."""
    punctuation = set(",.;:\"!?@#$%^&*()-_+=[]{}|\\/<>`~")
    return ''.join(' ' if ch in punctuation else ch for ch in text)

# Input from the user and word frequency calculation
if __name__ == "__main__":
    """Remove punctuation, count word frequencies, and display the results."""
    text_input = input("Enter a sentence or paragraph for getting word frequency in it: ")
    
    # Step 1: Remove punctuation
    clean_txt = remove_punctuation(text_input)
    
    # Step 2: Convert to lowercase and split into words
    words = clean_txt.lower().split()
    
    # Step 3: Count word frequencies
    word_freq = dict(Counter(words))
    
    # Output the results
    print("\nWord Frequencies:")
    for word, count in word_freq.items():
        print(f"{word}: {count}")
