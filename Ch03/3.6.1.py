#3.6.1 MNIST데이터셋 
#MNIST는 숫자 손글씨에 대한 이미지 데이터와 라벨을 가짐
import numpy as np
import sys, os 
sys.path.append(os.pardir) # *주의사항* 파일 실행 시 실행 위치를 파일이 존재하는 디렉토리 위치로 변경해야함 or 파일의 절대 위치로 주소 변경
from dataset.mnist import load_mnist #dataset의 mnist에서 load_mnist 함수를 불러옴
from PIL import Image #이미지 관련 라이브러리

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img)) #Numpy배열로 표현된 이미지 배열을 사진으로 변환
    pil_img.show() #이미지 출력



#1X28X28짜리 배열을 1차원 배열로 변경하여 불러옴 -> 1X28X28 = 784
#x_train은 이미지 배열, t_train은 이미지에 대한 정수 배열 
# ex) x_train[0]이 이미지 5를 표현한다면, t_train[0]은 정수 5

(x_train, t_train) , (x_test,t_test) = load_mnist(flatten = True, normalize = False) 

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape) #flatten을 True로 설정했으므로 1차원 배열임
img = img.reshape(28,28) #이미지로 표현하기 위해 28X28로 재배치
print(img.shape)

img_show(img) #이미지 출력