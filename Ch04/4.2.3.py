#4.2.3 미니배치 학습

import sys, os
import numpy as np
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label= True)

print(x_train.shape)
print(t_train.shape)

train__size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train__size,batch_size)

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(x_batch)
print(t_batch)