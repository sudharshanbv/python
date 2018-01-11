def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'No, that doesnt work'


a = raw_input('\n enter the value of a: ')
b = raw_input('\n enter the value of b: ')
c = raw_input('\n enter the value of c: ')
n = raw_input('\n enter the value of n: ')


check_fermat(int(a), int(b), int(c), int(n))
#check_fermat(1, 2, 3, 4)
