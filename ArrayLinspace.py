import numpy as np
try:
    arr1 = np.linspace(0,5,10)
    arr2 = np.linspace(-10,10,15)

    print("a) 10 equally spaced numbers between 0 and 5:",arr1)
    print("Length:", len(arr1))
    print("b) 15 equally spaced numbers between -10 and 10:",arr2)
    print("Length:",len(arr2))

except Exception as e:
    print("Error:",e)