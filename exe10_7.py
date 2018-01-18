# coding: utf-8


"""
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they
are anagrams.
"""

def is_anagram(word_1, word_2):
    if len(word_1) != len(word_2):
        return 0

    for i in word_1:
        if not i in word_2:
            return 0

    return 1



word_1 = raw_input('Enter the first word : ')
word_2 = raw_input('Enter the second word : ')

if is_anagram(word_1, word_2):
    print 'True'

else:
    print 'False'    
