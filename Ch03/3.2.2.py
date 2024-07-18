#3.2.2 계단 함수 구현하기

import numpy as np

def step_func(x): #0보다 크면 1, 작으면 0 리턴
    if(x > 0):
        return 1
    else:
        return 0
    
def np_step_func(x): #넘파이를 이용한 구현
    y = x > 0 #x의 원소들 중 0보다 큰 원소들은 True, 아니면 False로 변환
    return y.astype(np.int) #True는 1, False는 0으로 변환

x = np.array([-1.0,1.0,2.0])
print(x)

y = x>0
print(y)

print(y.astype(np.int32))