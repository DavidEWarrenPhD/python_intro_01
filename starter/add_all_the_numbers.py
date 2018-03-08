import sys

args = sys.argv[1:]
ints = [int(i) for i in args]

print(sum(ints))
