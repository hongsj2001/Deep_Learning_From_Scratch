#3.6.2 신경망의 추론 처리

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

def get_data():
    (x_train, t_train) , (x_test,t_test) = load_mnist(flatten = True, normalize = False)
    return x_test, t_test

def init_network():
    with open('sample_weight.pkl', 'rb') as f: #피클 파일을 읽어옴
        network = pickle.load(f)
    return network

def predict(network, x):
    W1,W2,W3 = network['W1'], network['W2'], network['W3']
    b1,b2,b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    y = softmax(a3)

    return y

x,t =get_data()
network = init_network()

accuracy_cnt = 0

for i in range(len(x)):
    y = predict(network, x[i]) #forward
    p = np.argmax(y) #예측값을 찾아냄
    if(p == t[i]): #예측 성공시 accuracy_cnt를 1올림
        accuracy_cnt += 1

print("Accuracy : " + str(float((accuracy_cnt / len(x))))) #정확도 계산