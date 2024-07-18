#3.4.3 구현 정리

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identity_fuction(x):
    return x

def init_network():
    network = {} #딕셔너리 생성
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) #2개->3개
    network['b1'] = np.array([0.1,0.2,0.3]) # 편향 (bias) 
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]]) #2층 뉴런 3개
    network['b2'] = np.array([0.1,0.2]) #편향
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]]) #3층 뉴런
    network['b3'] = np.array([0.1,0.2])

    return network


def forward(network, x):
    
    #입력받은 딕셔너리에서 가중치와 편향을 불러옴
    W1,W2,W3 = network['W1'], network['W2'], network['W3']
    b1,b2,b3 = network['b1'], network['b2'], network['b3']
    
    #신호 전달 과정
    a1 = np.dot(x,W1) + b1 
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    y = identity_fuction(a3)

    return y


network = init_network()

x = np.array([1.0,0.5])
y = forward(network,x)
print(y)