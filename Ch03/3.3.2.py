#3.3.2 행렬의 곱
import numpy as np

A = np.array([[1,2],[3,4]])
print(A.shape) #2X2

B = np.array([[5,6],[7,8]])
print(B.shape) #2X2

print(np.dot(A,B)) #행렬 곱 수행

A = np.array([[1,2,3],[4,5,6]])
print(A.shape) #2X3

B = np.array([[1,2],[3,4],[5,6]])
print(B.shape) #3X2

print(np.dot(A,B)) #행렬 곱 수행

C = np.array([[1,2],[3,4]])
print(C.shape) #2X2

#print(np.dot(A,C)) #에러 발생 -> A: 2X3 , C: 2X2 행렬로 모양이 맞지 않음

A = np.array([[1,2],[3,4],[5,6]])
print(A.shape)  #3X2

B = np.array([7,8])
print(B.shape) #1차원 배열일 때도 대응하는 원소를 일치 시켜야함

print(np.dot(A,B))