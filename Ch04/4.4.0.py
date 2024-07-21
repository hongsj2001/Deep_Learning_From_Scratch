#4.4.0 기울기 
#편미분을 동시에 계산

import numpy as np

# y = x1^2 + x2^2
def func(x):
    #return np.sum(x**2)
    return x[0]**2 + x[1]**2


#편미분
def numerical_gradient(f,x):
    h = 1e-4 #0.0001
    grad = np.zeros_like(x) #x와 모양이 같은 0배열 생성

    #각 변수에 대한 편미분 진행 후 grad에 저장
    for idx in range(x.size):

        tmp_val = x[idx]

        # f(x+h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)

        x[idx] = tmp_val # 기존 값 복원

    return grad

print(numerical_gradient(func,np.array([3.0,4.0])))
print(numerical_gradient(func,np.array([0.0,2.0])))
print(numerical_gradient(func,np.array([3.0,0.0])))