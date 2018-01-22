

# coding: utf-8

"""
If you did Exercise 10.8, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object that appears more than once in the
list.
Use a dictionary to write a faster, simpler version of has_duplicates . Solution: http: //
thinkpython. com/ code/ has_ duplicates. py .

"""

def has_duplicates(t):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.
    set() function takes a list as input and generates a list with no duplicate
    elements.

    t: sequence
    """
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print has_duplicates(t)
    t.append(1)
    print has_duplicates(t)

    t = [1, 2, 3]
    print has_duplicates2(t)
    t.append(1)
    print has_duplicates2(t)
