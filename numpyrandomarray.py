import numpy as np

# Create two (3, 4) arrays with random integers between 1 and 10
arr1 = np.random.randint(1, 11, size=(3, 4))
arr2 = np.random.randint(1, 11, size=(3, 4))

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

# Element-wise operations
addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2  # arr2 values are non-zero (1-10)

print("\nElement-wise Addition:")
print(addition)

print("\nElement-wise Subtraction:")
print(subtraction)

print("\nElement-wise Multiplication:")
print(multiplication)

print("\nElement-wise Division:")
print(division)