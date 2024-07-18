#2.3.1 간단한 구현부터 - AND게이트 구현

def AND(x1,x2): #AND 게이트 구현 (입력으로 x1,x2를 받고 각 신호의 가중치 곱의 합이 임계치(theta)를 넘으면 1 출력 그렇지 않으면 0 출력)
    w1,w2, theta = 0.5,0.5,0.7 #가중치와 임계값 설정
    tmp = x1*w1 + x2*w2 #AND 연산 진행 

    if(tmp <= theta): #결과가 임계값보다 작으면 0, 크면 1 출력
        return 0
    else:
        return 1

#OR , NAND 게이트 추가
def OR(x1,x2): 
    w1,w2, theta = 1,1,0.7 #가중치와 임계값 설정
    tmp = x1*w1 + x2*w2 #AND 연산 진행 

    if(tmp <= theta): #결과가 임계값보다 작으면 0, 크면 1 출력
        return 0
    else:
        return 1

def NAND(x1,x2): 
    w1,w2, theta = -0.5,-0.5,-0.7 #기존 AND게이트에서 가중치, 임계값에 -부호를 붙여서 구현
    tmp = x1*w1 + x2*w2

    if(tmp <= theta):
        return 0
    else:
        return 1

print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))

print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))