#!/usr/bin/env python
import random
import fileinput

"""
The pictures for hangman to be printed after each unsuccesful guess.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

HANGMAN= [
        # Noose only
        '''

            +-----------+
            |   |
            |   
            |
            |
            |
            +==========+
            ''',
            # Head
            '''

            +-----------+
            |   |
            |   O
            |
            |
            |
            +==========+
            ''',

            # Head and torso
            '''

            +-----------+
            |   |
            |   O
            |   |
            |
            |
            +==========+
            ''',

            # Head, torso, left arm
            '''

            +-----------+
            |   |
            |   O
            |  /|
            |
            |
            +==========+           
            ''',

            # Head, torso, left arm, right arm
            ''' 

            +-----------+
            |   |
            |   O
            |  /|\\
            |
            |
            +==========+ 
            ''',

            # Head, torso, left arm, right arm, left leg
            '''

            +-----------+
            |   |
            |   O
            |  /|\\
            |  /
            |
            +==========+ 
            ''',

            # Head, torso, left arm, right arm, left leg, right leg
            '''

            +-----------+
            |   |
            |   O
            |  /|\\
            |  / \\
            |
            +==========+ 
            '''
        ]

# A dictionary of categories and their respective words to guess. Please feel free to add
# to this dictionary.

CATEGORIES = {
        'animals': ['Alligator', 'Armadillo', 'Arctic Fox',
            'Arctic Wolf', 'Black Bear', 'Bongo', 
            'Bearded Collie','Bobcat', 'Cross River Gorilla', 
            'Cuttlefish', 'Dragonfly', 'Dward Crocodile', 'Dhole',
            'Eagle', 'English Cocker Spaniel', 'Elephant Seal', 
            'Falcon', 'Fin Whale', 'Gecko', 'Glow Worm', 'Hammerhead Shark',
            'Harambe', 'Heron', 'Horse', 'Human', 'Indian Elephant', 'Ibis',
            'Jackal', 'Jellyfish', 'Kangaroo', 'Koala', 'Komodo Dragon', 'Keel Billed Toucan',
            'Labradoodle', 'Ladybird', 'Leopard Tortoise', 'Lionfish', 'Liger', 
            'Lizard', 'Lemur', 'Lemming', 'Moose', 'Marsh Frog', 'Maltese',
            'Marine Toad', 'Mole', 'Mountain Gorilla', 'Numbat', 'Newt',
            'Nightingale', 'Okapi', 'Ostrich', 'Parrot', 'Penguin',
            'Peacock', 'Pool Frog', 'Porcupine', 'Possum', 'Quail', 'Rabbit',
            'Raccoon', 'Red Panda', 'River Turtle', 'Robin', 'Salamander', 'Sand Lizard',
            'Sand Lizard', 'Scorpion', 'Sea Dragon', 'Sea Otter', 'Seal', 
            'Sheep', 'Siamese', 'Sloth', 'Snapping Turtle', 'Sperm Whale',
            'Spider Monkey', 'Squid', 'Sumatran Tiger', 'Tree Frog', 'Tawny Owl', 
            'Tasmanian Devil', 'Termite', 'Turkey', 'Turkish Angora', 'Vampire Bat',
            'Wallaby', 'Walrus', 'Whale Shark', 'Woolly Mammoth', 'White Tiger', 
            'Yak', 'Zebra', 'Zebra Shark'],

        'colours': ['Orange', 'Red', 'Blue', 'Green', 'Yellow', 'Azure', 'Brown', 'Teal', 'Grass', 
            'sky blue', 'pink', 'purple', 'lime green', 'Amber'],

        'sports': ['Soccer', 'Baseball', 'Basketball', 'Squash', 'Hockey', 'Lacrosse',
            'Golf', 'cricket', 'skiing', 'boxing', 'polo', 'badminton',
            'surfing', 'track and field', 'equestrianism', 'rugby', 'football', 'judo'],

        'tv shows': ['Supernatural', 'Pretty Little Liars', 'Fresh Prince of Bel-Air',
            'The OA', 'Gossip Girl', 'Friends', 'Game of Thrones', 'westworld', 'caillou', 
            'arthur', 'magic school bus', 'dragon ball z', 'Family Guy', 'Master of None',
            'Luke Cage', 'Daredevil', 'Archer', 'Inception', 'Interstellar', 'American Dad',
            "grey's anatomy"]
        }

"""
Helper functions for the game Hangman.
"""

def getRandomWord(wordList):
    """ Return a random word from a given list of words
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def getHiddenWord(actualWord):
    """ Return a hidden string representation of actualWord.
    Each letter in actualWord is represented by an underscore followed 
    by exactly one space. Only alphanumerical characters are treated
    """
    hiddenWord = ''

    for index in range(len(actualWord)):
        if actualWord[index].isalpha():
            hiddenWord = hiddenWord + ' _'
        else:
            hiddenWord = hiddenWord + ' ' +  actualWord[index]

    # Check if we did this correctly
    if len(hiddenWord) == 2 * len(actualWord):
        return hiddenWord
    else:
        print("Something went wrong after selecting your word!\n")
        return None


