# coding: utf-8


"""
Exercise 10.6. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators < , > , etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should re-
turn False .e
"""


def is_sorted(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return 0

    return 1


limit = raw_input('Enter the number of elements : ')
t = []
print 'Enter the elements\n'
for i in range(int(limit)):
    t.append(int(raw_input()))

if is_sorted(t):
    print 'True'

else:
    print 'False'
