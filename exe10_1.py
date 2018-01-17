# coding: utf-8

"""Write a function called nested_sum that takes a nested list of integers and add up
the elements from all of the nested lists."""

#i = 0

def nested_sum(t):
    sum = 0
    for x in t:
        for i in x:
            sum += i

    return sum


t = [10, [1, 2, 3], [4, 5, 6]]

print nested_sum(t)