def letterInWord(letter, actualWord, hiddenWord):
    """ Return an updated hiddenWord if letter is in actualWord.
    If letter is not in actualWord, then increment the global var count

    @param str letter: a single char letter
    @param str actualWord: a string
    @param str hiddenWord: a string of hidden letters
    """
    hiddenWordList = list(hiddenWord)

    matchFound = False

    for index in range(len(actualWord)):
       if letter.lower() == actualWord[index].lower():
           # Found a match! Print the statements accordingly
            matchFound = True
            print("You guessed correctly!\n")
            hiddenWordList[index * 2 + 1] = actualWord[index]

    if not matchFound:
        print(letter, " is not in the word, try again!\n");
        global guessedLetters
        guessedLetters.append(letter)
        global count
        count = count + 1

    return ''.join(hiddenWordList)

def displayGameBoard(count, hiddenWord, guessedLetters):
    """ Print a hangman game board with the current guesses, correct picture,
    and the secret word

    @param list HANGMAN: The pictures of hangman
    @param int count: The number of incorrect guesses so far
    @param guessedWord: String representation of current hidden word
    @param listi guessedLetters: A list of incorrect letters guessed
    """
    print(HANGMAN[count],"\n")

    print(hiddenWord)
    
    print("Letters you've guessed already: ")
    for letter in guessedLetters:
        print("[", letter, "]", end='')
    

def gameInProgress():
    """ Return True if the game is still in progress
    """
    global count
    global hiddenWord
    global actualWord

    wordMatches = True

    for index in range(len(actualWord)):
        if actualWord[index] != hiddenWord[index * 2 + 1]:
            wordMatches = False

    if wordMatches:
        print(hiddenWord)
        print("\nCongratulations! You guessed the correct word!")

    return not((count >= 7) or wordMatches)

if __name__ == "__main__":
    # Main program runs until the user prompts 'y' to restart the game or
    # 'n' to terminate the game. 
    while True:
        count = 0

        guessedLetters = []

        print("\n\n+++++++++ Welcome to Hangman! +++++++++\n")
        print("Begin by choosing a category. The objective of the game is to correctly guess a word from your category one letter at a time. Every incorrect guess leads to our man closer to his death!\n")

        print("Choose a category: animals, colours, sports, or tv shows")

        category = input("Please type your selected category: ")

        while not CATEGORIES.__contains__(category):
            category = input("Please type your select category again (case sensitive): ")

        wordList = CATEGORIES.__getitem__(category)

        actualWord = getRandomWord(wordList)
      #  print(actualWord)

        hiddenWord = getHiddenWord(actualWord)
        
        # This is the game in progress. Loops until the count hits 7 (i.e, 
        # the hangman has been drawn completely, or, until the word has been
        # correctly guessed. 
        while gameInProgress():
            displayGameBoard(count, hiddenWord, guessedLetters)

            letter = input("\nGuess a letter: ")

            hiddenWord = letterInWord(letter, actualWord, hiddenWord)
        
        if count == 7:
            print("\nOh no, the man has died! The word was ", actualWord)

        continue_game = input("\nDo you want to restart the game? (y/n): ")

        if continue_game == 'y':
            continue
        elif continue_game == 'n':
            print("\nSee ya later!")
            break
        else:
            print("Invalid input. Exiting game")
            break
