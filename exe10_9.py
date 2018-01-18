# coding: utf-8


"""
Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original. Hint: they don’t have
to be in the same order.
"""
def remove_duplicates(t):
    u = []
    flag = 0
    for i in t:
        for j in u:
            if i == j:
                flag = 1
        if flag == 0:
            u.append(i)
        flag = 0

    return u


limit = raw_input('Enter the number of elements : ')
t = []
print 'Enter the elements\n'
for i in range(int(limit)):
    t.append(int(raw_input()))

print ''
print remove_duplicates(t)
