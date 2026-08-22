import numpy as np

# Create a 5x5 array with random integers between 1 and 100
arr = np.random.randint(1, 101, size=(5, 5))

print("Original Array:")
print(arr)

# Extract border elements
top_row = arr[0, :]
bottom_row = arr[-1, :]
left_col = arr[1:-1, 0]
right_col = arr[1:-1, -1]

border_elements = np.concatenate(
    [top_row, right_col, bottom_row[::-1], left_col[::-1]]
)

print("\nBorder Elements:")
print(border_elements)