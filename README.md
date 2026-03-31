# EIGENVALUES-AND-EIGENVECTORS
## Aim:
To write a python program to find the Eigenvalues and Eigen Vectors
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
Step 1: Import NumPy and define the matrix 
𝐴
A.

Step 2: Use np.linalg.eig(A) to compute eigenvalues and eigenvectors.

Step 3: Store the results in variables (eigenvalues and eigenvectors).

Step 4: Print the eigenvalues and eigenvectors.

## Program:
```
#Program to find the eigen values and eigen vectors.
#Developed by: Ezhilan H
#RegisterNumber: 212225240040

import numpy as np

A = np.array([[4, 2],[2, 4]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigen values are", eigenvalues,"and Eigen Vectors are", eigenvectors)
```

## Output:
<img width="1322" height="548" alt="image" src="https://github.com/user-attachments/assets/f2ba6912-184a-4644-a38a-4fe04e304b86" />

## Result:
Thus the Eigenvalue and Eigenvector is successfully solved using python program
