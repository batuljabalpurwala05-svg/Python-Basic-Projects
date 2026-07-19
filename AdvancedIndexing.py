import numpy as np
try:
    arr = np.random.randint(1,101,(5,5))
    print("Original matrix :\n",arr)
    print("Diagonal elements :",np.diag(arr))
    print("Elements greater than 50 :",arr[arr > 50])
    arr[arr<30] = 0
    print("Modified matrix with elements less than 30 replaced by 0 :\n",arr)

except Exception as e:
    print("Error:",e)

