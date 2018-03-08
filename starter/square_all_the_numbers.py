import sys


def square(x):
    '''Return the square of x.'''
    return x ** 2


args = sys.argv[1:]
ints = [int(i) for i in args]

print([square(i) for i in ints])
