#1.5.4 넘파이의 N차원 배열
import numpy as np
A = np.array([[1,2],[3,4]]) #2차원 배열 생성

print(A) #2차원 배열 A 출력
print(A.shape) #A의 모양 출력 (2X2 배열)
print(A.dtype) #A의 원소의 자료형 출력

B = np.array([[3,0],[0,6]])
print(A+B) #같은 모양의 배열이면 원소끼리 연산
print(A*B)
print(A*10) #A의 각 원소에 10을 곱함