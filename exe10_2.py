# coding: utf-8

"""
Write a function named capitalize_nested that takes a nested list of strings
and returns a new nested list with all strings capitalized.
"""
def capitalize_all(t):
    res = []
    for s in t:
        for i in s:
            res.append(i.capitalize())
    return res

t = [['hai', 'hello', 'world'], ['wow', 'wonder', 'amazing']]
print t
print capitalize_all(t)
