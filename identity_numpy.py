import numpy
numpy.set_printoptions(legacy = '1.13')

dim = input().strip().split()
print (numpy.eye(int(dim[0]), int(dim[1])))