import random
import string
import logging
import sys

WORDLIST_FILENAME = "palavras.txt"

class WordWorld(object):
    def __init__(self, guesses):
        self.secret_word = self.load_words().lower()
        self.letters_guessed = []
        self.guessed = guesses


    def is_word_guessed(self):
        for letter in self.secret_word:
          if letter in self.letters_guessed:
             pass
          else:
             return False
        return True



    def load_words(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        inFile = open(WORDLIST_FILENAME, 'r', 0)

        try:
           inFile = open(WORDLIST_FILENAME, 'r', 0)
           logging.info ('Opening the file')
        except IOError:
           print'File not found, enter with right File!'
           logging.info ('This file does not exist')
           sys.exit()

        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        word_list = string.split(line)
        print "  ", len(word_list), "words loaded."

        random_word = random.choice(word_list)
        join_letters = ''.join(set(random_word))

        while(len(join_letters) > 8):
           random_choice_word = random.choice(word_list)
        return random_word


    def get_guessed_word(self):
        guessed = ''
        return guessed


    def get_available_letters(self):
      #'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        return available


    def guessed_letter(self, secret_word, letters_guessed):
        guessed = self.get_guessed_word()

        for letter in secret_word:
            if letter in letters_guessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed


    def unite_letters(self, secret_word):
        unite_letters = ''.join(set(secret_word))
        print "This word has ", len(unite_letters), " different letters"


class Hangman(WordWorld):

    def __init__(self, guesses):
        WordWorld.__init__(self, guesses=guesses)

    def hangman_body(self, guesses):
        if guesses == 8:
            print "________      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
            print "|             "

        elif guesses == 7:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "

        elif guesses == 6:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|             "
            print "|             "
            print "|             "

        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|      o      "
            print "|             "
            print "|             "
            print "|             "

        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|      o      "
            print "|      |      "
            print "|             "
            print "|             "

        elif guesses == 3:
            print "________      "
            print "|      ^      "
            print "|      o      "
            print "|     /|      "
            print "|             "
            print "|             "

        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|      o      "
            print "|     /|\     "
            print "|             "
            print "|             "

        elif guesses == 1:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|      o      "
            print "|     /|\     "
            print "|     /       "
            print "|             "

        else:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|     \o/     "
            print "|      |      "
            print "|     / \     "
            print "|             "

def main():

    guesses = 8
    hangman = Hangman(guesses)
    letter_word = WordWorld(guesses)
    letters_guessed = hangman.letters_guessed

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(hangman.secret_word), ' letters long.'
    letter_word.unite_letters(hangman.secret_word)
    print '-------------'

    while not hangman.is_word_guessed() and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        hangman.hangman_body(guesses)

        available = hangman.get_available_letters()
        for letter in available:
            if letter in letters_guessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in letters_guessed:
           letters_guessed.append(letter)
           guessed = letter_word.guessed_letter(hangman.secret_word, letters_guessed)

           print 'Oops! You have already guessed that letter: ', guessed
        elif letter in hangman.secret_word:
            letters_guessed.append(letter)
            guessed = letter_word.guessed_letter(hangman.secret_word, letters_guessed)
            print 'Good Guess: ', guessed
        else:
            guesses -=1
            letters_guessed.append(letter)
            guessed = letter_word.guessed_letter(hangman.secret_word, letters_guessed)

            print 'Oops! That letter is not in my word: ', guessed
        print '------------'

    else:
        if hangman.is_word_guessed():
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', hangman.secret_word, '.'

main()
