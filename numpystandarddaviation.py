import numpy as np

# Create a (3, 3) array with values from 1 to 9
arr = np.arange(1, 10).reshape(3, 3)

print("Original Array:")
print(arr)

# Normalize the array
mean = np.mean(arr)
std = np.std(arr)

normalized_arr = (arr - mean) / std

print("\nMean:", mean)
print("Standard Deviation:", std)

print("\nNormalized Array:")
print(normalized_arr)