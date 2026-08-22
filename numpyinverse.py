import numpy as np

# Create a 3x3 matrix
matrix = np.array([[4, 2, 1],
                   [3, 5, 7],
                   [1, 2, 6]])

print("Matrix:")
print(matrix)

# Determinant
det = np.linalg.det(matrix)
print("\nDeterminant:")
print(det)

# Inverse
inv = np.linalg.inv(matrix)
print("\nInverse:")
print(inv)

# Eigenvalues
eigenvalues = np.linalg.eigvals(matrix)
print("\nEigenvalues:")
print(eigenvalues)