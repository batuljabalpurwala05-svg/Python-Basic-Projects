import numpy as np
try:
    arr1 = np.arange(0,21,1)
    arr2 = np.arange(10,51,2)
    arr3 = np.arange(5,101,5)

    print("Array from 0 to 20 with step of 1 :",arr1)
    print("Even numbers from 10 to 50 :",arr2)
    print("Array from 5 to 100 with step of 5 :",arr3)
except  Exception as e:
    print("Error:",e) 