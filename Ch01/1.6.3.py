#1.6.3 이미지 표시하기
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('c:/HONG/Deep_Learning_From_Scratch/Ch01/image.jpg') #이미지를 불러옴

plt.imshow(img) #이미지 출력
plt.show()