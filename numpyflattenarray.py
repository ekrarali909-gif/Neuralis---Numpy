import numpy as np

# Create a (5, 5) array with random integers between 1 and 100
arr = np.random.randint(1, 101, size=(5, 5))

print("Original Array:")
print(arr)

# Flatten the array
flat_arr = arr.flatten()

print("\nFlattened Array:")
print(flat_arr)

# Reshape back to (5, 5)
reshaped_arr = flat_arr.reshape(5, 5)

print("\nReshaped Array (5, 5):")
print(reshaped_arr)