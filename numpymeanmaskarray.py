import numpy as np

# Create a (3, 3) array with random integers between 1 and 20
arr = np.random.randint(1, 21, size=(3, 3))

print("Original Array:")
print(arr)

# Create a mask for diagonal elements
mask = np.eye(3, dtype=bool)

# Create masked array
masked_arr = np.ma.array(arr, mask=mask)

print("\nMasked Array (Diagonal Masked):")
print(masked_arr)

# Compute mean of unmasked elements
mean_unmasked = masked_arr.mean()

print("\nMean of Unmasked Elements:")
print(mean_unmasked)

# Replace masked elements with the mean
filled_arr = masked_arr.filled(mean_unmasked)

print("\nArray After Replacing Masked Elements with Mean:")
print(filled_arr)