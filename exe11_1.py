# coding: utf-8


"""
Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator
as a fast way to check whether a string is in the dictionary.
If you did Exercise 10.11, you can compare the speed of this implementation with the list in operator
and the bisection search.
"""
import time
ss
def find_word(word, word_list):
    if word in word_list:
        return 1
    else:
        return 0

word_list = dict()

fin = open('words.txt')
for line in fin:
    word = line.strip()
    word_list[word] = ''

word = raw_input('Enter the word : ')
start_time = time.time()
if find_word(word, word_list):
    print 'Present'

else:
    print 'Absent'

elapsed_time = time.time() - start_time

print elapsed_time, 'seconds'
