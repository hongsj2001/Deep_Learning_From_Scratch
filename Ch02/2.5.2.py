#2.5.2 XOR 게이트 구현하기
import numpy as np


# AND, NAND, OR게이트 구현은 기존과 동일
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7

    tmp = np.sum(w*x)+b

    if(tmp <= 0):
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7

    tmp = np.sum(w*x)+b

    if(tmp <= 0):
        return 0
    else:
        return 1
    
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2

    tmp = np.sum(w*x)+b

    if(tmp <= 0):
        return 0
    else:
        return 1
    

#AND, OR, NAND로 XOR 구현 가능
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))
