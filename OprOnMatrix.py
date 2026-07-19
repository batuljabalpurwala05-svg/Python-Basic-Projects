import numpy as np
try:
    matrix = np.random.randn(6,6)
    print("Original Matrix :\n",matrix)
    print("Shape :",matrix.shape)
    print("Size of matrix:",matrix.size)
    print("Data type of matrix :",matrix.dtype)
    max_index = np.where(matrix == np.max(matrix))
    min_index = np.where(matrix == np.min(matrix))

    print("Max index:", max_index)
    print("Min index:", min_index)
    submatrix = matrix[:3,:3]
    print("Top-left 3x3 Submatrix:\n",submatrix)
    
    matrix = np.abs(matrix)
    print("Matrix after replacing negatives with absolute values:\n",matrix)
    print("Mean of modified matrix :",np.mean(matrix))
except Exception as e:
    print("Error:",e)