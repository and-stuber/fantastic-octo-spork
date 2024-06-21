import itertools
from collections import Counter

# List of letters provided
letters = ['A', 'E', 'D', 'T', 'P', 'S', 'M']

# Read the dictionary file (assume it's a txt file with one word per line)
with open('/usr/share/dict/brazilian') as f:
    words = f.read().splitlines()

# Function to check if a word can be formed with the given letters
def can_form_word(word, letters_count):
    word_count = Counter(word)
    return all(word_count[char] <= letters_count[char] for char in word_count)

# Filter words with 11 letters that can be formed from the given letters
letters_count = Counter(letters)
valid_words = [word for word in words if len(word) == 11 and can_form_word(word.upper(), letters_count)]

# Display the valid words
valid_words
