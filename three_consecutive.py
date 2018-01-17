# -*- coding: utf-8 -*-

"""
This question is based on a Puzzler that was broadcast on the radio program Car
Talk ( http: // www. cartalk. com/ content/ puzzlers ):

Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-
p-p-i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?

Write a program to find it. Solution: http: // thinkpython. com/ code/ cartalk1. py .
"""


def three_consecutive(word):
    count = 0
    i = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1

        elif count != 3:
            count = 0

        if count != 0:
            i += 2

        else:
            i += 1

    if count >= 3:
        return 1

    else:
        return 0


#word = raw_input('Enter a word : ')
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if three_consecutive(word):
        print word
    #print 'True'

    else:
        pass
        #print 'false'
