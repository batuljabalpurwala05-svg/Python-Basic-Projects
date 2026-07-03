import numpy as np
try:
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])

    print("Array a :",a)
    print("Array b :",b)
    print("Addition :",a+b)
    print("Subtraction :",a-b)
    print("Multiplication :",a * b)
    print("Element wise power :",a ** b)
    print("Modulo operation :",a % b)
except Exception as e:
    print("Error:",e)