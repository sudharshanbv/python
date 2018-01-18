# coding: utf-8

"""
Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. So middle([1,2,3,4]) should return [2,3] .
"""
def middle(t):
    del t[0]
    del t[-1]
    return t

t =[1, 2, 3, 4]

print middle(t)
