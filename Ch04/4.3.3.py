#4.3.3 편미분

import numpy as np

#   y = x1^2 + x2^2 
def func_2(x):
    #return np.sum(x**2)
    return x[0]**2 + x[1]**2

def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

#x0=3,x1=4 일 때 x0에 대한 편미분
def func_tmp1(x0):
    return x0*x0 + 4.0**2.0
#x0=3,x1=4 일 때 x1에 대한 편미분
def func_tmp2(x1):
    return 3.0**2.0 + x1*x1

print(numerical_diff(func_tmp1,3.0))
print(numerical_diff(func_tmp2,4.0))
