# File:    proj1.py
# Author:  Bryan Nguyen
# Date:    3/28/19
# Section: 22
# E-mail:  bryann1@umbc.edu
# Description: This program will be able to translate an English phrase
# into how it would be pronounced in Hawaiian English. It'll accomplish
# this task via multiple functions in order to find the consonants, vowels,
# and okina to properly translate the given phrase to Hawaiian pronounciation.

# info for getting choice
ANSWERS  = ["y", "yes", "n", "no"]
CONTINUE = "Do you want to enter another word? (y/yes/n/no): "
# info about characters
OKINA       = "'"
VOWELS      = ["a", "e", "i", "o", "u"]
COMP_VOWELS = ["ai", "ae", "ao", "au", "ei", "eu", "iu", "oi", "ou", "ui"]
CONSONANTS = ["h", "k", "l", "m", "n", "p", "w"]
CHANGE_W = ["a", "e", "i"]
KEEP_W = ["o", "u"]

###################################################
# pronounceW() this will either change the w to a v or leave it as is
#              depending where the w is or whatever follows after it.
#              if the w is at the start of a word or follows an o or u
#              it'll be left as a w but if followed by a, e, i, it'll be a v.
# Parameters:  word; the string that has the letter w in it
#              index; the index where the w is located in the word
# Return:      It'll return a v or w depending on conditions
def pronounceW(word, index):
    # finds where the w is in the word
    wPronounce = word[index]
    # start of word
    startWord = word[0]
    # finds the word that follows the w
    findW = word[index - 1:index]
    # if w follows an a, e, i, it becomes a v
    if findW in CHANGE_W:
        wPronounce = "v"
    # if w is at the start of word or follows a o, or u, it stays as a w
    if findW in KEEP_W or startWord == "w":
        wPronounce = "w"
    # return the pronounciation of the "w"
    return wPronounce

##################################################
# pronounce() will take the entire phrase into account
#             in translating it to Hawaiian pronounciation
# Parameters:  phrase; the whole input that may be single/multiple words
# Return:      It'll return the string translated to Hawaiian pronounciation
def pronounce(phrase):
    # turns the given phrase into a list
    listPhrase = phrase.split()
    index = 0
    newWord = []
    # keeps track of the each words pronounced
    while index < len(listPhrase):
        # the pronounceWord() will run for every word in phrase
        eachWord = listPhrase[index]
        pronouncedWord = pronounceWord(eachWord)
        newWord.append(pronouncedWord)
        index += 1
    # will join the pronounced version of the given word
    hawaiianWord = " ".join(newWord)
    # returns the entire phrase pronounced in Hawaiian
    return hawaiianWord

##################################################
# pronounceWord() takes care of a single word in translating it
# Parameters:     word; a single word
# Return:         It'll return the string with the Hawaiian pronounciation
def pronounceWord(word):
    index = 0
    index2 = 2
    # initialize empty string
    newWord = ""
    while index < len(word):
        compareLetter = word[index].lower()
        compareComplex = word[index2 - 0:index2]
        # checks to see whether the program should translate the selected word
        if compareLetter in VOWELS:
            # calls simpleVowel to translate simple vowels
            compareLetter = simpleVowel(compareLetter)
            newWord = newWord + compareLetter + "-"
        elif CONSONANTS[len(CONSONANTS) - 1] in word:
            compareLetter = pronounceW(word, index)
            newWord = newWord + compareLetter + "-"
        # leaves word alone if it doesn't need translation
        elif compareLetter not in VOWELS:
            newWord = newWord + compareLetter
        index += 1
    # after program is done translating, it takes out the extra dash at end
    newWord = newWord[:len(newWord) - 1]
    # returns the translated word from the phrase
    return newWord

