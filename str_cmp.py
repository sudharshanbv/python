"""the following function prints all the letters from word1 that also appear in
word2 """

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print letter


word1 = raw_input('Enter the first word: ')
word2 = raw_input('Enter the second word: ')

in_both(word1, word2)
