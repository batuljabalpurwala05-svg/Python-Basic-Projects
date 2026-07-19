import numpy as np
try:
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    b = np.array([[9,8,7],[6,5,4],[3,2,1]])
    
    add = a + b
    matrix_multi = a@b
    element_multi = a * b

    print("Addition :",add)
    print("Multiplication :",matrix_multi)
    print("Element wise multiplication :",element_multi)
except Exception as e:
    print("Error:",e)