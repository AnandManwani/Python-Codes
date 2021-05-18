import numpy

n, m = [int(x) for x in input().strip().split()]

arr = numpy.array([[int(x) for x in input().strip().split()] for _ in range(n)])

a = numpy.sum(arr, axis = 0)

print (numpy.prod(a))
