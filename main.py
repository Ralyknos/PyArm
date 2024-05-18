# Date edited: November 20th, 2022
# Editor: Kylar Johnson

# First phase: one segment no obstacles no rotation
# Second phase: one segment no obstacles w/ rotation
# Third phase: one segment w/ obstacles w/rotation
# Fourth phase: two segment no obstacles w/ rotation
# Fifth phase: two segment w/ obstacles w/ rotation
# Sixth phase: three segment no obstacles w/ rotation
# Seventh phase: Three segment w/ obstacles w/ rotation

import numpy as np


arm  = np.array([0, 0, 0])  

# Creating arrays
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

print("Array a:", a)
print("Array b:\n", b)

# Array operations
c = a + 10
print("Array c (a + 10):", c)

d = b * 2
print("Array d (b * 2):\n", d)

# Element-wise operations
e = np.sin(a)
print("Array e (sin(a)):", e)

# Matrix operations
f = np.dot(b, a)
print("Array f (dot product of b and a):", f)

# Statistical operations
mean_b = np.mean(b)
print("Mean of b:", mean_b)

# Reshaping arrays
reshaped_b = b.reshape((3, 2))
print("Reshaped b:\n", reshaped_b)
