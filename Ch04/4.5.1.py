#4.5.1 2층 신경망 클래스 구현하기

import sys, os
sys.path.append(os.pardir)
from common.functions import* #common 폴더 내 function.py에 정의된 모든 함수를 불러옴
from common.gradient import numerical_gradient #common 폴더 내 gradient.py에 정의된 numerical_gradient 함수를 불러옴


#2층 신경망 클래스 구현
class TwoLayerNet:
    
    #초기화 진행 / 입력층 뉴런 수, 은닉 층 뉴런 수, 출력 층 뉴런 수, 초기 가중치 
    def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01): 
        self.params = {} #파라미터들을 저장할 딕셔너리
        
        #1층 
        self.params['W1'] = weight_init_std * np.random.randn(input_size,hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        
        #2층
        self.params['W2'] = weight_init_std*np.random.randn(hidden_size,output_size)
        self.params['b2'] = np.zeros(output_size)


    def predict(self,x): #순전파 구현
        W1,W2 = self.params['W1'], self.params['W2'] #param 딕셔너리에서 Weight 불러옴
        b1,b2 = self.params['b1'], self.params['b2'] #param 딕셔너리에서 Bias 불러옴

        a1 = np.dot(x,W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1,W2) + b2
        y = softmax(a2)

        return y
    
    def loss(self,x,t): #Loss 계산, x는 입력 레이블, t는 정답 레이블
        y = self.predict(x) #순전파 출력 결과

        return cross_entropy_error(y,t) #출력 결과에 CEE 계산
    
    def accuracy(self,x,t): #정확도 계산
        y = self.predict(x) #순전파 계산
        y = np.argmax(y, axis=1) #결과를 1차원 배열로 변환
        t = np.argmax(t, axis=1) #정답 레이블을 1차원 배열로 변환

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
    
    #편미분
    def numerical_gradient(self,x,t):
        loss_W = lambda W: self.loss(x,t)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])

        return grads
    


#784개의 입력, hidden layer 100개, output layer 10개의 신경망 생성
net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
print(net.params['W1'].shape)
print(net.params['b1'].shape)
print(net.params['W2'].shape)
print(net.params['b2'].shape)

x = np.random.randn(100,784) #100X784 모양의 랜덤 배열 생성
y = net.predict(x)

print(x)
print(y)

x = np.random.randn(100,784) #100X784 모양의 랜덤 배열을 입력으로 사용
t = np.random.randn(100,10)  #100X10 모양의 랜덤 배열을 정답 레이블로 사용
print(x)
print(t)
        
grads = net.numerical_gradient(x,t)

print(grads['W1'].shape)
print(grads['b2'].shape)
print(grads['W2'].shape)
print(grads['b2'].shape)