#3.5.2 소프트맥스 함수 구현 시 주의점 (오버플로우)
import numpy as np

#

def softmax(a): #오버플로우 문제를 해결한 소프트맥스 함수 구현
    c = np.max(a) #원소들 중 최댓값을 구함
    exp_a = np.exp(a - c) #각 원소들에 최댓값을 뺀 후 exp연산 수행
    sum_exp_a = np.sum(exp_a) #각 원소들을 더함
    y = exp_a / sum_exp_a #각 원소들에 합을 나눔
    return y

a = np.array([1010,1000,990])
print(softmax(a))