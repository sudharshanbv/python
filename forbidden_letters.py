# -*- coding: utf-8 -*-

"""Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Modify your program to prompt the user to enter a string of forbidden letters and then print the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?"""

def avoids(word, forbidden):
    for i in forbidden:
        if i in word:
            return 0
    return 1
word = raw_input('Enter the word: ')
forbidden = raw_input('Enter a string of forbidden letters: ')

if avoids(word, forbidden):
    print 'True'

else:
    print 'False'
