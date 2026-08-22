import numpy as np

# Create a (4, 4) array with random integers between 1 and 20
arr = np.random.randint(1, 21, size=(4, 4))

print("Original Array:")
print(arr)

# Create a masked array where elements > 10 are masked
masked_arr = np.ma.masked_greater(arr, 10)

print("\nMasked Array (elements > 10 are masked):")
print(masked_arr)

# Compute the sum of unmasked elements
unmasked_sum = masked_arr.sum()

print("\nSum of Unmasked Elements:")
print(unmasked_sum)