#4.4.2 신경망에서의 기울기

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from common.functions import softmax, cross_entropy_error #common 폴더의 functions.py에 정의된 softmax, cee 함수 불러옴
from common.gradient import numerical_gradient #common 폴더의 gradient.py에 정의된 numerical_gradient 함수 불러옴


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # 2X3 모양의 랜덤 정규분포로 초기화

    def predict(self, x): #순전파 계산
        return np.dot(x, self.W) #x와 가중치 곱연산 수행

    def loss(self, x, t): #loss 계산
        z = self.predict(x) #순전파
        y = softmax(z) #소프트맥스 함수를 활성화 함수로 사용
        loss = cross_entropy_error(y, t) #CEE 계산

        return loss

x = np.array([0.6, 0.9]) #입력
t = np.array([0, 0, 1]) #정답 레이블

net = simpleNet() #simpleNet 클래스 생성

f = lambda w: net.loss(x, t) #loss 계산 수행
dW = numerical_gradient(f, net.W) #기울기 계산

print(dW)