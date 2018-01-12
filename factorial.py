def factorial_rec(n):
    if n == 0:
        return 1
    else:
        result = n * factorial_rec(n - 1)
        return result

fac = raw_input('Enter a number : ')

print factorial_rec(int(fac))
