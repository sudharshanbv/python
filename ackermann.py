
def ackermann_fun(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_fun(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann_fun(m - 1, ackermann_fun(m, n - 1))


m = raw_input('Enter the value for m: ')
n = raw_input('Enter the value for n: ')

print ackermann_fun(int(m),int(n))
