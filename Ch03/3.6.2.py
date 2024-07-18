#3.6.2 신경망의 추론 처리

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax
from PIL import Image


def img_show(img): #이미지 출력
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

def get_data(): #MNIST 테스트 데이터 가져옴
    (x_train, t_train) , (x_test,t_test) = load_mnist(flatten = True, normalize = False)
    return x_test, t_test

def init_network(): #피클 파일로부터 가중치 데이터를 가져옴
    with open('sample_weight.pkl', 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x): #입력 데이터에 대해 신호 전달 구현
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

accuracy_cnt = 0 #예측에 성공한 횟수 

for i in range(len(x)): #데이터 갯수 만큼 실행 (테스트 이미지셋은 10000개 이므로 10000회 실행)
    y = predict(network, x[i]) #신호 전달
    p = np.argmax(y) #소프트맥스 함수의 출력이므로 가장 높은 확률을 가진 인덱스 출력
    if(p == t[i]): #예측 결과와 일치하면 카운트 증가
        accuracy_cnt += 1


print("Accuracy : " + str(float((accuracy_cnt / len(x))))) #(맞춘 횟수 / 전체 실행 횟수) 로 정확도 출력