import numpy as np

# Create a (3, 3) array with random integers between 1 and 10
arr = np.random.randint(1, 11, size=(3, 3))

# Create a 1D array of shape (3,)
row_add = np.array([10, 20, 30])

# Add the 1D array to each row using broadcasting
result = arr + row_add

print("Original Array:")
print(arr)

print("\n1D Array:")
print(row_add)

print("\nResult after Broadcasting Addition:")
print(result)