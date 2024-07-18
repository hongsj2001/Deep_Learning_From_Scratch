#3.5.1 소프트맥스 함수 구현하기

import numpy as np

def naive_softmax(a): 
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([0.3,2.9,4.0])

print(naive_softmax(a))