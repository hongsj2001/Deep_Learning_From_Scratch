#6.1 매개변수 갱신

import os
import sys
sys.path.append(os.pardir) #부모디렉토리 호출을 위함
import matplotlib.pyplot as plt 
from dataset.mnist import load_mnist #dataset 폴더의 mnist.py에 정의된 load_mnist 함수를 불러옴
from common.util import smooth_curve #common 폴더의 util.py에 정의된 smooth_curve 함수를 불러옴
from common.multi_layer_net import MultiLayerNet #common 폴더의 multi_layer_net에 정의된 MultiLayerNet 클래스를 불러옴
from optimizer import *



#정규화 시킨 MNIST 데이터셋을 불러옴
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

train_size = x_train.shape[0]
batch_size = 128 #배치 크기
max_iterations = 2000 #반복 횟수


optimizers = {} #optimizer들을 저장할 딕셔너리 생성
optimizers['SGD'] = SGD() 
optimizers['Momentum'] = Momentum()
optimizers['AdaGrad'] = AdaGrad()
optimizers['Adam'] = Adam()

#각 opimizer들에 대한 신경망과 Loss 값을 저장할 딕셔너리 생성
networks = {}
train_loss = {}

#각 optimizer들에 대해 다중 신경망 생성 및 Loss값을 저장할 리스트 생성
for key in optimizers.keys():
    networks[key] = MultiLayerNet(
        input_size=784, hidden_size_list=[100, 100, 100, 100],
        output_size=10)
    train_loss[key] = []    


#훈련 시작
for i in range(max_iterations):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    #각 optimizer들에 대해 기울기 계산 및 가중치 업데이트
    for key in optimizers.keys():
        grads = networks[key].gradient(x_batch, t_batch)
        optimizers[key].update(networks[key].params, grads)

        #Loss값 계산 후 저장
        loss = networks[key].loss(x_batch, t_batch)
        train_loss[key].append(loss)
    

    #100회 수행 시 마다 Loss 값 출력
    if i % 100 == 0:
        print( "===========" + "iteration:" + str(i) + "===========")
        for key in optimizers.keys():
            loss = networks[key].loss(x_batch, t_batch)
            print(key + ":" + str(loss))


# 그래프 그리기
markers = {"SGD": "o", "Momentum": "x", "AdaGrad": "s", "Adam": "D"}
x = np.arange(max_iterations)
for key in optimizers.keys():
    plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.ylim(0, 1)
plt.legend()
plt.show()