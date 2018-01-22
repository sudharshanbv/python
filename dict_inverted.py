# coding: utf-8

"""
Lists can appear as values in a dictionary. For example, if you were given a dictionary that
maps from letters to frequencies, you might want to invert it; that is, create a dictionary
that maps from frequencies to letters. Since there might be several letters with the same
frequency, each value in the inverted dictionary should be a list of letters.
"""

"""

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

"""
def invert_dict(d):
     inverse = {}
     for key, val in d.iteritems():
         inverse.setdefault(val, []).append(key)
     return inverse

def histogram(s):
    d = dict()
    #traverse through each character
    for c in s:
        d[c] = d.get(c, 0)
        d[c] += 1
    #return the dictionary
    return d


d = histogram('parrot')

print d

print invert_dict(d)
