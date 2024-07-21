#4.2.2 교차 엔트로피 오차 (Cross Entropy Error)

import numpy as np

def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))  #delta를 더해주는 이유? np.log함수에 0을 입력하면 -inf가 되기 때문

#정답은 2
t = [0,0,1,0,0,0,0,0,0,0]

# ex1) 정답이 2일 확률이 가장 높다고 추정
y1 = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
print("ex1의 CEE: "+ str(cross_entropy_error(np.array(y1),np.array(t))))

# ex1) 정답이 7일 확률이 가장 높다고 추정
y2 = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
print("ex2의 CEE: "+ str(cross_entropy_error(np.array(y2),np.array(t))))
