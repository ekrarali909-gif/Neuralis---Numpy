import numpy as np

# Create a (5, 5) array with random integers between 1 and 100
arr = np.random.randint(1, 101, size=(5, 5))

print("Original Array:")
print(arr)

# Compute statistics
mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)
variance = np.var(arr)

print("\nMean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)
print("Variance:", variance)