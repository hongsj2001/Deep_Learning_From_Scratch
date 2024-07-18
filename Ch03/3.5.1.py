#3.5.1 소프트맥스 함수 구현하기

import numpy as np

def softmax(a):
    exp_a = np.exp(a) #넘파이 배열의 각 원소에 exp연산 수행
    sum_exp_a = np.sum(exp_a) #exp연산을 수행한 배열의 원소들의 합 계산
    y = exp_a / sum_exp_a #합으로 나눔
    return y

a = np.array([0.3,2.9,4.0])

exp_a = np.exp(a)
print(exp_a)

sum_exp_a = np.sum(exp_a)
print(exp_a)

y = exp_a / sum_exp_a
print(y)

print(softmax(a))