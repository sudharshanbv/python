

def palindrome(word):
    for i in range(len(word) / 2):
        if word[i] != word[-1 - i]:
            return 0

    return 1

str = raw_input('Enter the string : ')
if palindrome(str):
    print 'True'

else:
    print 'False'
