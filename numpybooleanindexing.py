import numpy as np

# Create a (5, 5) array with random integers between 1 and 100
arr = np.random.randint(1, 101, size=(5, 5))

print("Original Array:")
print(arr)

# Extract corner elements using fancy indexing
corners = arr[[0, 0, 4, 4], [0, 4, 0, 4]]

print("\nCorner Elements:")
print(corners)