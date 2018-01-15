"""The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r is the remainder when
a is divided by b, then gcd ( a, b ) = gcd ( b, r ) . As a base case, we can use gcd ( a, 0 ) = a."""

def gcd(a, b):
    if b == 0:
        return a

    if a > b:
        r = a%b
        return gcd(b, r)

    else:
        r = b%a
        return gcd(a, r)

a = raw_input('Enter the value of a: ')
b = raw_input('Enter the value of b: ')

print gcd(int(a), int(b))
