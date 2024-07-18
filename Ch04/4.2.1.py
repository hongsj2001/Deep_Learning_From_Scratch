# 4.2.1 오차제곱합
import numpy as np

def sum_of_sqaures_for_error(y,t):
    return 0.5*np.sum((y-t)**2)

#정답은 2
t = [0,0,1,0,0,0,0,0,0,0]

# ex1) 정답이 2일 확률이 가장 높다고 추정
y1 = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
print("ex1의 오차제곱합: "+ str(sum_of_sqaures_for_error(np.array(y1),np.array(t))))

# ex1) 정답이 7일 확률이 가장 높다고 추정
y2 = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
print("ex2의 오차제곱합: "+ str(sum_of_sqaures_for_error(np.array(y2),np.array(t))))


