#2.3.2 가중치와 편향 도입 

import numpy as np
x = np.array([0,1])
w = np.array([0.5,0.5])
b = -0.7    #기존 theta를 -b로 치환

print(x*w)

print(sum(w*x))
print(sum(w*x)+b)