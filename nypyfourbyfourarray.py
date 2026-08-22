import numpy as np

# Create a (4, 4) array with values from 1 to 16
arr = np.arange(1, 17).reshape(4, 4)

print("Original Array:")
print(arr)

# Row-wise sum
row_sum = np.sum(arr, axis=1)

# Column-wise sum
col_sum = np.sum(arr, axis=0)

print("\nRow-wise Sum:")
print(row_sum)

print("\nColumn-wise Sum:")
print(col_sum)