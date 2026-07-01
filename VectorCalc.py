import numpy as np
try:
    v1 = np.array([2, 4, 6, 8])
    v2 = np.array([1, 3, 5, 7])

    add = v1 + v1
    sub = v1 - v2
    multi = v1 * v2
    dotmultiply = np.dot(v1,v2)

    print("Addition:",add)
    print("Subtraction:",sub)
    print("Multiplication :",multi)
    print("Dot product :",dotmultiply)

except Exception as e:
    print("Error:",e)
