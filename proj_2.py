# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 17:28:23 2018

@author: Wei Hong
Spyder (Python 3.6)
"""

WORDLIST_FILENAME = "word_list.txt"

#open text file and obtain the list of words
def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

wordList = loadWords()


used_words = []
starting_letter = ''

#start game
while True:
    input_word = input('Please type a word: ') 
    if input_word in used_words: #check if words are used
        print('You typed a word that has been typed before.')
        break
    elif input_word not in wordList: #check if word is in list
        print('you didn\'t type a word found in word_list.txt.')
        break
    elif input_word[0] == starting_letter or starting_letter == '': #check if next word is valid
        starting_letter = input_word[-1]
        used_words.append(input_word)
    else:
        print('you didn\'t type a word that starts with \'' + starting_letter + '\'.')
        break
    