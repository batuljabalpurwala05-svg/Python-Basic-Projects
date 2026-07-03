import numpy as np

try:
    arr = np.arange(1, 25)

    print("Original 1D Array:",arr)
    print("Shape:", arr.shape)

    arr2 = arr.reshape(4,6)
    print("Reshaped array 4X6 :\n",arr2)
    print("Shape :",arr2.shape)

    arr3 = arr.reshape(3,8)
    print("Reshaped array 3X8 :\n",arr3)
    print("Shape :",arr3.shape)

    array3D = arr.reshape(2,3,4)
    print("3D Array :\n",array3D)
    print("Shape :",array3D.shape)
except Exception as e:
    print("Error:",e)

