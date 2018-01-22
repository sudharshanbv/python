



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

print d.keys()
