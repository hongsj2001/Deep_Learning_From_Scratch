#4.3.2 수치 미분의 예

import numpy as np
import matplotlib.pylab as plt

# y = 0.01x^2 + 0.1x
def func_1(x):
    return 0.01*x**2 + 0.1*x


#수치 미분
def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

#주어진 점에서의 접선 구하기
def tangent_line(f, x):
    d = numerical_diff(f, x) #수치 미분을 이용한 접선의 기울기
    #print(d)
    y = f(x) - d*x #y절편
    return lambda t: d*t + y

print(numerical_diff(func_1,5))
print(numerical_diff(func_1,10))


#그래프 생성
x = np.arange(0.0,20.0,0.1) #x값 범위 : 0부터 20까지 0.1단위로 끊어서 생성
y = func_1(x) #y값
plt.xlabel("x") #x축 이름
plt.ylabel("f(x)") #y축 이름

tf = tangent_line(func_1, 5) #x=5에서의 접선
y2 = tf(x)

plt.plot(x, y,label="f(x)")
plt.plot(x, y2, label="Tangent Line")
plt.legend()
plt.show()


