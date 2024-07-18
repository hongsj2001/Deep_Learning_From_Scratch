#1.5.6 원소 접근
import numpy as np
X = np.array([[51,55],[14,19],[0,4]])
print(X) #배열 X 출력 
print(X[0]) #배열 X의 0번째 행 출력
print(X[0][1]) #배열 X의 0번째 행 1번째 열의 원소 출력

for row in X: #for문을 이용하여 각 열 출력
    print(row)

X = X.flatten() #X를 1차원 배열로 변환
print(X) #1차원 배열 형태로 출력됨
print(X[np.array([0,2,4])]) #0,2,4번째 인덱스의 원소 출력

print(X>15) #조건을 붙여 Bool배열로 출력 -> 원소가 15보다 크면 True, 작으면 False로 
print(X[X>15]) #조건을 붙여 조건에 맞는 원소들만 출력