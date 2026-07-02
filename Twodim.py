import numpy as np
try:
    matrix = np.random.randint(20,81,(4,5))
    print("Matrix :\n",matrix)
    print("Minimum value :",np.min(matrix))
    print("maximum value :",np.max(matrix))
    print("Sum of all elements :",np.sum(matrix))
    print("Mean :",np.mean(matrix))
    print("Standard deviation :",np.std(matrix))
    # Row wise sum
    print("Sum of each row :",np.sum(matrix,axis=1))
    # Column wise sum
    print("Sum of each column :",np.sum(matrix,axis=0))
except Exception as e:
    print("Error:",e)