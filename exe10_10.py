
"""
Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and
the other using the idiom t = t + [x] . Which one takes longer to run? Why?
Hint: use the time module to measure elapsed time. Solution: http: // thinkpython. com/
code/ wordlist. py .
"""
import time


def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2():
    """Reads lines from a file and builds a list using list +."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'

start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'
