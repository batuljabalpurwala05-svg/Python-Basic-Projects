import numpy as np
try:
    arr1 = np.random.randint(10,101,(5,6))
    print("5x6 array :",arr1)
    print("Shape :",arr1.shape)
    print("Total number of elements (size):",arr1.size)
    print("Data Type:",arr1.dtype)
except Exception as e:
    print("Error:",e)