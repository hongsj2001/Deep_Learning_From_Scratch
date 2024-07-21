#4.2.4 배치용 교차 엔트로피 오차 구현하기

import sys, os
import numpy as np
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

 #정답 레이블이 원 핫 인코딩 형식으로 주어졌을 때
def cross_entropy_error1(y,t): #y는 신경망 출력, t는 정답 레이블
    if y.ndim == 1: #데이터가 하나인 경우
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)

    batch_size = y.shape[0]
    return -np.sum(t*np.log(y+1e-7)) / batch_size

#정답 레이블이 숫자 레이블로 주어졌을 때
def cross_entropy_error2(y,t): #y는 신경망 출력, t는 정답 레이블
    if y.ndim == 1: #데이터가 하나인 경우
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t]+ 1e-7)) / batch_size