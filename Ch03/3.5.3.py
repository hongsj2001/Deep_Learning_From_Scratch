#3.5.3 소프트맥스 함수의 특징
#소프트맥스 함수의 출력은 0에서 1사이의 실수로 표현된다. 즉, 소프트맥스 함수의 출력은 '확률'로 해석가능
#머신러닝은 학습과 추론 두 단계로 이루어지는데 학습 단계에서 소프트맥스를 사용하고 추론 단계에서는 생략 가능

import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([0.3,2.9,4.0])
y = softmax(a)
print(y)

print(np.sum(y)) #합이 1