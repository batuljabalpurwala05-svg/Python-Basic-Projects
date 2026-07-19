import numpy as np
try:
    arr = np.random.randint(1,51,20)
    matrix = arr.reshape(4,5)
    print("Matrix :\n",matrix)
    print("Sum :",np.sum(matrix))
    print("Mean :",np.mean(matrix))
    print("Standard deviation :",np.std(matrix))

    print("Maximum value in each row :",np.max(matrix,axis=1))

except Exception as e:
    print("Error:",e)