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

x = np.arange(0.0,20.0,0.1)
y = func_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(func_1, 5)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()


