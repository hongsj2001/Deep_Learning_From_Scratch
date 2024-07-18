#3.4.2 각 층의 신호 전달 구현하기
import numpy as np

def sigmoid(x): #시그모이드 함수
    return 1 / (1 + np.exp(-x))

def identity_fuction(x): #항등 함수
    return x


X = np.array([1.0,0.5]) #입력
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) #가중치
B1 = np.array([0.1,0.2,0.3]) #편향 (Bias)

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X,W1) + B1 #Forward 수행
Z1 = sigmoid(A1) #결과를 활성화 함수인 시그모이드 함수로 전달
print(A1)
print(Z1)

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]]) #가중치
B2 = np.array([0.1,0.2]) #편향

print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1,W2) + B2 #위와 동일
Z2 = sigmoid(A2)

print(Z2)

W3 = np.array([[0.1,0.3],[0.2,0.4]]) #위와 동일
B3 = np.array([0.1,0.2])

A3 = np.dot(Z2,W3) + B3
Z3 = identity_fuction(A3) #활성화 함수로 항등 함수 사용

print(A3)
print(Z3)