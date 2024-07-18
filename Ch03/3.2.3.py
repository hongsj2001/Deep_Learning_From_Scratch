#3.2.3 계단 함수의 그래프

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int64)

x = np.arange(-5.0,5.0,0.1) #x값 범위 -5부터 5까지 0.1 단위로
y = step_function(x)
plt.plot(x,y) #그래프를 그림
plt.ylim(-0.1,1.1) #y축 범위 -0.1부터 1.1 까지
plt.show() #그래프 출력