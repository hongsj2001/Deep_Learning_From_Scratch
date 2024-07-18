#3.2.7 ReLU 함수

import numpy as np
import matplotlib.pylab as plt
def relu(x): #0이하면 0, 0보다 크면 그대로 출력
        return np.maximum(0,x)

x = np.arange(-5.0,5.0,0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-0.1,5.0)
plt.show()