###################################################
# getHawaiianPhrase() asks user to input a Hawaiian phrase
#                     and asks them again if the phrase isn't valid
#                     while also explaining why it's invalid.
# Parameters:         Function takes no input
# Return:             It'll return a string of the user's phrase
def getHawaiianPhrase():
    # the loop will keep going until the phrase given is valid
    wordLoop = True
    while wordLoop:
        # asks user to put in a phrase to pronounce
        inputPhrase = input("Enter a Hawaiian phrase to pronounce: ")
        wordLoop = False
        # turns the phrase into a list of strings
        splitPhrase = inputPhrase.split()
        index = 0
        while index < len(splitPhrase):
            # a way for the program to index through each word in phrase
            eachWord = splitPhrase[index]
            lastLetter = eachWord[len(eachWord) - 1]
            lowLetter = lastLetter.lower()
            # checks to see if the phrase ends in a vowel or not
            if lowLetter not in VOWELS:
                print("The word", eachWord, "doesn't end in a vowel.")
                wordLoop = True
            letterIndex = 0
            while letterIndex < len(eachWord):
                # each letter of each word in the phrase is iterated through
                eachLetter = eachWord[letterIndex]
                lowerEach = eachLetter.lower()
                # checks to see if all the letters are valid/invalid words
                if lowerEach not in VOWELS and lowerEach not in CONSONANTS:
                    print("The letter", eachLetter, "is not valid.")
                letterIndex += 1
            index += 1
    # returns the given phrase to be sorted out for translation
    return inputPhrase

###################################################
# simpleVowel() this will determine how a vowel is pronounced
#               depending on conditions
# Parameters:   letter; a single letter
# Return:       It returns a new version of the letter in
#               Hawaiian pronounciation
def simpleVowel(letter):
    # takes care of capitalization in comparing word to vowels list
    compareLetter = letter.lower()
    if compareLetter == "a":
        compareLetter = "ah"
    elif compareLetter == "e":
        compareLetter = "eh"
    elif compareLetter == "i":
        compareLetter = "ee"
    elif compareLetter == "o":
        compareLetter = "oh"
    elif compareLetter == "u":
        compareLetter = "oo"
    # returns proper pronounciation of each letter
    return compareLetter

###################################################
# complexVowel() this will deal with how a two letter vowel will be pronounced
# Parameters:    vowels; a string that has two vowels together
# Return:        It returns a new version of the vowels in
#                Hawaiian pronounciation
def complexVowel(vowels):
    compareVowel = vowels.lower()
    # does the same thing as simpleVowels() but applies to complex vowels
    if compareVowel == "ai" and compareVowel == "ae":
        compareVowel = "eye"
    elif compareVowel == "ao" and compareVowel == "au":
        compareVowel = "ow"
    elif compareVowel == "ei":
        compareVowel = "ay"
    elif compareVowel == "eu":
        compareVowel = "eh-oo"
    elif compareVowel == "iu":
        compareVowel = "ew"
    elif compareVowel == "oi":
        compareVowel = "oy"
    elif compareVowel == "ou":
        compareVowel = "ow"
    elif compareVowel == "ui":
        compareVowel = "ooey"
    # returns the translated complex vowel
    return compareVowel

###################################################
# getChoice() prompts and reprompts the user until
#             they select a valid choice
# Parameters: question; a string to be asked
#             options; a list of string options
# Return:     choice; a string chosen by the user
def getChoice(question, options):
    compareVal = True
    while compareVal:
        compareVal = False
        # asks the user if they want to keep putting in words
        anotherInput = input(question)
        # takes care of difference in capitalization from the user's response
        compareInput = anotherInput.lower()
        # keeps reprompting the user to put a valid response
        if compareInput not in options:
            print("Enter y/yes/n/no")
            compareVal = True
        if compareInput in options:
            if compareInput == "y" or compareInput == "yes":
                compareVal = False
        # returns whatever valid input the user inputs in
        return compareInput

def main():
    runVal = True
    while runVal:
        runVal = False
        # the first thing the program does is to ask user for a phrase
        userPhrase = getHawaiianPhrase()
        # it gets the returned valid phrase and translates from there
        hawaiianPhrase = pronounce(userPhrase)
        # prints how the given phrase is pronounced in Hawaiian pronounciation
        print("The phrase", userPhrase, "is pronounced: ")
        print("\t", hawaiianPhrase)
        answerInput = getChoice(CONTINUE, ANSWERS)
        # if the user says y or yes, the program keeps translating given phrases
        if answerInput == "y" or answerInput == "yes":
            runVal = True
        else:
            runVal = False

main()
