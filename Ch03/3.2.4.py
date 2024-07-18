#3.2.3 시그모이드 함수 구현하기

import numpy as np
import matplotlib.pylab as plt

def sigmoid(x): # 넘파이를 이용한 시그모이드 함수 구현
    return 1 / (1 + np.exp(-x)) #행렬의 각 원소에 1/(1+exp^(-x)) 연산 수행

x = np.array([-1.0,1.0,2.0])
print(sigmoid(x))
t = np.array([1.0,2.0,3.0])
print(1.0+t)

print(1.0/t)

x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

