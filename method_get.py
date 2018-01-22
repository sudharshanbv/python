

"""
Dictionaries have a method called get that takes a key and a default value. If the
key appears in the dictionary, get returns the corresponding value; otherwise it returns the default
value. For example:
"""

def histogram(s):
    d = dict()
    #traverse through each character
    for c in s:
        d[c] = d.get(c, 0)
        d[c] += 1
    #return the dictionary
    return d


d = histogram('a')
print d

print d.get('a', 0)
print d.get('b', 0)
