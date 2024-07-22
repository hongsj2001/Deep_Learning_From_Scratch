#가중치의 초깃값

import numpy as np
import matplotlib.pyplot as plt


#시그모이드 함수 구현
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Relu 함수 구현
def ReLU(x):
    return np.maximum(0, x)

#하이퍼 탄젠트 함수 구현
def tanh(x):
    return np.tanh(x)
    
input_data = np.random.randn(1000, 100)  #1000X100 모양의 랜덤 데이터 생성
node_num = 100 
hidden_layer_size = 5  #은닉층 5개
activations = {}  # 활성화 결과를 저장

x = input_data

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-1]

    w = np.random.randn(node_num, node_num) * 1
    # w = np.random.randn(node_num, node_num) * 0.01
    # w = np.random.randn(node_num, node_num) * np.sqrt(1.0 / node_num)
    # w = np.random.randn(node_num, node_num) * np.sqrt(2.0 / node_num)


    a = np.dot(x, w)


    z = sigmoid(a)
    # z = ReLU(a)
    # z = tanh(a)

    activations[i] = z

# 히스토그램 그리기
for i, a in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    if i != 0: plt.yticks([], [])
    # plt.xlim(0.1, 1)
    # plt.ylim(0, 7000)
    plt.hist(a.flatten(), 30, range=(0,1))
plt.show()