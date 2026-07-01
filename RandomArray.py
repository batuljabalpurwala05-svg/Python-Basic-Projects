import numpy as np
try:
    # a) 1D array of 10 random numbers between 0 and 1
    arr1 = np.random.rand(10)
    # b) 3x3 matrix from standard normal distribution
    arr2 = np.random.randn(3,3)
     # c) 2D array (4x5) of random integers between 10 and 50
    arr3 = np.random.randint(10,51,(4,5))
    # Printing results
    print("a) A 1D array of 10 random numbers between 0 and 1 :",arr1)
    print("b) A 3x3 matrix of random numbers from standard normal distribution :",arr2)
    print("c) A 2D array (4x5) of random integers between 10 and 50 :",arr3)
except Exception as e:
    print("Error :",e)