#Program to find the eigen values and eigen vectors.
#Developed by: Ezhilan H
#RegisterNumber: 212225240040

import numpy as np

A = np.array([[4, 2],[2, 4]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigen values are", eigenvalues,"and Eigen Vectors are", eigenvectors)
