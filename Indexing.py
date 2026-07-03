import numpy as np
try:

    arr = np.array([
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120]])
    print("Original array :",arr)
    print("First row :",arr[0])
    print("Last column :",arr[:,-1])
    print("Center 2x2 Submatrix:",arr[1:3,1:3])
    print("Even Numbers:")
    even_nums = arr[arr % 2 == 0]
    print(even_nums)
except Exception as e:
    print("Error :",e)