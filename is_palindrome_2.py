def palindrome(word):
    if word[0:len(word) / 2:1] != word[len(word) - 1:len(word) / 2:-1]:
        return 0

    return 1

str = raw_input('Enter the string : ')
if palindrome(str):
    print 'palindrome'

else :
    print 'Not Palindrome'    
