
def count(word, letter):
    index = 0
    count = 0
    while index < len(word):
        if word[index] == letter:
            count = count + 1
        index = index + 1
    return count

word = raw_input('Enter the string: ')
letter = raw_input('Enter the letter to be found: ')


ret = count(word, letter)

if ret == 0:
    print 'Letter not found in the string'

else:
    print 'Letter found at', ret, 'instances'
