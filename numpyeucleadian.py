import numpy as np

# Define structured array data type
dtype = [('x', 'i4'), ('y', 'i4')]

# Create structured array with sample points
points = np.array([
    (1, 2),
    (4, 6),
    (7, 3),
    (2, 8)
], dtype=dtype)

print("Points:")
print(points)

# Compute Euclidean distance between each pair of points
n = len(points)

print("\nPairwise Euclidean Distances:")
for i in range(n):
    for j in range(i + 1, n):
        dx = points[i]['x'] - points[j]['x']
        dy = points[i]['y'] - points[j]['y']
        distance = np.sqrt(dx**2 + dy**2)

        print(f"Distance between Point {i+1} and Point {j+1}: {distance:.2f}")