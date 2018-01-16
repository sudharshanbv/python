# -*- coding: utf-8 -*-

"""Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou ? How about aeiouy ?"""


def uses_all(word, required):
    for i in required:
        if not i in word:
            return 0
    return 1

word = raw_input('Enter the word: ')
required = raw_input('Enter a string of required letters: ')

if use_all(word, required):
    print 'True'

else:
    print 'False'
