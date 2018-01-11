def is_triangle(a, b, c):
    if a <= b + c and b <= a + c and c <= a + b:
        print 'Yes'
    else:
        print 'No'


a = raw_input('\n enter the value of a: ')
b = raw_input('\n enter the value of b: ')
c = raw_input('\n enter the value of c: ')



is_triangle(int(a), int(b), int(c))
#check_fermat(1, 2, 3, 4)
