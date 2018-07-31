# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #init list of booleans and memoization dict
    boolList = []
    boolDict = {}
    #iterate through each char in secretWord and test inclusion in lettersGuessed
    for i in secretWord:
        #memoization of letters in secretWord and result in boolDict
        if i in boolDict:
            boolList.append(boolDict[i])
        elif i not in boolDict:
            if i in lettersGuessed:
                boolDict[i] = True
                boolList.append(True)
            else:
                boolDict[i] = False
                boolList.append(False)

    return all(boolList)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #init list of correctly guessed letters
    correctLetters = []
    secretWord = list(secretWord)
    ct = 0
    #create list of underscores for each letter in secretWord
    for i in range(len(secretWord)):
        correctLetters.append('_ ')
    #iterate through lettersGuessed and modify correctLetters if guess is correct
    for i in lettersGuessed:
        if i in secretWord:
            #find indices of all occurrences of i in secretWord and append to correctLetters
            for k in secretWord:
                if i == k:
                   correctLetters[ct] = i
                   secretWord[ct] = ''
                   ct += 1
                if i != k:
                    ct += 1
        elif i not in secretWord:
            continue
        ct = 0
    return ''.join(correctLetters)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    import string

    #init variables
    availableLetters = list(string.ascii_lowercase)

    #remove letters of lettersGuessed from availableLetters
    for i in lettersGuessed:
        availableLetters.remove(i)

    return ''.join(availableLetters)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    guessCt = 8
    print('Welcome to the game Hangman!\n' + 'I am thinking of a word that is', len(secretWord), 'letters long')
    while guessCt > 0:
        print('-----------')
        print('You have ' + str(guessCt) + ' guesses left')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available Letters:', availableLetters)
        guess = input('Please guess a letter: ')
        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:', correctLetters)
        elif guess not in lettersGuessed:
            lettersGuessed.append(guess)
            correctLetters = getGuessedWord(secretWord, lettersGuessed)
            if guess in secretWord:
                print('Good guess: ', correctLetters)
            elif guess not in secretWord:
                print('Oops! That letter is not in my word: ', correctLetters)
                guessCt -= 1
            if guessCt > 0 and '_ ' not in correctLetters:
                print('-----------')
                print('Congratulations, you won!')
                break

    if guessCt == 0:
        print('-----------')
        print('Sorry, you ran out of guesses. The word was', secretWord + '.')

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)


