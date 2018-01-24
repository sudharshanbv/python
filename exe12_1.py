"""
Write a function called sumall that takes any number of arguments and returns their sum.
"""
def sumall(t):
    sum = 0
    for i in t:
        sum += i

    return sum



limit = raw_input('Enter the number of elements : ')
t = tuple()
print 'Enter the elements\n'
for i in range(int(limit)):
    t = t[0:] + (int(raw_input()),)

print sumall(t)
