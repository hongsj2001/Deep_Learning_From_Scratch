#4.3.1 미분

#미분 구현 시 나쁜 예 -> why?
#1. 반올림 오차 문제 발생 (소숫점 8자리 이하가 생략되어 최종 계산 오차 발생)
#2. 이와 같은 구현은 x와 x+h 사이의 기울기에 해당하므로 x에서의 기울기가 X -> x+h와 x-h의 기울기 계산으로 변경
def wrong_numerical_diff(f,x):
    h = 1e-50
    return (f(x+h) - f(x)) / h

#중앙 차분
def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)
