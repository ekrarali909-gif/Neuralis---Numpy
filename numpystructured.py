import numpy as np

# Define the structured data type
dtype = [('name', 'U20'), ('age', 'i4'), ('weight', 'f4')]

# Create a structured array with sample data
people = np.array([
    ('Alice', 25, 55.5),
    ('Bob', 30, 72.3),
    ('Charlie', 22, 68.1),
    ('David', 28, 80.0)
], dtype=dtype)

print("Original Structured Array:")
print(people)

# Sort by age
sorted_people = np.sort(people, order='age')

print("\nSorted by Age:")
print(sorted_people)