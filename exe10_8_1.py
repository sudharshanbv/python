
# coding: utf-8
"""
Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.
"""

def has_duplicates(t):
    idx = 0
    for i in t[:-1]:
        for j in range (idx + 1, len(t[:])):
            if i == t[j]:
                return 1
        idx += 1

    return 0


limit = raw_input('Enter the number of elements : ')
t = []
print 'Enter the elements\n'
for i in range(int(limit)):
    t.append(int(raw_input()))

print ''
if has_duplicates(t):
    print 'Has Duplicates'

else:
    print 'No Duplicates'
