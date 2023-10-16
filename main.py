import sympy 
import numpy as np


N = 1000000

a = np.zeros( N, dtype=int )
max_ratio = 0.0
n_max = 1
for i in range(1, N+1 ):
    a[i-1] = sympy.totient(i)

    ra = float(i) / float(a[i-1])
    if ra>max_ratio: 
        max_ratio = ra
        n_max = i

    if i%1000 == 0 : 
        print( ".", i )
print( max_ratio, n_max )



