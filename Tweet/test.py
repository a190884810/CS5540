from numpy import *; from numpy.linalg import * #矩阵计算模块

c = array([(x,y) for x in [0,-1,1] for y in [0,-1,1]])

t = 1./36. * ones(9)

t[asarray([norm(ci)<1.1 for ci in c])] = 1./9.
print (t)
