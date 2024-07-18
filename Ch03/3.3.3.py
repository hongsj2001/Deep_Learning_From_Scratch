#3.3.3 신경망에서의 행렬 곱

import numpy as np
X = np.array([1,2]) #X를 입력
print(X.shape)

W = np.array([[1,3,5],[2,4,6]]) #W는 가중치 -> 2개의 뉴런에서 3개의 뉴런으로 신호 전달
print(W.shape) 

Y = np.dot(X,W)
print(Y)