
def print_hist(h):
    for c in h:
        print c, h[c]

def histogram(s):
    d = dict()
    #traverse through each character
    for c in s:
        d[c] = d.get(c, 0)
        d[c] += 1
    #return the dictionary
    return d


d = histogram('parrot')

print_hist(d)
