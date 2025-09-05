# 1.  Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.
import numpy as np

elem = list(map(int, input("Enter 9 numbers separated by space: ").split()))
arr = np.array(elem).reshape(3, 3)

print("ndim:",arr.ndim)
print("shape:",arr.shape)

print("First row:",arr[0])
print("First column:",arr[:,0])
print("2x2",arr[0:2,0:2])

# 2. Create one dimensional 3*3 array and perform ndim, shape, reshape operation on it.

import numpy as np
elem=list(map(int, input("Enter even number of elements:").split()))
arr=np.array(elem)

print("ndim:",arr.ndim)
print("shape:",arr.shape)

print("reshape:", arr.reshape(2,2))
