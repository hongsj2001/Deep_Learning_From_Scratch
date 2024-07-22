#6.4.2 가중치 감소

import os
import sys
sys.path.append(os.pardir)
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist #dataset 폴더의 mnist.py에서 load_mnist 함수 불러옴
from common.multi_layer_net_extend import MultiLayerNetExtend #common 폴더의 multi_layer_net_extend에서 MultiLayerExtend 클래스 불러옴
from common.trainer import Trainer #common 폴더의 trainer.py에서 Trainer 클래스 불러옴

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

#훈련 데이터를 줄여서 오버피팅 유도
x_train = x_train[:300]
t_train = t_train[:300]

# 드롭아웃 사용 여부와 비율 설정
use_dropout = True  # 드롭아웃 사용 여부 (쓰지 않을 때는 False)
dropout_ratio = 0.2 #드롭아웃 비율


#입력 뉴런 28X28 = 784, 뉴런 100개를 갖는 5층 hidden layer, 출력 뉴런 10개를 갖는 신경망 생성, 드롭 아웃 비율은 0.2로 설정하고 드롭아웃 사용
network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100, 100],
                              output_size=10, use_dropout=use_dropout, dropout_ration=dropout_ratio)
trainer = Trainer(network, x_train, t_train, x_test, t_test,
                  epochs=301, mini_batch_size=100,
                  optimizer='sgd', optimizer_param={'lr': 0.01}, verbose=True)
trainer.train()

train_acc_list, test_acc_list = trainer.train_acc_list, trainer.test_acc_list




markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, marker='o', label='train', markevery=10)
plt.plot(x, test_acc_list, marker='s', label='test', markevery=10)
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()