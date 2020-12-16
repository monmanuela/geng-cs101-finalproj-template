# FINAL PROJECT Q1 - HANGMAN
# Generation Girl Winter Club 2020 - CS101 English Class
# Mentors: Johanna Gunawan, Monika Manuela Hengki
# TAs: Saskia Latievarya, Shafira Naya Aprisadianti

# Developer: <PUT YOUR NAME HERE>

import random

# Opening message to users
print(...)

# List of of words (up to you!)
words = [...]

# Pick a random word from the list above
rand = ... # Generate a random index of the list
chosen_word = ... # Use rand and the list

# Print the underscores in hangman fashion: e.g. 'hello' -> '_ _ _ _ _'
for ...:
  print(...)

# List of boolean to track whether each letter has been guessed previously
is_letter_guessed = [False] * 26

# Variable to keep track of the number of lives left
lives = ...

# While the user hasn't run out of lives, keep asking for a guess
while ...:
  # Ask the user to guess a letter
  guess = ...

  # Input validation - must be 1 letter only and is an alphabet (i.e. 'a' to 'z' only)
  if ...:
    print('Invalid guess, please enter 1 alphabet only')
    continue
  
  # Convert guess to a lowercase letter to keep it simple
  guess = guess.lower()

  # Get the number corresponding to the letter: e.g. 'a' is 0, 'b' is 1, etc.
  number = ord(guess) - 97

  # Check if this letter has been guessed previously
  if ...:
    print('You have guessed this letter before, try another one!')
    continue
  
  # Mark the letter as guessed
  ...

  # Check for wrong guess (the letter does not exist in the word)
  if ...:
    # Reduce the number of lives
    ...
    print('Wrong guess, {} lives left'.format(lives))

  # Print the letters or underscores: e.g. 'hello' and 'l', 'e' were guessed previously -> '_ e l l _'
  is_all_revealed = True
  for letter in chosen_word:
    number = ord(letter) - 97
    
    # Print the letter if it has been guessed before
    if ...:
      print(...)
    
    # Print an underscore otherwise
    else:
      is_all_revealed = False
      print(...)
  
  # Break if we have guessed all the letters
  if ...:
    print('Congrats!')
    break
