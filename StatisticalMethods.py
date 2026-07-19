import numpy as np
try:
    arr = np.random.randint(1,51,20)
    print("1D Array :",arr)
    print("Minimum Value :",np.min(arr))
    print("Index of the minimum value :",np.argmin(arr))
    print("Maximum value :",np.max(arr))
    print("Index of maximum value :",np.argmax(arr))
    print("Sum of all elements :",np.sum(arr))
    print("Mean of all elements :",np.mean(arr))
    print("Standard Deviation :",np.std(arr))

except Exception as e:
    print("Error:",e)