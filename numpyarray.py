import numpy as np

# Create a 5x5 array with random integers between 1 and 20
arr = np.random.randint(1, 21, size=(5, 5))

print("Original Array:")
print(arr)

# Replace all elements in the third column (index 2) with 0
arr[:, 2] = 0

print("\nModified Array:")
print(arr)