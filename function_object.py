def do_twice(fun):
    fun()
    fun()

def fun():
    print 'hello, i am sudharshan'

do_twice(fun)
