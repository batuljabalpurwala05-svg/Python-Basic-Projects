import numpy as np
try:
    A = np.array([[1,2,3],[4,5,6],[7,8,9]])
    B = np.array([[9,8,7],[6,5,4],[3,2,1]])
    print("Matrix A:\n",A)
    print("Matrix B:\n",B)
    print("Element wise multiplication :\n",A*B)
    print("Matrix Multiplication:\n",A@B)
except Exception as e:
    print("Error:",e)
# In element-wise multiplication, corresponding elements are multiplied
# In matrix multiplication, rows of A are multiplied with columns of B.