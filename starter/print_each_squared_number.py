import sys


def square(x):
    '''Return the square of x.'''
    return x ** 2


args = sys.argv[1:]
ints = [int(i) for i in args]

for number in ints:
    print(square(number))
