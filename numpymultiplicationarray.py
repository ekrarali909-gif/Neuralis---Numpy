import numpy as np

# Create two arrays
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])   # Shape (2, 3)

arr2 = np.array([[7, 8],
                 [9, 10],
                 [11, 12]])    # Shape (3, 2)

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

# Matrix multiplication
result = np.matmul(arr1, arr2)  # or arr1 @ arr2

print("\nMatrix Multiplication Result:")
print(result)