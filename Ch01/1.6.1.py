#1.6.1 matplotlib를 이용한 그래프 그리기
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1) #0부터 6까지 0.1간격으로 생성
y = np.sin(x) #Sin 그래프 생성

plt.plot(x,y)
plt.show()