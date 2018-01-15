
"""Modify find so that it has a third parameter, the index in word where it should start
looking."""

def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

word = raw_input('Enter the string: ')
letter = raw_input('Enter the letter to be found: ')
start = raw_input('Enter the starting index: ')

ret = find(word, letter, int(start))

if ret != -1:
    print 'Letter found at',ret

else:
    print 'Letter not found'
