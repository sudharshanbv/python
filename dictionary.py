
"""
In this script, histogram function takes a string as an argument and creates a dictionary
with characters as 'keys' and the frequency of each character as 'value' and returns the
dictionary
"""

def histogram(s):
    d = dict()
    #traverse through each character
    for c in s:
        # if the character is not present in the dictionary as key, initialize it with count 1
        if c not in d:
            d[c] = 1
        # if the character is already present as key, increment the count
        else:
            d[c] += 1
    # return the dictionary
    return d

d = histogram('brontosaurus')

print d
