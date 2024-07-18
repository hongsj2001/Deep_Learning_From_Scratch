#3.3.1 다차원 배열
import numpy as np

A = np.array([1,2,3,4]) 
print(A) #[1,2,3,4]
print(np.ndim(A)) #1
print(A.shape) #1X4
print(A.shape[0]) #4

B = np.array([[1,2],[3,4],[5,6]])
print(B)

print(np.ndim(B)) #2
print(B.shape) #3X2