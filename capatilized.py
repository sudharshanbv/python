"""
capitalize() is a method in list

RETURN:
Return a copy of the string with its first character capitalized and the rest lowercased.
"""

"""capitalize_all() is a function to change the all first letters of each element
in a list to a capital letter"""

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

t = ['hai', 'hello', 'world']

print capitalize_all(t)
