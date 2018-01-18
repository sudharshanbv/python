# coding: utf-8

"""
Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For
example, the cumulative sum of [1, 2, 3] is [1, 3, 6] .
"""


def cum_sum(t):
    new = []
    j = 0
    for i in t:
        j += i
        new.append(j)

    return new


t = [1, 2, 3, 4, 5, 6]
print cum_sum(t)
