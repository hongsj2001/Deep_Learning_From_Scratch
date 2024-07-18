#2.3.3 가중치와 편향 구현하기
import numpy as np


def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7 #기존 임계값에 -를 붙여서 편향 구현

    tmp = np.sum(w*x)+b #각 원소 곱의 합에 편향을 더한다.

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
    
def OR(x1,x2): #이전에서는 OR를 가중치 1,1로 구현했지만, 기존 AND게이트에서 임계값을 0.5 낮춰서 구현 가능
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2 

    tmp = np.sum(w*x)+b 

    if(tmp <= 0):
        return 0
    else:
        return 1    

print("\nAND 게이트")    
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

print("\nNAND 게이트")    
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))

print("\nOR 게이트")
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))