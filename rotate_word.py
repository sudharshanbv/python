

def rotate_word(word, num):
    res = ''
    for c in word:
        sum = ord(c) + num

        if sum > 122:
            res += chr(sum - 122)

        else:
            res += chr(sum)

    return res


word = raw_input('Enter the string : ')
num = raw_input('Enter the number : ')

print rotate_word(word, int (num))
