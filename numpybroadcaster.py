import numpy as np

# Create a (4, 4) array with random integers between 1 and 20
arr = np.random.randint(1, 21, size=(4, 4))

# Create a 1D array of shape (4,)
col_subtract = np.array([1, 2, 3, 4])

# Subtract the 1D array from each column using broadcasting
result = arr - col_subtract.reshape(4, 1)

print("Original Array:")
print(arr)

print("\n1D Array:")
print(col_subtract)

print("\nResult after Broadcasting Subtraction:")
print(result)