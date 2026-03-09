'''
TASK 1: Hangman Game

Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.

Simplified Scope: 
    ● Use a small list of 5 predefined words (no need to use a file or API). 
    ● Limit incorrect guesses to 6.
    ● Basic console input/output — no graphics or audio.

Key Concepts Used: random, while loop, if-else, strings, lists.
'''
import random

list_of_words = ['python', 'hangman', 'coding', 'program', 'laptop']

list_of_words = random.choice(list_of_words)
word_length = len(list_of_words)

# list for storing guessed alphabets
guessed_alpha = []

# initializing no. of wrong guesses
wrong_guesses = 0

# no. of maximum guesses allowed
max_guesses = 6 

display_word = ['_' for _ in list_of_words]
display_word = ["_"] * word_length
print("Welcome to Hangman Game!")
print("Guess the word by entering one letter at a time.")
print(f"You have {max_guesses} wrong guesses allowed.")
print("Word to guess: " + ' '.join(display_word))
print(f"The word has {word_length} letters.")

# main loop: while loop with main execution

while wrong_guesses < max_guesses and '_' in display_word:
    guess = input("Enter an alphabet to guess the word: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical character at a time.")
        continue

    if guess in guessed_alpha:
        print("You've already guessed that alphabet. Try another alphabet.")
        continue

    guessed_alpha.append(guess)

    # Correct guess
    if guess in list_of_words:
        print("Correct guess!")
        for i in range(len(list_of_words)):
            if list_of_words[i] == guess:
                display_word[i] = guess
    # Wrong guess
    else:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_guesses - wrong_guesses} tries left.")

# Game End (Post-loop)
    print("_" * 50)
    print("Word: " + ' '.join(display_word))
    print("Guessed alphabets: " + ', '.join(guessed_alpha))
    print()
   
# Final outcome
if '_' not in display_word:
    print("Congratulations! You guessed the word:", list_of_words)
else:
    print("Game over! The word was:", list_of_words)
























