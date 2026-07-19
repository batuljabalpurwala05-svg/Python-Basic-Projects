import numpy as np
try:
    n = int(input("How many numbers do you want to generate? "))
    # Generate random numbers between 10 and 100
    arr = np.random.randint(10, 101, n)
    print("Generated Array:",arr)
   
    # Basic statistics
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard Deviation:", np.std(arr))

    # Min and Max
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))

    # Try reshaping into 2D 
    root = int(np.sqrt(n))

    if root * root == n:
        matrix = arr.reshape(root, root)
        print("Reshaped Matrix:")
        print(matrix)

        print("Row-wise Sum:")
        print(np.sum(matrix, axis=1))
    else:
        print("Cannot reshape into a perfect 2D square matrix.")

except ValueError:
    print("Invalid input! Please enter an integer.")
except Exception as e:
    print("Error:", e)
