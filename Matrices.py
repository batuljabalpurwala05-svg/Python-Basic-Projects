import numpy as np
try:
    matrix = np.random.randint(1,101,(4,4))

    print("4X4 Matrix is :\n",matrix)
    print("matrix shape :",matrix.shape)
    print("Dimensions:",matrix.ndim)
    print("Total number of elements :",matrix.size)
    print("matrix datatype :",matrix.dtype)
    print("minimum value :",np.min(matrix))
    print("maximum value :",np.max(matrix))
except Exception as e:
    print("Error:",e)