#4.4.1 경사법 (경사 하강법)

import numpy as np
import matplotlib.pylab as plt
from gradient_2d import numerical_gradient #gradient_2d 내의 numerical_gradient 함수 사용

#경사 하강법 구현
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x #초깃값
    x_history = [] #x의 변화를 보기 위한 리스트 생성

    for i in range(step_num): #100회 반복
        x_history.append( x.copy() ) #리스트에 x값 추가

        grad = numerical_gradient(f, x) #편미분
        x -= lr * grad #경사하강법

    return x, np.array(x_history) #x값과 x값의 변화를 표현한 리스트 리턴


def function_2(x): #x0^2 + x1^2
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0]) #초기값 설정

lr = 0.1 #학습률
step_num = 20 #반복 횟수
x, x_history = gradient_descent(function_2, init_x, lr=lr, step_num=step_num)

plt.plot( [-5, 5], [0,0], '--b')
plt.plot( [0,0], [-5, 5], '--b')
plt.plot(x_history[:,0], x_history[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()