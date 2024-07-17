# Problem Set 2, hangman.py
# Name: Gustavo S. Maeda

# Hangman Game
# -----------------------------------

import random
import string
from pathlib import Path

WORDLIST_FILEPATH = Path(__file__).with_name('words.txt')

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILEPATH, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guess = ""
    for char in secret_word:
        for letter in letters_guessed:
            if char == letter:
                guess += char
            else:
                continue
    
    return guess == secret_word

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    show_letters = []
    for char in secret_word:
        show_letters.append("_ ")
    
    for letter in letters_guessed:
        for count,char in enumerate(secret_word):
            if letter == char:
                show_letters[count] = letter
    
    show_letters_str = ''.join(show_letters)
    
    return show_letters_str

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    for letter in letters_guessed:
      if letter in alphabet:
        alphabet.remove(letter)
      else:
        pass
        
    available_letters = alphabet
    
    return available_letters
    
def hangman(secret_word):
    guesses_remaining = 6
    letters_guessed = []
    print("The secret word has %d letters. You start with 6 guesses." % len(secret_word))
    
    while guesses_remaining > 0:
      if(is_word_guessed(secret_word, letters_guessed)):
        break
      else:
        print("You have %d guesses remaining" % guesses_remaining)
        letter = input("Guess a letter: ")
        letters_guessed.append(letter)
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: ", available_letters)
        if letter not in secret_word:
            guesses_remaining -= 1
            print("Invalid guess. Now you have %d guesses" %guesses_remaining)
        print(get_guessed_word(secret_word, letters_guessed))
    
    if is_word_guessed(secret_word, letters_guessed):
      print("-----------------------------------------------")
      print("Congratulations, you won!")
    else:
      print("------------------------------------------------")
      print("You ran out of guesses. Better luck next time.")
      print(f"The secret word was {secret_word}")

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)
