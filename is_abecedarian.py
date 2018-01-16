
# -*- coding: utf-8 -*-

"""Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?"""


def is_abecedarian(word):
    previous = word[0]
    for i in (word[1:]):
        if ord(i) < ord(previous):
            return 0
        previous = i
    return 1


word = raw_input('Enter the word: ')

if is_abecedarian(word):
    print 'True'

else:
    print 'False'



"""
An alternative is to use recursion:
-----------------------------------------
def is_abecedarian(word):
if len(word) <= 1:
return True
if word[0] > word[1]:
return False
return is_abecedarian(word[1:])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
++++++++++++++++++++++++++++++++++++++++++
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another option is to use a while loop:
-----------------------------------------------
def is_abecedarian(word):
i = 0
while i < len(word)-1:
if word[i+1] < word[i]:
return False
i = i+1
return True
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
++++++++++++++++++++++++++++++++++++++++++++
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




"""
