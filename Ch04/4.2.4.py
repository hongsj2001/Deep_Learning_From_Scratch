#4.2.4 배치용 교차 엔트로피 오차 구현하기

import sys, os
import numpy as np
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

def cross_entropy_error1(y,t):
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)

    batch_size = y.shape[0]
    return -np.sum(t*np.log(y+1e-7)) / batch_size

def cross_entropy_error2(y,t):
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t]+ 1e-7)) / batch_size

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label= True)
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size,batch_size)

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(cross_entropy_error1(x_batch,t_batch))
print(cross_entropy_error2(x_batch,t_batch))