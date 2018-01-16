
# -*- coding: utf-8 -*-

"""Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo ? Other than “Hoe alfalfa?”"""

def uses_only(word, allowed):
    for i in word:
        if not i in allowed:
            return 0
    return 1

word = raw_input('Enter the word: ')
allowed = raw_input('Enter a string of allowed letters: ')

if uses_only(word, allowed):
    print 'True'

else:
    print 'False'
