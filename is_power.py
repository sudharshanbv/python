"""A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b . Note:
you will have to think about the base case."""

def is_power(a, b):
    if (not a%b):


a = raw_input('Enter the value of a: ')
b = raw_input('Enter the value of b: ')
is_power(int(a), int(b))
